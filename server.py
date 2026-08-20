import json, sqlite3, os, secrets
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

ROOT=os.path.dirname(os.path.abspath(__file__))
DB=os.path.join(ROOT,'jastech.db')
DEFAULT={"name":"JasTech Recrutamento & Seleção","cnpj":"","location":"Carandaí/MG e região.","heroTitle":"Conectando talentos às melhores oportunidades.","heroText":"A JasTech aproxima empresas e profissionais e organiza as etapas de recrutamento e seleção.","whatsapp":"5531999999999","primary":"#1769ff","nav":"#071b3a","bg":"#f5f8fc","text":"#10213d","layout":"classic","buttonStyle":"rounded","mediaImage":"","mediaVideo":"","password":"1234","jobs":[{"id":1,"title":"Auxiliar Administrativo","area":"Administrativo","city":"Carandaí/MG","type":"Efetivo","active":True},{"id":2,"title":"Vendedor(a)","area":"Vendas","city":"Carandaí/MG","type":"Efetivo","active":True},{"id":3,"title":"Auxiliar de Produção","area":"Produção","city":"Região","type":"Efetivo","active":True}],"candidates":[],"companies":[],"stages":["Cadastro recebido","Triagem de currículo","Entrevista JasTech","Finalista / encaminhado para entrevista","Aprovado","Não aprovado"]}

def conn():
    c=sqlite3.connect(DB); c.execute('CREATE TABLE IF NOT EXISTS app_state (id INTEGER PRIMARY KEY CHECK(id=1), data TEXT NOT NULL, updated_at TEXT DEFAULT CURRENT_TIMESTAMP)'); c.commit(); return c

def load():
    c=conn(); row=c.execute('SELECT data FROM app_state WHERE id=1').fetchone(); c.close()
    if not row:
        save(DEFAULT); return DEFAULT.copy()
    try: return json.loads(row[0])
    except: save(DEFAULT); return DEFAULT.copy()

def save(d):
    c=conn(); c.execute('INSERT INTO app_state(id,data) VALUES(1,?) ON CONFLICT(id) DO UPDATE SET data=excluded.data,updated_at=CURRENT_TIMESTAMP',(json.dumps(d,ensure_ascii=False),)); c.commit(); c.close()

class Handler(SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs): super().__init__(*args,directory=ROOT,**kwargs)
    def send_json(self, obj, status=200):
        raw=json.dumps(obj,ensure_ascii=False).encode(); self.send_response(status); self.send_header('Content-Type','application/json; charset=utf-8'); self.send_header('Content-Length',str(len(raw))); self.send_header('Cache-Control','no-store'); self.end_headers(); self.wfile.write(raw)
    def do_GET(self):
        path=urlparse(self.path).path
        if path=='/health': return self.send_json({'ok':True,'service':'JasTech'})
        if path=='/api/state': return self.send_json(load())
        if path=='/api/jobs':
            d=load(); return self.send_json([j for j in d.get('jobs',[]) if j.get('active') is True])
        return super().do_GET()
    def do_POST(self):
        path=urlparse(self.path).path
        if path!='/api/state': return self.send_json({'error':'Not found'},404)
        try:
            n=int(self.headers.get('Content-Length','0')); body=self.rfile.read(n); d=json.loads(body.decode('utf-8'))
            if not isinstance(d,dict) or not isinstance(d.get('jobs'),list): raise ValueError('estado inválido')
            save(d); return self.send_json({'ok':True,'state':d})
        except Exception as e: return self.send_json({'ok':False,'error':str(e)},400)

if __name__=='__main__':
    port=int(os.environ.get('PORT','8000')); conn().close(); print(f'JasTech online em http://localhost:{port}'); ThreadingHTTPServer(('0.0.0.0',port),Handler).serve_forever()
