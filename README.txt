JasTech — versão com comandos do Financeiro corrigidos.

Os botões “Ver empresas” e “Ver cobranças” agora usam listeners exclusivos e funcionam por clique, sem onclick duplicado.
<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>JasTech | Recrutamento & Seleção</title>
<style>
:root{--nav:#071b3a;--blue:#1769ff;--cyan:#23b7ff;--bg:#f5f8fc;--white:#fff;--text:#10213d;--muted:#64748b;--line:#e3e9f1;--danger:#dc3545}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Arial,sans-serif;color:var(--text);background:var(--bg)}a{text-decoration:none;color:inherit}.wrap{width:min(1120px,92%);margin:auto}
header{background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:20}.nav{height:72px;display:flex;align-items:center;justify-content:space-between}.logo{font-weight:900;font-size:26px;color:var(--nav)}.logo span{color:var(--blue)}nav{display:flex;gap:20px;font-weight:700;font-size:14px}.btn{border:0;padding:12px 17px;border-radius:10px;font-weight:800;cursor:pointer;display:inline-block}.primary{background:var(--blue);color:#fff}.light{background:#fff;border:1px solid #d8e0eb;color:var(--nav)}.danger{background:var(--danger);color:#fff}
.hero{background:linear-gradient(135deg,#061833,#0d3f80);color:#fff;padding:82px 0}.heroGrid{display:grid;grid-template-columns:1.15fr .85fr;gap:45px;align-items:center}.ey{color:#72d8ff;font-size:12px;font-weight:900;letter-spacing:1.5px;text-transform:uppercase}.hero h1{font-size:clamp(42px,6vw,67px);line-height:1.03;margin:15px 0;letter-spacing:-2px}.hero p{font-size:18px;color:#dbeafe;max-width:650px}.actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:25px}.glass{background:#ffffff12;border:1px solid #ffffff2b;border-radius:20px;padding:24px}.flow div{padding:12px;background:#ffffff10;border-radius:9px;margin:8px 0}.flow b{color:var(--cyan)}
section{padding:70px 0}.head{text-align:center;max-width:700px;margin:0 auto 35px}.head h2{font-size:38px;margin:0 0 10px}.head p,.card p,.muted{color:var(--muted)}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:17px}.card,.box,.panel{background:#fff;border:1px solid var(--line);border-radius:16px;padding:22px}.icon{font-size:26px}.split{display:grid;grid-template-columns:1fr 1fr;gap:20px}.dark{background:var(--nav);color:#fff;border-color:var(--nav)}.dark p{color:#dbeafe}.check{margin:10px 0}.check b{color:var(--cyan)}
.jobs{display:grid;gap:13px}.availableJobs{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:30px}
.jobCompany{font-weight:800;color:var(--blue);margin-bottom:8px;font-size:14px}
.availableCard .jobDetails{margin-top:8px;line-height:1.45}
.availableCard .apply-job-btn{margin-top:16px;width:100%}
.availableCard{background:#fff;border:1px solid var(--line);border-radius:16px;padding:20px;box-shadow:0 6px 18px #10213d0d}.availableCard h3{margin:0 0 8px;font-size:20px}.availableCard .jobMeta{margin:10px 0}.availableCard .btn{width:100%;text-align:center;margin-top:12px}.availableHeader{display:flex;justify-content:space-between;align-items:end;gap:15px;margin-bottom:15px}.availableHeader h3{margin:0;font-size:25px}.availableCount{font-weight:800;color:var(--blue)}.job{background:#fff;border:1px solid var(--line);border-radius:14px;padding:20px;display:flex;justify-content:space-between;align-items:flex-start;gap:20px}.jobMain{flex:1}.jobTitle{font-size:20px;margin-bottom:8px}.jobMeta{display:flex;flex-wrap:wrap;gap:7px;margin:8px 0}.jobDetails{margin-top:10px;color:#475569;line-height:1.55}.jobDetails b{color:#172033}.jobActions{display:flex;flex-direction:column;gap:8px;align-items:stretch;min-width:150px}.jobActions .btn{text-align:center}.jobSelectBox{margin-top:16px;padding:14px;border:1px dashed var(--line);border-radius:12px;background:#f8fafc}.tag{font-size:12px;background:#eaf2ff;color:#1557c8;padding:4px 8px;border-radius:20px;font-weight:800}
form{display:grid;gap:13px}.row{display:grid;grid-template-columns:1fr 1fr;gap:13px}label{font-size:13px;font-weight:800}input,select,textarea{width:100%;padding:11px;margin-top:6px;border:1px solid #d8e0eb;border-radius:9px;font:inherit}textarea{min-height:100px}.note{font-size:12px;color:var(--muted);background:#f4f7fb;padding:11px;border-radius:8px}.msg{font-weight:700;margin-top:8px}
.cta{background:linear-gradient(135deg,#0b2b5d,#1769ff);color:#fff;border-radius:22px;padding:38px;display:flex;justify-content:space-between;align-items:center}.cta h2{font-size:32px;margin:0}
footer{background:#06152d;color:#cbd5e1;padding:38px 0}.foot{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:25px}.ft{font-weight:900;color:#fff;margin-bottom:9px}
#admin{display:none;background:#eef5ff;min-height:100vh;padding:55px 0}.adminTop{display:flex;justify-content:space-between;gap:15px;align-items:center}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:20px 0}.stat{background:#fff;border:1px solid var(--line);padding:18px;border-radius:14px}.stat strong{display:block;color:var(--blue);font-size:29px;margin-top:7px}table{width:100%;border-collapse:collapse}th,td{text-align:left;padding:10px;border-bottom:1px solid var(--line);font-size:13px}.adminNav{display:flex;gap:8px;flex-wrap:wrap;margin:18px 0}.hidden{display:none!important}.modal{position:fixed;inset:0;background:#06152dbd;display:none;align-items:center;justify-content:center;padding:20px;z-index:50}.modalBox{background:#fff;border-radius:18px;padding:25px;width:min(460px,100%)}.portalResult{margin-top:18px}.portalHead{display:flex;justify-content:space-between;gap:10px;align-items:center;margin-bottom:12px}.portalCard{border:1px solid var(--line);border-radius:12px;padding:15px;margin-top:10px;background:#f8fbff}.miniStats{display:flex;gap:8px;flex-wrap:wrap}.miniStats span{background:#fff;border:1px solid var(--line);border-radius:10px;padding:9px 12px}.miniStats b{color:var(--blue)}
@media(max-width:800px){nav,header .btn{display:none}.heroGrid,.split,.cards,.foot,.availableJobs{grid-template-columns:1fr}.row,.stats{grid-template-columns:1fr}.job{flex-direction:column;align-items:flex-start}.cta{display:block}.cta .btn{margin-top:18px}.availableHeader{display:block}.availableCount{display:block;margin-top:6px}}

.layoutHero{border-radius:18px;padding:25px;margin-top:14px;background:var(--nav);color:#fff}
.previewMedia{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:12px}
.previewMedia img,.previewMedia video{width:100%;max-height:180px;object-fit:cover;border-radius:12px;border:1px solid var(--line)}
.themeGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.colorBox{display:flex;align-items:center;gap:8px}.colorBox input{width:58px;height:42px;padding:2px}
@media(max-width:800px){.themeGrid,.previewMedia{grid-template-columns:1fr}}
.layout-center .heroGrid{grid-template-columns:1fr;text-align:center}.layout-center .hero p{margin-left:auto;margin-right:auto}.layout-center .actions{justify-content:center}.layout-media .heroGrid{grid-template-columns:.8fr 1.2fr}.layout-media #heroMedia{order:2}.pill-buttons .btn{border-radius:999px}.square-buttons .btn{border-radius:3px}.siteMusicPlayer{position:fixed;left:18px;right:18px;bottom:18px;z-index:40;background:#071b3a;color:#fff;border:1px solid #ffffff22;border-radius:16px;padding:10px 14px;display:grid;grid-template-columns:1fr auto;gap:8px 15px;align-items:center;box-shadow:0 10px 30px #0004}.siteMusicInfo{display:flex;gap:10px;align-items:center;min-width:0}.siteMusicInfo b{display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:55vw}.siteMusicInfo small{display:block;color:#cbd5e1}.siteMusicControls{display:flex;gap:6px}.siteMusicControls button{border:0;background:#ffffff16;color:#fff;border-radius:9px;padding:8px 11px;cursor:pointer}.siteMusicControls .musicPlay{background:#1769ff}.siteMusicProgress{grid-column:1/-1;height:3px;background:#ffffff22;border-radius:99px;overflow:hidden}.siteMusicProgress div{height:100%;width:0;background:#23b7ff}.siteMusicPlayer iframe,.siteMusicPlayer audio{position:absolute;width:1px;height:1px;opacity:0;pointer-events:none}.siteMusicPlayer.hidden{display:none}@media(max-width:650px){.siteMusicPlayer{left:8px;right:8px;bottom:8px}.siteMusicInfo b{max-width:45vw}}</style>
</head>
<body>
<div id="public">
<header><div class="wrap nav"><a class="logo" href="#inicio">Jas<span>Tech</span></a><nav><a href="#empresas">Empresas</a><a href="#vagas">Vagas</a><a href="#candidato">Candidatos</a><a href="#contato">Contato</a></nav><a class="btn primary" href="#empresa">Quero contratar</a></div></header>

<section class="hero" id="inicio"><div class="wrap heroGrid"><div><div class="ey">Recrutamento & Seleção</div><h1 id="heroTitle">Conectando talentos às melhores oportunidades.</h1><p id="heroText">A JasTech aproxima empresas e profissionais e organiza as etapas de recrutamento e seleção.</p><div class="actions"><a class="btn primary" href="#empresa">Quero contratar</a><a class="btn light" href="#candidato">Cadastrar currículo</a></div></div><div><div id="heroMedia" class="previewMedia"></div><div class="glass"><h2>Como funciona</h2><div class="flow"><div><b>01</b> Solicitação da vaga</div><div><b>02</b> Divulgação</div><div><b>03</b> Triagem e entrevista</div><div><b>04</b> Encaminhamento</div><div><b>05</b> Contratação</div></div></div></div></div></section>

<section><div class="wrap"><div class="head"><h2>Soluções</h2><p>Serviços para organizar e facilitar contratações.</p></div><div class="cards"><div class="card"><div class="icon">🎯</div><h3>Recrutamento</h3><p>Atração de profissionais.</p></div><div class="card"><div class="icon">📄</div><h3>Triagem</h3><p>Análise dos currículos.</p></div><div class="card"><div class="icon">💬</div><h3>Entrevistas</h3><p>Entrevistas iniciais.</p></div><div class="card"><div class="icon">⭐</div><h3>Seleção</h3><p>Identificação dos melhores perfis.</p></div><div class="card"><div class="icon">👥</div><h3>Banco de talentos</h3><p>Profissionais para futuras oportunidades.</p></div><div class="card"><div class="icon">🚀</div><h3>Processos em massa</h3><p>Várias contratações.</p></div></div></div></section>

<section id="empresas" style="background:#fff"><div class="wrap split"><div class="box dark"><div class="ey">Para empresas</div><h2>Precisa contratar?</h2><p>Envie sua necessidade e receba candidatos alinhados ao perfil.</p><div class="check"><b>✓</b> Divulgação</div><div class="check"><b>✓</b> Triagem</div><div class="check"><b>✓</b> Entrevistas</div><div class="check"><b>✓</b> Encaminhamento</div><a class="btn light" href="#empresa">Solicitar recrutamento</a></div><div class="box"><h2>Serviços</h2><p>Valores podem ser ajustados conforme o processo.</p><p><b>Divulgação:</b> R$ 150–300</p><p><b>Recrutamento:</b> R$ 400–700</p><p><b>Completo:</b> R$ 700–1.200</p><p><b>Em massa:</b> sob orçamento</p></div></div></section>

<section id="vagas"><div class="wrap"><div class="head"><h2>Vagas disponíveis agora</h2><p>As oportunidades abaixo já estão disponíveis para candidatura. Use a busca quando quiser encontrar uma vaga específica.</p></div><div class="availableHeader"><h3>🔔 Oportunidades abertas</h3><span id="availableCount" class="availableCount"></span></div><div id="availableJobs" class="availableJobs"></div><div class="box" style="margin:28px 0 18px"><div class="availableHeader"><h3>🔎 Pesquisar vagas</h3><span class="muted">Filtre por cargo, área ou cidade</span></div><div class="row"><label style="flex:2">Pesquisar<input id="jobSearch" type="search" placeholder="Ex.: vendedor, administrativo, Carandaí..." autocomplete="off"></label><label>Área<select id="jobAreaFilter"><option value="">Todas as áreas</option></select></label><label>Cidade<input id="jobCityFilter" placeholder="Todas as cidades"></label></div><div id="jobSearchCount" class="muted" style="margin-top:8px"></div></div><div id="jobs" class="jobs"></div></div></section>

<section id="candidato"><div class="wrap"><div class="head"><h2>Cadastre seu currículo</h2><p>Entre para o Banco de Talentos JasTech.</p></div><div class="box"><form id="candidateForm"><div class="row"><label>Nome<input name="name" required></label><label>WhatsApp<input name="phone" required></label></div><div class="row"><label>E-mail de acesso<input name="email" type="email" required></label><label>Senha de acesso<input name="password" type="password" minlength="6" required></label></div><div class="row"><label>Cidade<input name="city" required></label><label>Vaga que deseja se candidatar<input name="jobTitleInput" id="candidateJob" list="jobOptions" placeholder="Digite para buscar ou selecione uma vaga" autocomplete="off" required><datalist id="jobOptions"></datalist></label></div><div class="row"><label>Cargo pretendido<input name="role" required></label><label>Área<select name="area"><option>Administrativo</option><option>Vendas</option><option>Atendimento</option><option>Logística</option><option>Produção</option><option>Construção</option><option>Tecnologia</option><option>Saúde</option><option>Educação</option><option>Serviços gerais</option><option>Primeiro emprego</option></select></label></div><label>Experiência<textarea name="experience"></textarea></label><label>Currículo PDF<input name="resume" type="file" accept=".pdf"></label><div class="note">Para esta versão em um único arquivo, os cadastros ficam armazenados neste navegador. Para receber currículos de todos os candidatos pela internet, é necessário backend/banco de dados.</div><button class="btn primary">Salvar currículo</button><div id="candidateMsg" class="msg"></div></form></div></div></section>

<section id="empresa" style="background:#fff"><div class="wrap"><div class="head"><h2>Solicite uma vaga</h2><p>Cadastre a necessidade da sua empresa.</p></div><div class="box"><form id="companyForm"><div class="row"><label>Empresa<input name="company" required></label><label>Responsável<input name="contact" required></label></div><div class="row"><label>WhatsApp<input name="phone" required></label><label>E-mail de acesso<input name="email" type="email" required></label></div><div class="row"><label>Senha de acesso<input name="password" type="password" minlength="6" required></label><label>Confirme a senha<input name="password2" type="password" minlength="6" required></label></div><div class="row"><label>Cargo<input name="role" required></label><label>Quantidade<input name="quantity" type="number" min="1" value="1"></label></div><div class="row"><label>Cidade<input name="city"></label><label>Salário/benefícios<input name="salary"></label></div><label>Requisitos<textarea name="requirements"></textarea></label><button class="btn primary">Salvar solicitação</button><div id="companyMsg" class="msg"></div></form></div></div></section>

<section id="acessos" style="background:#fff"><div class="wrap"><div class="head"><h2>Acompanhe seu processo</h2><p>Empresas e candidatos têm acesso individual às informações do processo seletivo.</p></div><div class="split"><div class="box"><div class="icon">🏢</div><h3>Área da empresa</h3><p>Acompanhe somente as vagas que sua empresa enviou para recrutamento, candidatos inscritos, finalistas indicados e andamento das etapas.</p><form id="companyLoginForm"><label>E-mail<input name="email" type="email" required></label><label>Senha<input name="password" type="password" required></label><button class="btn primary">Entrar como empresa</button><div id="companyLoginMsg" class="msg"></div></form><div id="companyPortal" class="portalResult hidden"></div></div><div class="box"><div class="icon">👤</div><h3>Área do candidato</h3><p>Consulte o andamento da vaga em que você se inscreveu e veja a etapa atual e a mensagem final da JasTech.</p><form id="candidateLoginForm"><label>E-mail<input name="email" type="email" required></label><label>Senha<input name="password" type="password" required></label><button class="btn primary">Entrar como candidato</button><div id="candidateLoginMsg" class="msg"></div></form><div id="candidatePortal" class="portalResult hidden"></div></div></div></div></section>

<section id="contato"><div class="wrap"><div class="cta"><div><h2>Vamos encontrar o profissional certo?</h2><p id="location">Carandaí/MG e região.</p></div><a id="whats" class="btn light" href="https://wa.me/5531999999999" target="_blank">WhatsApp</a></div></div></section>
<div id="siteMusicPlayer" class="siteMusicPlayer hidden"><div class="siteMusicInfo"><span>🎵</span><div><b id="musicNow">Música</b><small id="musicType">Playlist JasTech</small></div></div><div class="siteMusicControls"><button type="button" onclick="musicPrev()">⏮</button><button type="button" class="musicPlay" id="musicPlayBtn" onclick="musicToggle()">▶</button><button type="button" onclick="musicNext()">⏭</button></div><div class="siteMusicProgress"><div id="musicProgressBar"></div></div><div id="musicStage"></div></div><footer><div class="wrap foot"><div><div class="ft" id="siteName">JasTech Recrutamento & Seleção</div><span id="footerCnpj"></span><br>Conectando talentos às melhores oportunidades.</div><div><div class="ft">Navegação</div><a href="#empresas">Empresas</a><br><a href="#vagas">Vagas</a><br><a href="#candidato">Candidatos</a></div><div><div class="ft">Contato</div><span id="footerLocation">Carandaí/MG e região.</span><br><span id="footerPhone">(31) 99999-9999</span></div></div></footer>

</div>

<script>
const KEY="jastech_unico_v2";
const OLD_KEY="jastech_unico_v1";
const defaults={name:"JasTech Recrutamento & Seleção",cnpj:"",location:"Carandaí/MG e região.",heroTitle:"Conectando talentos às melhores oportunidades.",heroText:"A JasTech aproxima empresas e profissionais e organiza as etapas de recrutamento e seleção.",whatsapp:"5531999999999",primary:"#1769ff",nav:"#071b3a",bg:"#f5f8fc",text:"#10213d",layout:"classic",buttonStyle:"rounded",mediaImage:"",mediaVideo:"",music:[],password:"1234",jobs:[
{id:1,title:"Auxiliar Administrativo",area:"Administrativo",city:"Carandaí/MG",type:"Efetivo",active:true},
{id:2,title:"Vendedor(a)",area:"Vendas",city:"Carandaí/MG",type:"Efetivo",active:true},
{id:3,title:"Auxiliar de Produção",area:"Produção",city:"Região",type:"Efetivo",active:true}],candidates:[],companies:[],stages:["Cadastro recebido","Triagem de currículo","Entrevista JasTech","Finalista / encaminhado para entrevista","Aprovado","Não aprovado"]};
function data(){
  try{
    let raw=localStorage.getItem(KEY);
    if(!raw){ const old=localStorage.getItem(OLD_KEY); if(old){ raw=old; localStorage.setItem(KEY,old); } }
    const saved=JSON.parse(raw||"null");
    if(!saved)return structuredClone(defaults);
    const d={...structuredClone(defaults),...saved};
    d.jobs=Array.isArray(saved.jobs)?saved.jobs:structuredClone(defaults.jobs);
    d.jobs=d.jobs.map(j=>({...j,active:j.active===true||j.active===1||String(j.active).toLowerCase()==="true"}));
    d.candidates=Array.isArray(saved.candidates)?saved.candidates:[];
    d.companies=Array.isArray(saved.companies)?saved.companies:[];
    if(!saved.adminApprovalV2){d.jobs=d.jobs.map(j=>j.companyId&&!j.approvedByAdmin?{...j,active:false,approvedByAdmin:false,processStatus:"Solicitação recebida"}:j);d.adminApprovalV2=true;}
    d.stages=Array.isArray(saved.stages)&&saved.stages.length?saved.stages:structuredClone(defaults.stages);
    return d;
  }catch(e){return structuredClone(defaults)}
}
function save(d){localStorage.setItem(KEY,JSON.stringify(d))}
function applySite(){
let d=data();
siteName.textContent=d.name; heroTitle.textContent=d.heroTitle; heroText.textContent=d.heroText;
location.textContent=d.location; footerLocation.textContent=d.location; footerPhone.textContent=formatPhone(d.whatsapp);
footerCnpj.textContent=d.cnpj?("CNPJ: "+d.cnpj):"";
whats.href="https://wa.me/"+d.whatsapp;
document.documentElement.style.setProperty("--blue",d.primary||"#1769ff");
document.documentElement.style.setProperty("--nav",d.nav||"#071b3a");
document.documentElement.style.setProperty("--bg",d.bg||"#f5f8fc");
document.documentElement.style.setProperty("--text",d.text||"#10213d");
document.body.style.background=d.bg||"#f5f8fc";
document.querySelector(".hero").style.background=`linear-gradient(135deg,${d.nav||"#071b3a"},${d.primary||"#1769ff"})`;
document.querySelectorAll(".btn.primary").forEach(x=>x.style.background=d.primary||"#1769ff");
document.body.classList.remove("layout-center","layout-media");
if(d.layout==="center")document.body.classList.add("layout-center");
if(d.layout==="media")document.body.classList.add("layout-media");
document.body.classList.toggle("pill-buttons",d.buttonStyle==="pill");
document.body.classList.toggle("square-buttons",d.buttonStyle==="square");
renderMedia();
}
function moneyBR(v){return Number(v||0).toLocaleString("pt-BR",{style:"currency",currency:"BRL"})}
function formatPhone(n){n=String(n||"").replace(/\D/g,"");return n.length>=12?"("+n.slice(2,4)+") "+n.slice(4,9)+"-"+n.slice(9):n}
function esc(s){return String(s??"").replace(/[&<>"']/g,m=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"}[m]))}
function renderJobs(){
  const d=data(), activeJobs=Array.isArray(d.jobs)?d.jobs.filter(x=>x.active):[];
  const featured=document.getElementById("availableJobs");
  const availableCount=document.getElementById("availableCount");
  const container=document.getElementById("jobs");
  if(availableCount)availableCount.textContent=`${activeJobs.length} vaga${activeJobs.length===1?"":"s"} aberta${activeJobs.length===1?"":"s"}`;
  if(featured){
    featured.innerHTML=activeJobs.map(x=>{
      const company=d.companies.find(c=>String(c.id)===String(x.companyId));
      const companyName=x.company||x.companyName||company?.company||company?.name||"Empresa contratante não informada";
      const details=[x.city?`<span class="tag">📍 ${esc(x.city)}</span>`:"",x.type?`<span class="tag">💼 ${esc(x.type)}</span>`:"",x.area?`<span class="tag">🏷️ ${esc(x.area)}</span>`:"",x.quantity?`<span class="tag">👥 ${esc(x.quantity)} oportunidade${Number(x.quantity)===1?"":"s"}</span>`:""].join("");
      return `<article class="availableCard" data-job-id="${esc(x.id)}">
        <div class="jobCompany">🏢 ${esc(companyName)}</div>
        <h3>${esc(x.title||x.role||"Vaga")}</h3>
        <div class="jobMeta">${details}</div>
        ${x.salary?`<div class="jobDetails"><b>💰 Salário/benefícios:</b> ${esc(x.salary)}</div>`:""}
        ${x.requirements?`<div class="jobDetails"><b>📋 Requisitos:</b> ${esc(x.requirements)}</div>`:""}
        ${x.description?`<div class="jobDetails"><b>📝 Descrição:</b> ${esc(x.description)}</div>`:""}
        ${x.schedule?`<div class="jobDetails"><b>🕐 Horário:</b> ${esc(x.schedule)}</div>`:""}
        ${x.contractType?`<div class="jobDetails"><b>📄 Contrato:</b> ${esc(x.contractType)}</div>`:""}
        <button type="button" class="btn primary apply-job-btn" data-job-id="${esc(x.id)}">Candidatar-se</button>
      </article>`;
    }).join("") || `<div class="box" style="grid-column:1/-1"><b>Nenhuma vaga publicada no momento.</b><p class="muted">Novas oportunidades aparecerão aqui assim que forem aprovadas pelo administrador.</p></div>`;
    featured.querySelectorAll('.apply-job-btn').forEach(btn=>btn.addEventListener('click',()=>{
      const job=activeJobs.find(j=>String(j.id)===String(btn.dataset.jobId));
      if(job) goToCandidate(job.title);
    }));
  }
  if(!container)return;
  const q=String(document.getElementById("jobSearch")?.value||"").trim().toLowerCase();
  const area=String(document.getElementById("jobAreaFilter")?.value||"").trim().toLowerCase();
  const city=String(document.getElementById("jobCityFilter")?.value||"").trim().toLowerCase();
  const filtered=activeJobs.filter(x=>{
    const hay=[x.title,x.area,x.city,x.type,x.salary,x.requirements].map(v=>String(v||"").toLowerCase()).join(" ");
    return (!q||hay.includes(q))&&(!area||String(x.area||"").toLowerCase()===area)&&(!city||String(x.city||"").toLowerCase().includes(city));
  });
  const count=document.getElementById("jobSearchCount");
  if(count)count.textContent=`${filtered.length} vaga${filtered.length===1?"":"s"} encontrada${filtered.length===1?"":"s"}`;
  container.innerHTML=filtered.map(x=>{
    const details=[x.city?`<span class="tag">📍 ${esc(x.city)}</span>`:"",x.type?`<span class="tag">💼 ${esc(x.type)}</span>`:"",x.area?`<span class="tag">🏷️ ${esc(x.area)}</span>`:"",x.quantity?`<span class="tag">👥 ${esc(x.quantity)} vaga${Number(x.quantity)===1?"":"s"}</span>`:""].join("");
    return `<article class="job"><div class="jobMain"><div class="jobTitle"><strong>${esc(x.title)}</strong></div><div class="jobMeta">${details}</div>${x.salary?`<div class="jobDetails"><b>💰 Salário/benefícios:</b> ${esc(x.salary)}</div>`:""}${x.requirements?`<div class="jobDetails"><b>📋 Requisitos:</b> ${esc(x.requirements)}</div>`:""}<div class="jobDetails"><b>Interessado?</b> Veja os detalhes e candidate-se a esta oportunidade.</div></div><div class="jobActions"><a class="btn primary" href="#candidato" onclick="selectJob(${JSON.stringify(x.title)});return false">Candidatar-se</a><button type="button" class="btn light" onclick="selectJob(${JSON.stringify(x.title)})">Selecionar vaga</button></div></article>`;
  }).join("")||(q||area||city?'<div class="box"><b>Nenhuma vaga encontrada.</b><p class="muted">Tente outro termo, área ou cidade.</p></div>':'<div class="box">Nenhuma vaga publicada no momento.</div>');
  renderJobSelect();
}
function setupJobSearch(){
  const input=document.getElementById("jobSearch"), area=document.getElementById("jobAreaFilter"), city=document.getElementById("jobCityFilter");
  if(input&&!input.dataset.ready){input.dataset.ready="1";input.addEventListener("input",renderJobs)}
  if(city&&!city.dataset.ready){city.dataset.ready="1";city.addEventListener("input",renderJobs)}
  if(area&&!area.dataset.ready){area.dataset.ready="1";area.addEventListener("change",renderJobs)}
  const areas=[...new Set(data().jobs.filter(j=>j.active&&j.area).map(j=>j.area))].sort((a,b)=>String(a).localeCompare(String(b)));
  if(area){const current=area.value;area.innerHTML='<option value="">Todas as áreas</option>'+areas.map(a=>`<option value="${esc(a)}">${esc(a)}</option>`).join("");area.value=current}
}
function renderJobSelect(){
  const d=data(), list=document.getElementById("jobOptions"), field=document.getElementById("candidateJob");
  if(!list)return;
  const activeJobs=Array.isArray(d.jobs)?d.jobs.filter(x=>x.active):[];
  list.innerHTML=activeJobs.map(x=>`<option value="${esc(x.title)}">${esc(x.city||"Sem cidade")} — ${esc(x.area||"Sem área")}</option>`).join("");
  if(field){field.disabled=activeJobs.length===0;field.placeholder=activeJobs.length?"Digite para buscar ou selecione uma vaga":"Nenhuma vaga disponível no momento";}
}
function goToCandidate(t){selectJob(t);setTimeout(()=>document.getElementById("candidateJob")?.focus(),350);}
function selectJob(t){
  const field=document.getElementById("candidateJob");
  if(field){field.value=t;field.dispatchEvent(new Event("input",{bubbles:true}));}
  const role=document.querySelector('[name=role]'); if(role)role.value=t;
  const job=data().jobs.find(j=>String(j.title).trim().toLowerCase()===String(t).trim().toLowerCase()&&j.active);
  document.getElementById("candidato")?.scrollIntoView({behavior:"smooth",block:"start"});
}
function hashSimple(v){let h=0;for(let i=0;i<v.length;i++)h=((h<<5)-h)+v.charCodeAt(i)|0;return String(h)}
function stageIndex(stage){let d=data();return (d.stages||defaults.stages).indexOf(stage)}
function stageText(x){return x||"Cadastro recebido"}
candidateForm.onsubmit=e=>{
  e.preventDefault();
  const d=data(), f=new FormData(candidateForm), o=Object.fromEntries(f.entries());
  const requestedTitle=String(o.jobTitleInput||"").trim();
  const job=d.jobs.find(j=>String(j.title).trim().toLowerCase()===requestedTitle.toLowerCase() && j.active);
  if(!job){candidateMsg.textContent="Selecione ou digite exatamente uma das vagas disponíveis."; return}
  if(d.candidates.some(x=>String(x.email).toLowerCase()===String(o.email).toLowerCase())){candidateMsg.textContent="Este e-mail já possui um acesso de candidato.";return}
  const id=Date.now();
  d.candidates.push({id,name:o.name,phone:o.phone,email:o.email,city:o.city,role:job.title,jobTitle:job.title,jobId:job.id,area:job.area,resume:o.resume?.name||"",experience:o.experience,stage:"Cadastro recebido",feedback:"",createdAt:new Date().toISOString(),passwordHash:hashSimple(o.password)});
  save(d); candidateForm.reset(); candidateMsg.textContent="Cadastro realizado. Use seu e-mail e senha na Área do candidato para acompanhar o processo."; renderJobs();
}
companyForm.onsubmit=e=>{e.preventDefault();let d=data(),f=new FormData(companyForm),o=Object.fromEntries(f.entries());if(o.password!==o.password2){companyMsg.textContent="As senhas não conferem.";return}let existing=d.companies.find(x=>x.email.toLowerCase()===o.email.toLowerCase());if(existing){companyMsg.textContent="Este e-mail já possui um acesso de empresa.";return}let companyId=Date.now(),jobId=companyId+1;let company={id:companyId,company:o.company,contact:o.contact,phone:o.phone,email:o.email,passwordHash:hashSimple(o.password),paid:false,createdAt:new Date().toISOString(),jobs:[jobId]};let job={id:jobId,title:o.role,area:"",city:o.city||"",type:"A definir",active:false,companyId:companyId,quantity:Number(o.quantity)||1,salary:o.salary||"",requirements:o.requirements||"",processStatus:"Solicitação recebida",approvedByAdmin:false};d.companies.push(company);d.jobs.push(job);save(d);companyForm.reset();companyMsg.textContent="Solicitação enviada com sucesso. A vaga ficará aguardando a aprovação do administrador antes de aparecer no site."}
companyLoginForm.onsubmit=async e=>{e.preventDefault();await syncServer();let f=new FormData(companyLoginForm),o=Object.fromEntries(f.entries()),d=data(),c=d.companies.find(x=>x.email.toLowerCase()===o.email.toLowerCase()&&x.passwordHash===hashSimple(o.password));if(!c){companyLoginMsg.textContent="E-mail ou senha incorretos.";return}companyLoginMsg.textContent="";renderCompanyPortal(c)}
candidateLoginForm.onsubmit=async e=>{e.preventDefault();await syncServer();let f=new FormData(candidateLoginForm),o=Object.fromEntries(f.entries()),d=data(),c=d.candidates.find(x=>x.email.toLowerCase()===o.email.toLowerCase()&&x.passwordHash===hashSimple(o.password));if(!c){candidateLoginMsg.textContent="E-mail ou senha incorretos.";return}candidateLoginMsg.textContent="";renderCandidatePortal(c)}
function renderCompanyPortal(c){let d=data(),jobsC=d.jobs.filter(j=>(c.jobs||[]).map(Number).includes(Number(j.id))),html=`<div class="portalHead"><strong>${esc(c.company)}</strong><button class="btn light" onclick="companyPortal.classList.add('hidden')">Fechar</button></div>`;let msgs=Array.isArray(c.messages)?c.messages:[];if(msgs.length){html+=`<div class="portalCard" style="border:2px solid #1769ff"><h3>💳 Mensagens e cobranças</h3>${msgs.map(m=>`<div class="portalCard" style="margin:10px 0;background:#f7fbff"><p><b>${m.type==='cobranca'?'Cobrança da JasTech':'Mensagem'}</b> • ${formatDate(m.createdAt)}</p><p>${esc(m.text)}</p>${m.amount?`<p><b>Valor:</b> ${moneyBR(m.amount)} ${m.due?`• <b>Vencimento:</b> ${formatDate(m.due)}`:''}</p>`:''}<p><b>Formas de pagamento:</b> ${[m.methods?.pix&&'PIX',m.methods?.credit&&'Cartão de crédito',m.methods?.debit&&'Cartão de débito'].filter(Boolean).join(' • ')||'Consulte a JasTech'}</p>${m.methods?.pix&&m.pixInfo?`<p><b>PIX:</b> ${esc(m.pixInfo)}</p>`:''}${(m.methods?.credit||m.methods?.debit)&&m.cardLink?`<p><a class="btn primary" href="${esc(m.cardLink)}" target="_blank" rel="noopener">💳 Pagar com cartão</a></p>`:''}</div>`).join('')}</div>`}jobsC.forEach(j=>{let cand=d.candidates.filter(x=>Number(x.jobId)===Number(j.id)),finalists=cand.filter(x=>x.stage==="Finalista / encaminhado para entrevista"||x.stage==="Aprovado");html+=`<div class="portalCard"><h4>${esc(j.title)}</h4><p class="muted">${esc(j.processStatus||"Em análise")}</p><div class="miniStats"><span><b>${cand.length}</b> inscritos</span><span><b>${finalists.length}</b> finalistas indicados</span><span><b>${cand.filter(x=>x.stage==="Aprovado").length}</b> aprovados</span></div><p><b>Andamento:</b> ${esc(j.processStatus||"Solicitação recebida")}</p>${finalists.length?`<div><b>Finalistas encaminhados:</b><ul>${finalists.map(x=>`<li>${esc(x.name)} — ${esc(x.role)} (${esc(x.stage)})</li>`).join("")}</ul></div>`:'<p class="muted">Ainda não há finalistas indicados.</p>'}</div>`});companyPortal.innerHTML=html;companyPortal.classList.remove('hidden')}
function renderCandidatePortal(c){let html=`<div class="portalHead"><strong>Olá, ${esc(c.name)}</strong><button class="btn light" onclick="candidatePortal.classList.add('hidden')">Fechar</button></div><div class="portalCard"><h4>${esc(c.jobTitle||c.role)}</h4><p class="tag">Etapa atual</p><h3>${esc(stageText(c.stage))}</h3><p>${c.feedback?esc(c.feedback):'Seu processo está em acompanhamento pela JasTech. Novas informações aparecerão aqui quando a etapa for atualizada.'}</p></div>`;candidatePortal.innerHTML=html;candidatePortal.classList.remove('hidden')}
async function syncServer(){try{const r=await fetch("/api/state",{cache:"no-store"});if(!r.ok)return;const remote=await r.json();window.__serverData=remote;applySite();setupJobSearch();renderJobs();}catch(e){console.warn("Servidor indisponível; usando dados locais.",e)}}
function data(){try{return window.__serverData||JSON.parse(localStorage.getItem(KEY)||"null")||structuredClone(defaults)}catch(e){return structuredClone(defaults)}}
function save(d){window.__serverData=d;localStorage.setItem(KEY,JSON.stringify(d));fetch("/api/state",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(d)}).then(r=>r.json()).catch(()=>{});}
syncServer();
setInterval(()=>{if(document.visibilityState==="visible")syncServer()},5000);
window.addEventListener("storage",e=>{if(e.key===KEY||e.key===OLD_KEY){applySite();renderJobs();}});
document.addEventListener("visibilitychange",()=>{if(!document.hidden){applySite();renderJobs();}});
setInterval(()=>{if(!document.hidden)renderJobs();},2000);
let musicState={list:[],index:0,playing:false,audio:null};
function getMusicList(){const d=data();return Array.isArray(d.music)?d.music.filter(m=>m.active!==false):[]}
function renderMusicPlayer(){musicState.list=getMusicList();const box=document.getElementById('siteMusicPlayer');if(!box)return;if(!musicState.list.length){box.classList.add('hidden');return}box.classList.remove('hidden');if(musicState.index>=musicState.list.length)musicState.index=0;const m=musicState.list[musicState.index];document.getElementById('musicNow').textContent=m.title||'Música';document.getElementById('musicType').textContent=m.type==='youtube'?'YouTube':'MP3';document.getElementById('musicPlayBtn').textContent=musicState.playing?'⏸':'▶';const stage=document.getElementById('musicStage');if(musicState.audio){musicState.audio.pause();musicState.audio=null}stage.innerHTML='';if(m.type==='mp3'){const au=document.createElement('audio');au.src=m.src;au.preload='metadata';au.onended=musicNext;au.ontimeupdate=()=>{const p=au.duration?(au.currentTime/au.duration)*100:0;document.getElementById('musicProgressBar').style.width=p+'%'};stage.appendChild(au);musicState.audio=au}else{const iframe=document.createElement('iframe');iframe.src='https://www.youtube.com/embed/'+encodeURIComponent(m.videoId)+'?enablejsapi=1&rel=0';iframe.allow='autoplay; encrypted-media';iframe.title=m.title||'YouTube';stage.appendChild(iframe);document.getElementById('musicProgressBar').style.width='0%'} }
function musicToggle(){const m=musicState.list[musicState.index];if(!m)return;if(m.type==='mp3'&&musicState.audio){if(musicState.playing)musicState.audio.pause();else musicState.audio.play().catch(()=>{});musicState.playing=!musicState.playing;renderMusicControlsOnly()}else{if(m.type==='youtube'){const iframe=document.querySelector('#musicStage iframe');if(iframe){iframe.contentWindow.postMessage(JSON.stringify({event:'command',func:musicState.playing?'pauseVideo':'playVideo',args:[]}), '*');musicState.playing=!musicState.playing;renderMusicControlsOnly()}}}}
function renderMusicControlsOnly(){const b=document.getElementById('musicPlayBtn');if(b)b.textContent=musicState.playing?'⏸':'▶'}
function musicNext(){musicState.playing=false;musicState.index=(musicState.index+1)%musicState.list.length;renderMusicPlayer();musicToggle()}
function musicPrev(){musicState.playing=false;musicState.index=(musicState.index-1+musicState.list.length)%musicState.list.length;renderMusicPlayer()}
function initMusic(){musicState.list=getMusicList();if(musicState.list.length)renderMusicPlayer()}
initMusic();
setInterval(()=>{const l=getMusicList();if(l.length!==musicState.list.length)renderMusicPlayer()},3000);
</script>
</body></html>
JasTech — versão com comandos do Financeiro corrigidos.

Os botões “Ver empresas” e “Ver cobranças” agora usam listeners exclusivos e funcionam por clique, sem onclick duplicado.

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


const KEY="jastech_unico_v2";
const OLD_KEY="jastech_unico_v1";
const defaults={name:"JasTech Recrutamento & Seleção",cnpj:"",location:"Carandaí/MG e região.",heroTitle:"Conectando talentos às melhores oportunidades.",heroText:"A JasTech aproxima empresas e profissionais e organiza as etapas de recrutamento e seleção.",whatsapp:"5531999999999",primary:"#1769ff",nav:"#071b3a",bg:"#f5f8fc",text:"#10213d",layout:"classic",buttonStyle:"rounded",mediaImage:"",mediaVideo:"",music:[],password:"1234",jobs:[{id:1,title:"Auxiliar Administrativo",area:"Administrativo",city:"Carandaí/MG",type:"Efetivo",active:true},{id:2,title:"Vendedor(a)",area:"Vendas",city:"Carandaí/MG",type:"Efetivo",active:true},{id:3,title:"Auxiliar de Produção",area:"Produção",city:"Região",type:"Efetivo",active:true}],candidates:[],companies:[],finance:{transactions:[]},stages:["Cadastro recebido","Triagem de currículo","Entrevista JasTech","Finalista / encaminhado para entrevista","Aprovado","Não aprovado"]};
function data(){
  try{
    if(window.__serverData)return window.__serverData;
    let raw=localStorage.getItem(KEY);
    if(!raw){ const old=localStorage.getItem(OLD_KEY); if(old){ raw=old; localStorage.setItem(KEY,old); } }
    const saved=JSON.parse(raw||"null");
    if(!saved)return structuredClone(defaults);
    const d={...structuredClone(defaults),...saved};
    d.jobs=Array.isArray(saved.jobs)?saved.jobs:structuredClone(defaults.jobs);
    d.jobs=d.jobs.map(j=>({...j,active:j.active===true||j.active===1||String(j.active).toLowerCase()==="true"}));
    d.candidates=Array.isArray(saved.candidates)?saved.candidates:[];
    d.companies=Array.isArray(saved.companies)?saved.companies:[];
    if(!saved.adminApprovalV2){d.jobs=d.jobs.map(j=>j.companyId&&!j.approvedByAdmin?{...j,active:false,approvedByAdmin:false,processStatus:"Solicitação recebida"}:j);d.adminApprovalV2=true;}
    d.stages=Array.isArray(saved.stages)&&saved.stages.length?saved.stages:structuredClone(defaults.stages);
    return d;
  }catch(e){return structuredClone(defaults)}
}
function save(d){window.__serverData=d;localStorage.setItem(KEY,JSON.stringify(d));fetch("/api/state",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(d)}).then(r=>r.json()).catch(()=>{})} 
async function syncServer(){try{const r=await fetch("/api/state",{cache:"no-store"});if(!r.ok)return;const remote=await r.json();if(remote&&Array.isArray(remote.jobs)){window.__serverData=remote;localStorage.setItem(KEY,JSON.stringify(remote));refreshAdmin();}}catch(e){console.warn("Servidor indisponível",e)}}
function esc(s){return String(s??"").replace(/[&<>"']/g,m=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"}[m]))}
function doLogin(){
  const user=document.getElementById("loginUser");
  const pass=document.getElementById("loginPass");
  const msg=document.getElementById("loginMsg");
  const d=data();
  const expected=String(d.password||"1234");
  if(String(user.value||"").trim().toLowerCase()==="admin" && String(pass.value||"")===expected){
    sessionStorage.setItem("jasLogin","1");
    msg.textContent="";
    enterDash();
  }else{
    msg.textContent="Usuário ou senha incorretos. Use admin / 1234 na primeira entrada.";
  }
}
function enterDash(){
  document.getElementById("adminLogin").classList.add("hidden");
  document.getElementById("dashboard").classList.remove("hidden");
  loadEditor();refreshAdmin();syncServer();
  const el=document.getElementById("finDate");
  if(el&&!el.value)el.value=new Date().toISOString().slice(0,10);
}
function logout(){sessionStorage.removeItem("jasLogin");document.getElementById("adminLogin").classList.remove("hidden");document.getElementById("dashboard").classList.add("hidden")}
function showTab(id){["siteTab","designTab","jobsTab","processTab","candTab","compTab","financeTab","musicTab"].forEach(x=>document.getElementById(x).classList.toggle("hidden",x!==id))}
function loadEditor(){let d=data();editName.value=d.name;editCnpj.value=d.cnpj||"";editLocation.value=d.location;editHeroTitle.value=d.heroTitle;editHeroText.value=d.heroText;editWhats.value=d.whatsapp;colorPrimary.value=d.primary||"#1769ff";colorNav.value=d.nav||"#071b3a";colorBg.value=d.bg||"#f5f8fc";colorText.value=d.text||"#10213d";layoutChoice.value=d.layout||"classic";buttonStyle.value=d.buttonStyle||"rounded";renderMediaPreview()}
function saveSite(){let d=data();d.name=editName.value||d.name;d.cnpj=editCnpj.value||"";d.location=editLocation.value||d.location;d.heroTitle=editHeroTitle.value||d.heroTitle;d.heroText=editHeroText.value||d.heroText;d.whatsapp=editWhats.value.replace(/\D/g,"")||d.whatsapp;save(d);siteMsg.textContent="Informações salvas. Atualize o site público para visualizar.";}
function resetSite(){let d=data();Object.assign(d,{name:defaults.name,cnpj:defaults.cnpj,location:defaults.location,heroTitle:defaults.heroTitle,heroText:defaults.heroText,whatsapp:defaults.whatsapp});save(d);loadEditor();siteMsg.textContent="Informações restauradas."}
function addJob(){let d=data();if(!jobTitle.value.trim())return;d.jobs.push({id:Date.now(),title:jobTitle.value,area:jobArea.value,city:jobCity.value,type:jobType.value||"Efetivo",active:false,approvedByAdmin:false,processStatus:"Rascunho administrativo"});save(d);jobTitle.value=jobArea.value=jobCity.value=jobType.value="";refreshAdmin()}
function deleteJob(id){let d=data();d.jobs=d.jobs.filter(x=>x.id!==id);save(d);refreshAdmin()}
function toggleJob(id){let d=data(),x=d.jobs.find(x=>Number(x.id)===Number(id));if(!x)return;x.active=!Boolean(x.active);x.approvedByAdmin=x.active===true;x.processStatus=x.active?"Publicado pelo administrador":"Pausada pelo administrador";save(d);refreshAdmin();}
function fileToData(file){return new Promise((res,rej)=>{let r=new FileReader();r.onload=()=>res(r.result);r.onerror=rej;r.readAsDataURL(file)})}
function saveDesign(){let d=data();d.primary=colorPrimary.value;d.nav=colorNav.value;d.bg=colorBg.value;d.text=colorText.value;d.layout=layoutChoice.value;d.buttonStyle=buttonStyle.value;let jobs=[];let img=mediaImage.files[0],vid=mediaVideo.files[0];if(img)jobs.push(fileToData(img).then(x=>d.mediaImage=x));if(vid)jobs.push(fileToData(vid).then(x=>d.mediaVideo=x));Promise.all(jobs).then(()=>{save(d);renderMediaPreview();designMsg.textContent="Aparência e mídia salvas."})}
function renderMediaPreview(){let d=data(),box=document.getElementById("mediaPreview"),out="";if(d.mediaImage)out+=`<img src="${d.mediaImage}" alt="Imagem">`;if(d.mediaVideo)out+=`<video src="${d.mediaVideo}" controls></video>`;box.innerHTML=out||"<span class='muted'>Nenhuma mídia cadastrada.</span>"}
function resetDesign(){let d=data();d.primary=defaults.primary;d.nav=defaults.nav;d.bg=defaults.bg;d.text=defaults.text;d.layout=defaults.layout;d.buttonStyle=defaults.buttonStyle;d.mediaImage="";d.mediaVideo="";save(d);loadEditor();designMsg.textContent="Aparência restaurada."}
function setCandidateStage(id){let d=data(),x=d.candidates.find(x=>x.id==id);if(!x)return;x.stage=document.getElementById('stage_'+id).value;x.feedback=document.getElementById('feedback_'+id).value;save(d);refreshAdmin()}
function setJobStatus(id){let d=data(),x=d.jobs.find(x=>x.id==id);if(!x)return;x.processStatus=document.getElementById('jobstatus_'+id).value;save(d);refreshAdmin()}
function publishCompanyJob(id){let d=data(),x=d.jobs.find(j=>Number(j.id)===Number(id));if(!x)return;x.active=true;x.approvedByAdmin=true;x.processStatus="Publicado pelo administrador";save(d);refreshAdmin()}
function setJobStatus(id){let d=data(),x=d.jobs.find(x=>x.id==id);if(!x)return;x.processStatus=document.getElementById('jobstatus_'+id).value;save(d);refreshAdmin()}
function refreshAdmin(){
let d=data();
statJobs.textContent=d.jobs.length;statCandidates.textContent=d.candidates.length;statCompanies.textContent=d.companies.length;statProcesses.textContent=d.candidates.length;
adminJobs.innerHTML=d.jobs.map(x=>{
 let c=x.companyId?d.companies.find(c=>Number(c.id)===Number(x.companyId)):null;
 let action=c&&!x.active?`<button class="btn primary" onclick="publishCompanyJob(${x.id})">🚀 Aprovar e publicar</button>`:`<button class="btn light" onclick="toggleJob(${x.id})">${x.active?"Pausar":"Ativar"}</button>`;
 return `<div class="box" style="margin:10px 0"><b>${esc(x.title)}</b> — ${esc(x.city)} — ${x.active?"Ativa":"Pausada"} ${c?`<span class="tag">🏢 ${esc(c.company)}</span>`:`<span class="tag">JasTech</span>`}<br>${c?`<small>Vaga vinculada ao cadastro da empresa • ${esc(c.email)}</small><br>`:""}<select id="jobstatus_${x.id}" style="max-width:420px"><option ${x.processStatus==="Solicitação recebida"?"selected":""}>Solicitação recebida</option><option ${x.processStatus==="Publicado automaticamente"?"selected":""}>Publicado automaticamente</option><option ${x.processStatus==="Em recrutamento"?"selected":""}>Em recrutamento</option><option ${x.processStatus==="Triagem em andamento"?"selected":""}>Triagem em andamento</option><option ${x.processStatus==="Finalistas encaminhados"?"selected":""}>Finalistas encaminhados</option><option ${x.processStatus==="Encerrado"?"selected":""}>Encerrado</option></select> <button class="btn light" onclick="setJobStatus(${x.id})">Salvar andamento</button> ${action} <button class="btn danger" onclick="deleteJob(${x.id})">Excluir</button></div>`;
}).join("");
adminCandidates.innerHTML=d.candidates.length?d.candidates.map(x=>{let opts=(d.stages||defaults.stages).map(st=>`<option ${x.stage===st?"selected":""}>${esc(st)}</option>`).join("");return `<div class="box" style="margin:12px 0"><button class="btn light" onclick="openCandidate(${x.id})"><b>${esc(x.name)}</b></button> — ${esc(x.jobTitle||x.role)}<br><small>${esc(x.email||"")} • ${esc(x.phone||"")} • ${esc(x.city||"")} • Cadastrado: ${formatDate(x.createdAt)}</small><div class="row" style="margin-top:10px"><label>Etapa atual<select id="stage_${x.id}">${opts}</select></label><label>Feedback para o candidato<textarea id="feedback_${x.id}">${esc(x.feedback||"")}</textarea></label></div><button class="btn primary" onclick="setCandidateStage(${x.id})">Salvar etapa e feedback</button></div>`}).join(""):"<p class='muted'>Nenhum candidato.</p>";
adminProcesses.innerHTML=d.candidates.length?d.candidates.map(x=>`<div class="box" style="margin:10px 0;display:flex;justify-content:space-between;gap:12px;align-items:center"><div><button class="btn light" onclick="openCandidate(${x.id})"><b>${esc(x.name)}</b></button><br><small>${esc(x.jobTitle||x.role||"Vaga não informada")} • ${esc(x.stage||"Cadastro recebido")} • ${formatDate(x.createdAt)}</small></div><span class="tag">${esc(x.stage||"Cadastro recebido")}</span></div>`).join(""):"<p class='muted'>Nenhum processo.</p>";
refreshFinance();
adminCompanies.innerHTML=d.companies.length?d.companies.map(c=>{let js=d.jobs.filter(j=>Number(j.companyId)===Number(c.id)||((c.jobs||[]).map(Number).includes(Number(j.id))));return `<div class="box" style="margin:12px 0"><b>🏢 ${esc(c.company)}</b> <span class="tag">${c.paid===true?"✅ Pago":"⚠️ Não pago"}</span><br><small>${esc(c.email)} • ${esc(c.contact)} • ${esc(c.phone)}</small><div style="margin-top:8px">${c.paid===true?"<span class='tag'>Pagamento confirmado</span>":`<button class="btn danger" onclick="deleteUnpaidCompany(${c.id})">🗑️ Excluir empresa não paga</button>`}</div>${js.length?js.map(j=>{let cand=d.candidates.filter(x=>Number(x.jobId)===Number(j.id));let fin=cand.filter(x=>x.stage==="Finalista / encaminhado para entrevista"||x.stage==="Aprovado");let publish=j.active?`<span class="tag">✅ Publicada pelo administrador</span>`:`<button class="btn primary" onclick="publishCompanyJob(${j.id})">🚀 Publicar esta vaga</button>`;return `<div class="box" style="margin-top:10px;cursor:pointer" onclick="this.classList.toggle('expanded')"><b>💼 ${esc(j.title)}</b><p>Status: <strong>${j.active?"Publicada":"Aguardando aprovação"}</strong> • Inscritos: <strong>${cand.length}</strong> • Finalistas: <strong>${fin.length}</strong> • Aprovados: <strong>${cand.filter(x=>x.stage==="Aprovado").length}</strong></p><p class="muted">Clique para ver os dados completos da solicitação.</p><div style="padding:10px 0"><p><b>Cidade:</b> ${esc(j.city||"Não informada")} &nbsp; <b>Tipo:</b> ${esc(j.type||"Não informado")} &nbsp; <b>Quantidade:</b> ${esc(j.quantity||1)}</p><p><b>Salário/benefícios:</b> ${esc(j.salary||"Não informado")}</p><p><b>Requisitos:</b> ${esc(j.requirements||"Não informado")}</p><p><b>Status:</b> ${esc(j.processStatus||"Solicitação recebida")}</p>${publish}</div></div>`}).join(""):`<p class="muted">Nenhuma vaga vinculada.</p>`}</div>`}).join(""):"<p class='muted'>Nenhuma empresa.</p>";
}
function formatDate(v){if(!v)return "Data não informada";try{return new Date(v).toLocaleString("pt-BR")}catch(e){return String(v)}}
function openCandidate(id){let d=data(),x=d.candidates.find(c=>Number(c.id)===Number(id));if(!x)return;let j=d.jobs.find(j=>Number(j.id)===Number(x.jobId));let c=j&&j.companyId?d.companies.find(c=>Number(c.id)===Number(j.companyId)):null;document.getElementById("candidateModalTitle").textContent=x.name||"Candidato";document.getElementById("candidateModalBody").innerHTML=`<div class="box"><p><b>Nome:</b> ${esc(x.name||"Não informado")}</p><p><b>E-mail:</b> ${esc(x.email||"Não informado")}</p><p><b>WhatsApp:</b> ${esc(x.phone||"Não informado")}</p><p><b>Cidade:</b> ${esc(x.city||"Não informado")}</p><p><b>Cargo pretendido:</b> ${esc(x.role||"Não informado")}</p><p><b>Área:</b> ${esc(x.area||"Não informada")}</p><p><b>Vaga:</b> ${esc(x.jobTitle||x.role||"Não informada")}</p><p><b>Empresa contratante:</b> ${esc(c?.company||"Não informada")}</p><p><b>Fase:</b> ${esc(x.stage||"Cadastro recebido")}</p><p><b>Data do cadastro:</b> ${formatDate(x.createdAt)}</p><p><b>Experiência:</b><br>${esc(x.experience||"Não informada")}</p><p><b>Currículo:</b> ${esc(x.resume||"Não enviado")}</p><p><b>Feedback:</b><br>${esc(x.feedback||"Nenhum feedback registrado")}</p></div>`;document.getElementById("candidateModal").style.display="flex"}
function closeCandidate(){document.getElementById("candidateModal").style.display="none"}
function deleteUnpaidCompany(id){let d=data(),c=d.companies.find(c=>Number(c.id)===Number(id));if(!c||c.paid===true){alert("Esta empresa está marcada como paga e não pode ser excluída por esta opção.");return}if(!confirm(`Excluir a empresa ${c.company||""} e suas vagas?`))return;d.companies=d.companies.filter(c=>Number(c.id)!==Number(id));d.jobs=d.jobs.filter(j=>Number(j.companyId)!==Number(id));save(d);refreshAdmin()}

function moneyBR(v){return Number(v||0).toLocaleString("pt-BR",{style:"currency",currency:"BRL"})}
function financeData(d){if(!d.finance||typeof d.finance!=="object")d.finance={transactions:[]};if(!Array.isArray(d.finance.transactions))d.finance.transactions=[];return d.finance}
function addFinanceTransaction(){
 let d=data(),f=financeData(d),type=document.getElementById("finType").value,amount=parseFloat(document.getElementById("finAmount").value),desc=document.getElementById("finDesc").value.trim(),date=document.getElementById("finDate").value;
 if(!(amount>0)||!desc){financeMsg.textContent="Informe valor e descrição.";return}
 let category=document.getElementById("finCategory").value; f.transactions.unshift({id:Date.now(),type,category,amount,description:desc,date:date||new Date().toISOString().slice(0,10),createdAt:new Date().toISOString()});
 save(d);document.getElementById("finAmount").value="";document.getElementById("finDesc").value="";financeMsg.textContent="Movimentação lançada no caixa.";refreshFinance();
}
function deleteFinanceTransaction(id){let d=data(),f=financeData(d);f.transactions=f.transactions.filter(x=>Number(x.id)!==Number(id));save(d);refreshFinance()}
function setCompanyPaid(id,paid){
 let d=data(),c=d.companies.find(x=>Number(x.id)===Number(id));if(!c)return;
 c.paid=!!paid;c.paidAt=paid?new Date().toISOString():null;
 save(d);refreshAdmin();refreshFinance();
}
function saveCompanyMessage(c,text,type){
 if(!c)return false;
 text=(text||"").trim();
 if(!text)return false;
 if(!Array.isArray(c.messages))c.messages=[];
 c.messages.unshift({id:Date.now()+Math.floor(Math.random()*1000),type:type||"mensagem",text,createdAt:new Date().toISOString(),read:false});
 return true;
}
function defaultPendingMessage(c){return `Olá, ${c.company||""}! Tudo bem? Identificamos que há um pagamento pendente junto à JasTech. Pedimos, por gentileza, que verifique sua cobrança e, se possível, regularize o pagamento. Caso já tenha realizado o pagamento, por favor desconsidere esta mensagem. Agradecemos a atenção e permanecemos à disposição. — Equipe JasTech`}
function defaultPaidMessage(c){return `Olá, ${c.company||""}! A JasTech agradece pelo pagamento realizado. Ficamos muito felizes em contar com sua parceria e confiança. Muito obrigado! Permanecemos à disposição sempre que precisar. — Equipe JasTech`}
function sendCompanyCharge(id){let d=data(),c=d.companies.find(x=>Number(x.id)===Number(id));if(!c)return;let amount=parseFloat(document.getElementById("chargeAmount_"+id).value)||0,due=document.getElementById("chargeDue_"+id).value,msg=document.getElementById("chargeMsg_"+id).value.trim();let methods={pix:document.getElementById("payPix_"+id).checked,credit:document.getElementById("payCredit_"+id).checked,debit:document.getElementById("payDebit_"+id).checked};if(!msg)msg="Olá! Identificamos um pagamento pendente junto à JasTech. Por favor, verifique sua cobrança. Caso já tenha pago, desconsidere esta mensagem. Obrigado!";if(!methods.pix&&!methods.credit&&!methods.debit){alert("Selecione pelo menos uma forma de pagamento.");return}c.paymentAmount=amount;c.paymentDue=due;c.pixInfo=document.getElementById("pixInfo_"+id).value.trim();c.cardLink=document.getElementById("cardLink_"+id).value.trim();c.paymentMethods=methods;if(!Array.isArray(c.messages))c.messages=[];c.messages.unshift({id:Date.now(),type:"cobranca",text:msg,amount,due,methods,pixInfo:c.pixInfo,cardLink:c.cardLink,createdAt:new Date().toISOString(),read:false});save(d);alert("Cobrança enviada para o perfil de "+(c.company||"empresa")+".");refreshFinance()}
function sendAutomaticCompanyMessage(id,type){let d=data(),c=d.companies.find(x=>Number(x.id)===Number(id));if(!c)return;let text=(type==="pago"?defaultPaidMessage(c):defaultPendingMessage(c));let field=document.getElementById("autoMsg_"+type+"_"+id);if(field&&field.value.trim())text=field.value.trim();if(!saveCompanyMessage(c,text,type==="pago"?"agradecimento":"cobranca"))return;save(d);alert("Mensagem enviada somente para "+(c.company||"esta empresa")+".");refreshFinance()}
function sendAutomaticToAll(status){let d=data(),companies=(d.companies||[]).filter(c=>status==="pago"?c.paid===true:c.paid!==true);if(!companies.length){alert(status==="pago"?"Nenhuma empresa paga cadastrada.":"Nenhuma empresa pendente cadastrada.");return}let field=document.getElementById("bulkMsg_"+status),template=field&&field.value.trim();if(!template)template=status==="pago"?"Olá! A JasTech agradece pelo pagamento realizado. Muito obrigado pela parceria e confiança. Permanecemos à disposição. — Equipe JasTech":"Olá! Identificamos um pagamento pendente junto à JasTech. Pedimos, por gentileza, que verifique sua cobrança e regularize o pagamento quando possível. Caso já tenha pago, desconsidere esta mensagem. Agradecemos a atenção. — Equipe JasTech";companies.forEach(c=>saveCompanyMessage(c,template.replace(/\{empresa\}/gi,c.company||""),status==="pago"?"agradecimento":"cobranca"));save(d);alert(`Mensagem enviada individualmente para ${companies.length} empresa(s) ${status==="pago"?"paga(s)":"pendente(s)"}.`);refreshFinance()}
function openIndividualMessageForCompany(id){
 openIndividualMessagePicker();
 const sel=document.getElementById("individualCompanySelect"); if(sel){sel.value=String(id);loadIndividualMessageTemplate();}
}
function openIndividualMessagePicker(){
 const d=data(), list=(d.companies||[]);
 const modal=document.getElementById("individualMessageModal"), sel=document.getElementById("individualCompanySelect");
 if(!modal||!sel){alert("Área de mensagem individual não encontrada.");return}
 sel.innerHTML=list.length?list.map(c=>`<option value="${c.id}">${esc(c.company||"Empresa")} — ${c.paid===true?"PAGA":"PENDENTE"} — ${moneyBR(c.paymentAmount||0)}</option>`).join(""):`<option value="">Nenhuma empresa cadastrada</option>`;
 modal.style.display="block"; loadIndividualMessageTemplate();
}
function closeIndividualMessagePicker(){const m=document.getElementById("individualMessageModal");if(m)m.style.display="none"}
function loadIndividualMessageTemplate(){
 const d=data(), id=document.getElementById("individualCompanySelect")?.value, c=(d.companies||[]).find(x=>String(x.id)===String(id)), field=document.getElementById("individualMessageText");
 if(!c||!field)return; field.value=c.paid===true?defaultPaidMessage(c):defaultPendingMessage(c);
}
function sendSelectedIndividualMessage(){
 const d=data(), id=document.getElementById("individualCompanySelect")?.value, c=(d.companies||[]).find(x=>String(x.id)===String(id)), field=document.getElementById("individualMessageText");
 if(!c){alert("Selecione uma empresa.");return}
 const text=(field?.value||"").trim(); if(!text){alert("Digite uma mensagem.");return}
 const type=c.paid===true?"agradecimento":"cobranca";
 if(!saveCompanyMessage(c,text,type)){alert("Não foi possível salvar a mensagem.");return}
 save(d); const st=document.getElementById("individualMessageStatus"); if(st)st.textContent="Mensagem enviada somente para "+(c.company||"esta empresa")+"."; alert("Mensagem enviada somente para "+(c.company||"esta empresa")+"."); refreshFinance();
}
function editCompanyMessage(id,status){let d=data(),c=d.companies.find(x=>Number(x.id)===Number(id));if(!c)return;let text=prompt("Digite a mensagem que deseja enviar para "+(c.company||"empresa")+":",status==="pago"?defaultPaidMessage(c):defaultPendingMessage(c));if(text===null)return;if(!text.trim()){alert("Digite uma mensagem.");return}saveCompanyMessage(c,text,status==="pago"?"agradecimento":"cobranca");save(d);alert("Mensagem enviada individualmente.");refreshFinance()}

function toggleFinancePanel(id,btn){const el=document.getElementById(id);if(!el)return false;const willOpen=!el.classList.contains('open');el.classList.toggle('open',willOpen);if(btn){btn.textContent=willOpen?(id==='companiesFinanceBody'?'Ocultar empresas ▴':'Ocultar cobranças ▴'):(id==='companiesFinanceBody'?'Ver empresas ▾':'Ver cobranças ▾');}return willOpen;}
function toggleFinanceBox(id){return toggleFinancePanel(id,null)}
function openFinanceBox(id,btn){return toggleFinancePanel(id,btn)}
function refreshFinance(){
 let d=data(),f=financeData(d),ins=f.transactions.filter(x=>x.type==="entrada").reduce((a,x)=>a+Number(x.amount||0),0),outs=f.transactions.filter(x=>x.type==="saida").reduce((a,x)=>a+Number(x.amount||0),0);
 let paidCompanies=(d.companies||[]).filter(c=>c.paid===true),pending=(d.companies||[]).filter(c=>c.paid!==true);
 let companyRevenue=paidCompanies.reduce((a,c)=>a+Number(c.paymentAmount||0),0),pendingTotal=pending.reduce((a,c)=>a+Number(c.paymentAmount||0),0);
 document.getElementById("finIn").textContent=moneyBR(ins+companyRevenue);document.getElementById("finPaid").textContent=paidCompanies.length+" empresas";document.getElementById("finPaidTotal").textContent=moneyBR(companyRevenue)+" pago";document.getElementById("finOut").textContent=moneyBR(outs);document.getElementById("finBalance").textContent=moneyBR(ins+companyRevenue-outs);document.getElementById("finPending").textContent=pending.length;document.getElementById("finPendingTotal").textContent=moneyBR(pendingTotal)+" pendente";
 let fc=document.getElementById("financeCompanies"),pendingRows=pending.map(c=>`<tr><td><b>${esc(c.company||"Empresa")}</b></td><td>${esc(c.email||"")}</td><td>${esc(c.contact||"")}</td><td>${c.paymentDue?formatDate(c.paymentDue):"—"}</td><td><b>${moneyBR(c.paymentAmount||0)}</b></td><td><button class="btn primary" onclick="sendAutomaticCompanyMessage(${c.id},'pendente')">📨 Enviar mensagem automática</button><button class="btn light" onclick="editCompanyMessage(${c.id},'pendente')">✏️ Personalizar mensagem</button></td></tr>`).join("");
 let paidRows=paidCompanies.map(c=>`<tr><td><b>${esc(c.company||"Empresa")}</b></td><td>${esc(c.email||"")}</td><td>${esc(c.contact||"")}</td><td>${c.paidAt?formatDate(c.paidAt):"—"}</td><td><b>${moneyBR(c.paymentAmount||0)}</b></td><td><button class="btn primary" onclick="sendAutomaticCompanyMessage(${c.id},'pago')">🙏 Enviar agradecimento automático</button><button class="btn light" onclick="editCompanyMessage(${c.id},'pago')">✏️ Personalizar mensagem</button></td></tr>`).join("");
 let pendingSummary=document.getElementById("pendingSummaryFinance");
 if(pendingSummary) pendingSummary.innerHTML=`<div><span class="mini">Empresas pendentes</span><strong>${pending.length}</strong></div><div><span class="mini">Valor pendente</span><strong>${moneyBR(pendingTotal)}</strong></div><div><span class="mini">Empresas pagas</span><strong>${paidCompanies.length}</strong></div><div><span class="mini">Valor pago</span><strong>${moneyBR(companyRevenue)}</strong></div><div style="grid-column:1/-1;overflow:auto"><h4 style="margin:10px 0">⚠️ Empresas pendentes</h4>${pending.length?`<table class="pendingTable"><thead><tr><th>Empresa</th><th>E-mail</th><th>Contato</th><th>Vencimento</th><th>Valor pendente</th><th>Mensagem</th></tr></thead><tbody>${pendingRows}</tbody></table>`:`<p class="muted">Nenhuma empresa pendente.</p>`}<h4 style="margin:18px 0 10px">✅ Empresas pagas</h4>${paidCompanies.length?`<table class="pendingTable"><thead><tr><th>Empresa</th><th>E-mail</th><th>Contato</th><th>Pagamento</th><th>Valor pago</th><th>Mensagem</th></tr></thead><tbody>${paidRows}</tbody></table>`:`<p class="muted">Nenhuma empresa paga.</p>`}</div>`;
 let bulk=document.getElementById("financeBulkMessages");
 if(bulk) bulk.innerHTML=`<div class="bulkMsgBox"><h3 style="margin-top:0">📨 Mensagens automáticas individuais</h3><p class="mini">As mensagens são enviadas separadamente e ficam no perfil individual de cada empresa. Você pode enviar para todas de um grupo ou escolher uma por uma.</p><div class="row"><label style="flex:1"><b>Mensagem para todas as PENDENTES</b><textarea id="bulkMsg_pendente">Olá! Identificamos um pagamento pendente junto à JasTech. Pedimos, por gentileza, que verifique sua cobrança e regularize o pagamento quando possível. Caso já tenha pago, desconsidere esta mensagem. Agradecemos a atenção. — Equipe JasTech</textarea><button class="btn primary" onclick="sendAutomaticToAll('pendente')">📨 Enviar para TODAS as pendentes</button></label><label style="flex:1"><b>Mensagem para todas as PAGAS</b><textarea id="bulkMsg_pago">Olá! A JasTech agradece pelo pagamento realizado. Muito obrigado pela parceria e confiança. Permanecemos à disposição. — Equipe JasTech</textarea><button class="btn primary" onclick="sendAutomaticToAll('pago')">🙏 Enviar para TODAS as pagas</button></label></div></div>`;
 fc.innerHTML=(d.companies||[]).length?d.companies.map(c=>`<div class="box" style="margin:9px 0"><div class="companyRow"><div class="companyData"><b>🏢 ${esc(c.company||"Empresa")}</b><br><span class="mini">${esc(c.email||"")} • ${esc(c.contact||"")}</span>${c.paymentAmount?`<br><span class="mini">Valor: <b>${moneyBR(c.paymentAmount)}</b></span>`:""}<br><span class="${c.paid===true?'statusPaid':'statusPending'}">${c.paid===true?'✅ PAGO':'⚠️ PENDENTE'}</span></div><div class="companyMsgActions">${c.paid===true?`<button class="btn light" onclick="setCompanyPaid(${c.id},false)">Marcar pendente</button><button class="btn primary" onclick="sendAutomaticCompanyMessage(${c.id},'pago')">🙏 Agradecimento automático</button><button class="btn light" onclick="editCompanyMessage(${c.id},'pago')">✏️ Personalizar</button>`:`<button class="btn primary" onclick="setCompanyPaid(${c.id},true)">Confirmar pagamento</button><button class="btn primary" onclick="sendAutomaticCompanyMessage(${c.id},'pendente')">📨 Mensagem automática</button><button class="btn light" onclick="editCompanyMessage(${c.id},'pendente')">✏️ Personalizar</button>`}</div></div><div class="companyDetail"><details><summary>Ver todos os dados e cobrança</summary><div class="payBox"><p><b>Empresa:</b> ${esc(c.company||"")}<br><b>E-mail:</b> ${esc(c.email||"")}<br><b>Contato:</b> ${esc(c.contact||"")}<br><b>Status:</b> ${c.paid===true?'Pago':'Pendente'}<br><b>Valor:</b> ${moneyBR(c.paymentAmount||0)}<br><b>Vencimento:</b> ${c.paymentDue?formatDate(c.paymentDue):'—'}${c.paidAt?`<br><b>Pago em:</b> ${formatDate(c.paidAt)}`:''}</p><label>Valor da cobrança (R$)<input id="chargeAmount_${c.id}" type="number" min="0" step="0.01" value="${Number(c.paymentAmount||0)||''}"></label><label>Vencimento<input id="chargeDue_${c.id}" type="date" value="${c.paymentDue||''}"></label><label>Mensagem de cobrança<textarea id="chargeMsg_${c.id}" placeholder="Digite a cobrança..."></textarea></label><div class="row"><label><input id="payPix_${c.id}" type="checkbox" ${c.paymentMethods?.pix!==false?'checked':''}> PIX</label><label><input id="payCredit_${c.id}" type="checkbox" ${c.paymentMethods?.credit!==false?'checked':''}> Crédito</label><label><input id="payDebit_${c.id}" type="checkbox" ${c.paymentMethods?.debit!==false?'checked':''}> Débito</label></div><div class="row"><label>Chave PIX / instruções<input id="pixInfo_${c.id}" value="${esc(c.pixInfo||'')}"></label><label>Link cartão<input id="cardLink_${c.id}" value="${esc(c.cardLink||'')}"></label></div><button class="btn primary" onclick="sendCompanyCharge(${c.id})">📨 Enviar cobrança no login</button></div></details></div></div>`).join(""):"<p class='muted'>Nenhuma empresa cadastrada.</p>";
 let rows=f.transactions.map(x=>`<tr><td>${formatDate(x.date)}</td><td>${x.type==="entrada"?'<span class="moneyIn">Entrada</span>':'<span class="moneyOut">Saída</span>'}</td><td><span class="expenseBadge">${esc(x.category||"Outros")}</span></td><td>${esc(x.description)}</td><td>${moneyBR(x.amount)}</td><td><button class="btn danger" onclick="deleteFinanceTransaction(${x.id})">Excluir</button></td></tr>`).join("");
 document.getElementById("financeTransactions").innerHTML=f.transactions.length?`<div style="overflow:auto"><table class="financeTable"><thead><tr><th>Data</th><th>Tipo</th><th>Categoria</th><th>Descrição</th><th>Valor</th><th>Ação</th></tr></thead><tbody>${rows}</tbody></table></div>`:"<p class='muted'>Nenhuma movimentação lançada.</p>";
 let fm=document.getElementById("financeMessages"),msgs=[];(d.companies||[]).forEach(c=>(c.messages||[]).forEach(m=>msgs.push({...m,company:c.company,email:c.email,paid:c.paid===true})));msgs.sort((a,b)=>String(b.createdAt).localeCompare(String(a.createdAt)));fm.innerHTML=msgs.length?msgs.map(m=>`<div class="messageCard"><b>🏢 ${esc(m.company)}</b> <span class="mini">${m.paid?'✅ Paga':'⚠️ Pendente'} • ${esc(m.email||"")} • ${formatDate(m.createdAt)}</span><p>${esc(m.text)}</p><p class="mini">${m.amount?`Valor: <b>${moneyBR(m.amount)}</b> • `:""}${m.due?`Vencimento: ${formatDate(m.due)} • `:""}Tipo: ${m.type||'mensagem'}</p></div>`).join(""):"<p class='muted'>Nenhuma mensagem enviada.</p>";
}

async function syncAdminServer(){try{const r=await fetch("/api/state",{cache:"no-store"});if(!r.ok)return;const remote=await r.json();window.__serverData=remote;localStorage.setItem(KEY,JSON.stringify(remote));if(sessionStorage.jasLogin==="1"){loadEditor();refreshAdmin();}}catch(e){console.warn(e)}}
function data(){try{return window.__serverData||JSON.parse(localStorage.getItem(KEY)||"null")||structuredClone(defaults)}catch(e){return structuredClone(defaults)}}
function save(d){window.__serverData=d;localStorage.setItem(KEY,JSON.stringify(d));fetch("/api/state",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(d)}).then(r=>r.json()).catch(()=>{});}
syncAdminServer();
if(sessionStorage.jasLogin==="1") enterDash();
window.addEventListener("storage",e=>{if(e.key===KEY||e.key===OLD_KEY){if(sessionStorage.jasLogin==="1")refreshAdmin();}});

document.addEventListener("DOMContentLoaded",()=>{
  const p=document.getElementById("loginPass");
  if(p) p.addEventListener("keydown",e=>{if(e.key==="Enter")doLogin()});
  if(sessionStorage.getItem("jasLogin")==="1") enterDash();
});
function ensureMusic(d){if(!Array.isArray(d.music))d.music=[];return d}
function ytId(url){try{const u=new URL(url);if(u.hostname.includes('youtu.be'))return u.pathname.slice(1).split('/')[0];if(u.hostname.includes('youtube.com')){if(u.pathname==='/watch')return u.searchParams.get('v');if(u.pathname.startsWith('/shorts/'))return u.pathname.split('/')[2];if(u.pathname.startsWith('/embed/'))return u.pathname.split('/')[2]}}catch(e){}return ''}
function searchYouTube(){const q=(document.getElementById('ytSearch')?.value||'').trim();if(!q){document.getElementById('musicMsg').textContent='Digite o nome da música ou artista para pesquisar.';return}window.open('https://www.youtube.com/results?search_query='+encodeURIComponent(q),'_blank','noopener');}
function addYouTubeMusic(){let d=ensureMusic(data()), url=(document.getElementById('ytUrl')?.value||'').trim(), id=ytId(url), title=(document.getElementById('ytTitle')?.value||'').trim();if(!id){document.getElementById('musicMsg').textContent='Cole um link válido do YouTube.';return}if(!title)title='Música do YouTube';d.music.push({id:Date.now(),type:'youtube',videoId:id,title,url,active:true,createdAt:new Date().toISOString()});save(d);document.getElementById('ytUrl').value='';document.getElementById('ytTitle').value='';document.getElementById('musicMsg').textContent='Música do YouTube adicionada à playlist.';renderAdminMusic();}
function addMP3Music(){const file=document.getElementById('mp3File')?.files?.[0], title=(document.getElementById('mp3Title')?.value||'').trim();if(!file){document.getElementById('musicMsg').textContent='Selecione um arquivo MP3.';return}if(file.size>8*1024*1024){document.getElementById('musicMsg').textContent='O MP3 precisa ter no máximo 8 MB.';return}const reader=new FileReader();reader.onload=()=>{let d=ensureMusic(data());d.music.push({id:Date.now(),type:'mp3',title:title||file.name.replace(/\.mp3$/i,''),src:reader.result,active:true,createdAt:new Date().toISOString()});save(d);document.getElementById('mp3File').value='';document.getElementById('mp3Title').value='';document.getElementById('musicMsg').textContent='MP3 adicionado à playlist.';renderAdminMusic()};reader.readAsDataURL(file)}
function renderAdminMusic(){const el=document.getElementById('adminMusicList');if(!el)return;const d=ensureMusic(data());el.innerHTML=d.music.length?d.music.map((m,i)=>`<div class="messageCard companyRow"><div class="companyData"><b>${m.type==='youtube'?'▶️':'🎵'} ${esc(m.title)}</b><div class="mini">${m.type==='youtube'?'YouTube':'MP3'} • ${m.active!==false?'Ativa':'Desativada'}</div></div><div class="companyMsgActions"><button class="btn light" onclick="toggleMusic(${m.id})">${m.active!==false?'⏸️ Desativar':'▶️ Ativar'}</button><button class="btn danger" onclick="deleteMusic(${m.id})">🗑️ Excluir</button></div></div>`).join(''):'<p class="muted">Nenhuma música adicionada.</p>'}
function toggleMusic(id){let d=ensureMusic(data()),m=d.music.find(x=>Number(x.id)===Number(id));if(m)m.active=m.active===false;save(d);renderAdminMusic()}
function deleteMusic(id){let d=ensureMusic(data());d.music=d.music.filter(x=>Number(x.id)!==Number(id));save(d);renderAdminMusic()}
renderAdminMusic();

// Controles do Financeiro: um único listener por botão, sem onclick duplicado.
document.addEventListener("DOMContentLoaded", function(){
  function wireFinanceToggle(btnId, bodyId, openText, closeText){
    const btn=document.getElementById(btnId), body=document.getElementById(bodyId);
    if(!btn || !body || btn.dataset.wired === "1") return;
    btn.dataset.wired="1";
    const setState=(open)=>{
      body.classList.toggle("open", open);
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      btn.textContent=open ? closeText : openText;
    };
    setState(false);
    btn.addEventListener("click", function(ev){
      ev.preventDefault(); ev.stopPropagation();
      setState(!body.classList.contains("open"));
    }, {capture:false});
  }
  wireFinanceToggle("companiesToggleBtn","companiesFinanceBody","Ver empresas ▾","Ocultar empresas ▴");
  wireFinanceToggle("messagesToggleBtn","messagesFinanceBody","Ver cobranças ▾","Ocultar cobranças ▴");
});

JasTech - SITE COMPLETO

index.html          = site público
admin/index.html    = painel administrativo
server.py           = servidor e banco de dados

Execute:
python server.py

Site público:
http://localhost:8000/

Admin:
http://localhost:8000/admin/

Não abra os HTMLs diretamente pelo duplo clique. Use o server.py para que o site público e o painel administrativo compartilhem o mesmo banco de dados.
