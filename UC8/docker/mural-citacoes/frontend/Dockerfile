# ---- ESTÁGIO 1: BUILD ----
FROM node:18-alpine AS builder

WORKDIR /app

# Copiar dependências e instalar
COPY package.json package-lock.json* ./
RUN npm install

# Copiar o restante do código e gerar o build
COPY . .
# Passar a URL do backend via build-arg
ARG REACT_APP_API_URL
ENV REACT_APP_API_URL=$REACT_APP_API_URL
RUN npm run build

# ---- ESTÁGIO 2: PRODUÇÃO ----
FROM nginx:stable-alpine

# Copiar build para o Nginx
COPY --from=builder /app/build /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]