Este projeto consiste na containerização de uma aplicação full-stack composta por:

* **Banco de Dados:** PostgreSQL
* **Backend:** Python + Flask
* **Frontend:** React + Nginx

Os containers se comunicam através de uma rede Docker customizada.

---

##  Passo a Passo para Execução

###  1. Criar a rede Docker

```bash
docker network create mural-rede
```

---

###  2. Subir o banco de dados (PostgreSQL)

```bash
docker run -d ^
  --name mural-db ^
  --network mural-rede ^
  -e POSTGRES_DB=muraldb ^
  -e POSTGRES_USER=admin ^
  -e POSTGRES_PASSWORD=root ^
  -v mural-db-dados:/var/lib/postgresql/data ^
  -v %cd%\db\init.sql:/docker-entrypoint-initdb.d/init.sql ^
  -p 5432:5432 ^
  postgres:15
```

Para verificar:

```bash
docker logs mural-db
```

Procure por:

```
database system is ready to accept connections
```

---

###  3. Build da imagem do backend

```bash
docker build -t mural-backend:v1 ./backend
```

---

###  4. Subir o container do backend

```bash
docker run -d ^
  --name mural-backend ^
  --network mural-rede ^
  -e DB_HOST=mural-db ^
  -e DB_NAME=muraldb ^
  -e DB_USER=admin ^
  -e DB_PASSWORD=root ^
  -p 5000:5000 ^
  mural-backend:v1
```

---

###  5. Testar o backend

Acesse no navegador:

```
http://localhost:5000/api/quotes
```

Se tudo estiver correto, será exibido um JSON com as citações.

---

###  6. Build da imagem do frontend

```bash
docker build --build-arg REACT_APP_API_URL=http://localhost:5000 -t mural-frontend:v1 ./frontend
```

A variável `REACT_APP_API_URL` é definida no build pois o React incorpora essa informação nos arquivos estáticos.

---

###  7. Subir o container do frontend

```bash
docker run -d ^
  --name mural-frontend ^
  --network mural-rede ^
  -p 8080:80 ^
  mural-frontend:v1
```

---

##  8. Acessar a aplicação

Abra o navegador e acesse:

```
http://localhost:8080
```

---

##  Funcionalidades esperadas

* Visualizar citações já cadastradas (vindas do `init.sql`)
* Adicionar novas citações
* Persistência de dados mesmo após reiniciar containers

---

##  Observações Importantes

* O backend se conecta ao banco utilizando o nome do container (`mural-db`) como host.
* O frontend utiliza `localhost` para acessar a API, pois a requisição é feita pelo navegador.
* O PostgreSQL utiliza volume para persistência de dados.
* O script `init.sql` é executado automaticamente na primeira inicialização do banco.

---

##  Comandos úteis

Ver logs:

```bash
docker logs mural-db
docker logs mural-backend
```

Parar containers:

```bash
docker stop mural-db mural-backend mural-frontend
```

Remover containers:

```bash
docker rm mural-db mural-backend mural-frontend ou docker rm -f mural-db mural-backend mural-frontend (O "f" significa force, ou seja, força a remoção, com ele, o Docker para o container se ele estiver rodando e depois remove.)
```
Remoce o volume:

>> docker volume rm mural-db-dados 

Remove a Rede:

>> docker network rm mural-rede

---

##  Conclusão

A aplicação foi completamente containerizada utilizando Docker, garantindo isolamento entre serviços, comunicação via rede e persistência de dados com volumes.