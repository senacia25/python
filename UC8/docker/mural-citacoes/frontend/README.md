# Frontend — Mural de Citações (React)

Esta é a aplicação frontend do projeto. Ela foi construída com **React** e consome a API do backend para exibir e adicionar citações.

## O que você precisa saber sobre esta aplicação

Você **não precisa entender o código React** para esta atividade. Seu objetivo é aprender a **containerizar** esta aplicação.

## Como esta aplicação funciona

Esta é uma aplicação de **página única (SPA)**. Para ser servida em produção, ela precisa passar por um processo chamado **build**, que transforma o código React em arquivos estáticos simples (HTML, CSS e JavaScript) que qualquer servidor web (como o Nginx) consegue servir.

O fluxo é:
1. Instalar as dependências: `npm install`
2. Gerar os arquivos estáticos: `npm run build`
3. Servir a pasta `build/` com um servidor web (Nginx)

## Sua Missão: Criar o Dockerfile

Você deve criar um `Dockerfile` nesta pasta que faça tudo isso automaticamente usando **multi-stage build**.

### Dica de Estrutura

```dockerfile
# ---- ESTÁGIO 1: BUILD ----
# Use uma imagem do Node.js para instalar dependências e gerar o build
FROM node:18-alpine AS builder

WORKDIR /app

# Copie os arquivos de dependências e instale
COPY package.json .
RUN npm install

# Copie o restante do código e gere o build de produção
COPY . .
RUN npm run build

# ---- ESTÁGIO 2: PRODUÇÃO ----
# Use uma imagem leve do Nginx para servir os arquivos estáticos
FROM nginx:stable-alpine

# Copie APENAS a pasta build do estágio anterior para o Nginx
COPY --from=builder /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

## Variável de Ambiente

A aplicação usa a variável `REACT_APP_API_URL` para saber onde está o backend. Você deve passá-la no momento do **build** (não no `docker run`), pois o React a incorpora nos arquivos estáticos.

```bash
docker build --build-arg REACT_APP_API_URL=http://localhost:5000 -t mural-frontend:v1 .
```

> **Atenção:** No React, variáveis de ambiente são "queimadas" no código durante o build. Por isso, você passa com `--build-arg` e não com `-e` no `docker run`.
