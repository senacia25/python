# Atividade Avaliativa: Docker — Construindo uma Aplicação Full-Stack

**Disciplina:** [Nome da Disciplina]
**Data de Entrega:** [Data]

---

## 1. Objetivo Pedagógico

Esta atividade consolida os conhecimentos adquiridos na aula de Docker: criação de redes, uso de volumes, variáveis de ambiente e comunicação entre containers. O desafio central é que você terá de containerizar uma aplicação construída com uma tecnologia que ainda não conhece, desenvolvendo a habilidade mais importante de um profissional DevOps: **pesquisar e adaptar**.

---

## 2. O Cenário: Mini-Blog de Citações

Você recebeu o código-fonte de um sistema chamado **Mural de Citações**. Sua missão é fazer toda a infraestrutura funcionar com Docker, sem usar Docker Compose.

O sistema é composto por três serviços que precisam se comunicar:

| Serviço | Tecnologia | Pasta | Porta |
| :--- | :--- | :--- | :--- |
| **Banco de Dados** | PostgreSQL | `db/` | 5432 |
| **Backend (API)** | Python + Flask | `backend/` | 5000 |
| **Frontend** | React (Node.js) | `frontend/` | 80 |

---

## 3. Estrutura do Projeto Entregue

```
mural-citacoes/
├── backend/
│   ├── app.py              ← Código da API (Python/Flask)
│   ├── requirements.txt    ← Dependências Python
│   └── Dockerfile          ← (VOCÊ PRECISA CRIAR ESTE ARQUIVO)
│
├── frontend/
│   ├── src/                ← Código React (não precisa modificar)
│   ├── public/
│   ├── package.json
│   ├── README.md           ← Leia este arquivo!
│   └── Dockerfile          ← (VOCÊ PRECISA CRIAR ESTE ARQUIVO)
│
└── db/
    └── init.sql            ← Script SQL que cria a tabela e insere dados iniciais
```

---

## 4. O Que Você Deve Fazer

### Parte 1 — Criar a Rede

Crie uma rede Docker customizada para que os três containers possam se comunicar usando seus nomes como endereço.

```bash
docker network create mural-rede
```

### Parte 2 — Subir o Banco de Dados (PostgreSQL)

Suba um container do PostgreSQL na rede criada. Observe que estamos usando **PostgreSQL**, não MySQL. O princípio é o mesmo, mas os nomes das variáveis de ambiente são diferentes. Pesquise a imagem oficial `postgres` no Docker Hub para descobrir quais variáveis usar.

Requisitos obrigatórios para o container do banco:
- Deve estar na rede `mural-rede`.
- Deve ter um **volume nomeado** para persistir os dados.
- Deve ter um nome de container (ex: `mural-db`).
- Deve montar o arquivo `db/init.sql` no diretório `/docker-entrypoint-initdb.d/` do container (o PostgreSQL executa automaticamente os scripts SQL nessa pasta ao iniciar).

### Parte 3 — Criar o Dockerfile do Backend

O Dockerfile do backend já foi criado para você como referência. Leia-o, entenda cada linha e, se quiser, personalize.

Em seguida, construa a imagem:

```bash
docker build -t mural-backend:v1 ./backend
```

Suba o container do backend. Ele precisa:
- Estar na rede `mural-rede`.
- Receber as variáveis de ambiente para se conectar ao banco (`DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`). O valor de `DB_HOST` deve ser o **nome do container** do banco de dados.
- Ter a porta 5000 mapeada.

### Parte 4 — Criar o Dockerfile do Frontend (O Desafio Principal)

Esta é a parte mais importante da atividade. Você deve criar um `Dockerfile` dentro da pasta `frontend/`.

Leia o arquivo `frontend/README.md` — ele contém uma dica com a estrutura do Dockerfile que você precisa criar, usando a técnica de **multi-stage build**.

Após criar o Dockerfile, construa a imagem:

```bash
docker build -t mural-frontend:v1 ./frontend
```

Suba o container do frontend com a porta 8080 do seu computador mapeada para a porta 80 do container.

### Parte 5 — Testar a Aplicação

Acesse `http://localhost:8080` no seu navegador. Se tudo estiver correto, você verá o Mural de Citações com as citações iniciais do banco de dados e poderá adicionar novas.

---

## 5. Critérios de Avaliação

| Critério | Peso | O que será avaliado |
| :--- | :---: | :--- |
| Banco de dados funcionando com volume e init.sql | 20% | Dados iniciais aparecem na tela |
| Backend conectado ao banco via rede Docker | 20% | API responde em `/api/health` e `/api/quotes` |
| Dockerfile do frontend com multi-stage build | 30% | Imagem final usa Nginx e não tem Node.js |
| Comunicação completa entre os 3 containers | 20% | É possível adicionar e ver citações no navegador |
| Organização e arquivo `INSTRUCOES.md` | 10% | Comandos claros e corretos para reproduzir o ambiente |

---

## 6. O Que Entregar

Crie um arquivo `INSTRUCOES.md` na raiz do projeto com todos os comandos, na ordem correta, para que qualquer pessoa consiga reproduzir o seu ambiente do zero. Compacte a pasta `mural-citacoes/` em um arquivo `.zip` e entregue.

---

## 7. Dicas Finais

- Use `docker logs NOME_DO_CONTAINER` sempre que algo não funcionar. Os logs são seus melhores amigos.
- Se o backend não conseguir conectar ao banco, verifique se o nome do container do banco está correto na variável `DB_HOST`.
- O PostgreSQL pode demorar alguns segundos para iniciar. Se o backend falhar na primeira tentativa, espere e tente novamente.
- Para o frontend, a palavra-chave de pesquisa mais útil é: **"multi-stage build react nginx dockerfile"**.
