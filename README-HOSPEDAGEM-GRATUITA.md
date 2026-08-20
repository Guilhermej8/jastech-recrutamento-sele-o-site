# JasTech — pacote pronto para hospedagem

Este pacote foi preparado para serviços de hospedagem que executam Python, como o Render.

## Arquivos de implantação

- `server.py` — servidor web e API.
- `render.yaml` — configuração de implantação.
- `Procfile` — comando de inicialização compatível.
- `requirements.txt` — dependências (nenhuma externa).
- `index.html` — site público.
- `admin/index.html` — área administrativa.
- `jastech.db` — criado automaticamente no primeiro uso (não fica dentro do ZIP).

## Publicação no Render

1. Crie uma conta no Render.
2. Crie um novo Web Service a partir deste projeto/ZIP enviado para um repositório Git.
3. Use o comando `python server.py` para iniciar.
4. O Render fornecerá um endereço HTTPS público.
5. O site ficará na raiz `/` e o painel em `/admin/`.

## Atenção sobre o banco

O projeto usa SQLite (`jastech.db`). Em hospedagens gratuitas sem disco persistente, o banco pode ser apagado após reinicializações/deploys. Para uso comercial, recomenda-se migrar o estado para PostgreSQL/Supabase ou outro banco persistente.

## Acesso administrativo atual

O projeto original mantém o acesso administrativo no JavaScript, com usuário `admin` e senha inicial `1234`. **Troque essa senha antes de uso real e não considere este login uma proteção de segurança de nível empresarial.**
