1. SENHA DIFERENTE (ERRO PRINCIPAL)

Você criou o banco com:

POSTGRES_PASSWORD=root

Mas o backend tentou conectar com:

DB_PASSWORD=123

Resultado:

FATAL: password authentication failed for user "admin"

O que isso causa:

backend NÃO conecta no banco

API quebra

frontend fica sem dados

2. VOLUME DO POSTGRES (ERRO MAIS TRAIÇOEIRO)

Mesmo depois de corrigir a senha, ainda dava erro às vezes.

Por quê?

Porque o Postgres salva tudo no volume:

mural-db-dados

O problema:

a senha antiga fica guardada lá dentro

mudar POSTGRES_PASSWORD depois não muda o banco já criado

Ou seja:

você mudava a senha no comando… mas o banco continuava com a antiga

Por isso, isso resolveu:

docker volume rm mural-db-dados

3. FRONTEND APONTANDO PRO LUGAR ERRADO

Usei:

REACT_APP_API_URL=http://mural-backend:5000

Isso funciona dentro do Docker, mas não no navegador.

Resultado:

frontend abre 

tenta chamar API (falha)

não carrega citações

não cria novas

Por quê?

O navegador não sabe o que é:

mural-backend

Ele só entende:

localhost

Correção:

REACT_APP_API_URL=http://localhost:5000


Resumo:

-O erro principal foi inconsistência nas variáveis de ambiente, especialmente a senha do banco.

-O uso de volume persistente do PostgreSQL manteve configurações antigas, mesmo após alterações.

-O frontend inicialmente apontava para um hostname interno do Docker (mural-backend), que não é acessível pelo navegador.
