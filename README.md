# CME Project

Este projeto é um sistema de gerenciamento de materiais e rastreamento de processos para um Centro de Material e Esterilização (CME). O sistema faz parte de um teste solicitado. Foi feito de maneira simples mas bem estruturada com comentarios ao longo do código explicando a finalidade das funções e peculiaridades.

## Estrutura do Projeto

O projeto está dividido em duas partes principais: backend, frontend e a estruturação de um banco de dados com um arquivo init para iniciação do banco, tabelas e alguns dados de teste.

- **Backend**: Implementado em Python usando FastAPI, SQLAlchemy e PostgreSQL.
- **Frontend**: Implementado em React com TypeScript.
- **DB**: Postgres

## Pré-requisitos

- Docker
- Docker Compose

## Como Rodar o Projeto

### Passo 1: Clonar o Repositório

```sh
git clone git@github.com:LRaziel/cme_project.git
```

### Passo 2: Docker Compose
Certifique-se de que o Docker e o Docker Compose estão instalados e configurados corretamente em sua máquina. E então rode o projeto.

```sh
docker-compose up -d --build
```
OU
```sh
docker-compose up -d --build db
docker-compose up -d --build backend
docker-compose up -d --build frontend
```

### Passo 3: Acessar a Aplicação
- **Backend**: A API estará disponível em http://localhost:8080.
- **Frontend**: A aplicação React estará disponível em http://localhost:3030.

## Endpoints da API
Abaixo estão alguns dos principais endpoints da API:

**Usuários**
- **GET /users**: Lista todos os usuários.
- **POST /users**: Cria um novo usuário.
- **GET /users/role/{role}**: Lista usuários por função.

**Materiais**
- **GET /materials**: Lista todos os materiais.
- **POST /materials**: Cria um novo material.
- **GET /materials/stage/{stage}**: Lista materiais por etapa.
- **GET /materials/status/{status}**: Lista materiais por status.
- **GET /materials/with-tracking**: Lista materiais com rastreamento.

**Rastreamento**
- **GET /tracking**: Lista todos os rastreamentos.
- **POST /tracking**: Cria um novo rastreamento.
- **GET /tracking/{serial}**: Lista rastreamentos por serial.
- **GET /tracking/{serial}/failures**: Lista falhas por serial.
- **GET /tracking/report/pdf**: Gera relatório PDF.
- **GET /tracking/report/xlsx**: Gera relatório XLSX.

**Falhas**
- **GET /failures**: Lista todas as falhas.
- **POST /failures**: Cria uma nova falha.

### Estrutura de Diretórios
```sh
📦cme_project
 ┣ 📂backend
 ┃ ┣ 📂app
 ┃ ┃ ┣ 📜main.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂config
 ┃ ┃ ┣ 📜database.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂internal
 ┃ ┃ ┣ 📂models
 ┃ ┃ ┃ ┣ 📜db_models.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📜crud.py
 ┃ ┃ ┣ 📜schemas.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂routers
 ┃ ┃ ┣ 📜failures.py
 ┃ ┃ ┣ 📜materials.py
 ┃ ┃ ┣ 📜tracking.py
 ┃ ┃ ┣ 📜users.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜Dockerfile
 ┃ ┗ 📜requirements.txt
 ┣ 📂db
 ┃ ┗ 📜init.sql
 ┣ 📂frontend
 ┃ ┣ 📂public
 ┃ ┃ ┣ 📜favicon.ico
 ┃ ┃ ┣ 📜index.html
 ┃ ┃ ┣ 📜logo192.png
 ┃ ┃ ┣ 📜logo512.png
 ┃ ┃ ┣ 📜manifest.json
 ┃ ┃ ┗ 📜robots.txt
 ┃ ┣ 📂src
 ┃ ┃ ┣ 📂components
 ┃ ┃ ┃ ┣ 📜FormMaterial.tsx
 ┃ ┃ ┃ ┣ 📜FormTracking.tsx
 ┃ ┃ ┃ ┣ 📜FormUser.tsx
 ┃ ┃ ┃ ┣ 📜Home.tsx
 ┃ ┃ ┃ ┗ 📜TrackingTable.tsx
 ┃ ┃ ┣ 📂interfaces
 ┃ ┃ ┃ ┗ 📜interfaces.ts
 ┃ ┃ ┣ 📂services
 ┃ ┃ ┃ ┗ 📜api.ts
 ┃ ┃ ┣ 📜App.css
 ┃ ┃ ┣ 📜App.test.tsx
 ┃ ┃ ┣ 📜App.tsx
 ┃ ┃ ┣ 📜index.css
 ┃ ┃ ┣ 📜index.tsx
 ┃ ┃ ┣ 📜logo.svg
 ┃ ┃ ┣ 📜react-app-env.d.ts
 ┃ ┃ ┣ 📜reportWebVitals.ts
 ┃ ┃ ┗ 📜setupTests.ts
 ┃ ┣ 📜Dockerfile
 ┃ ┣ 📜package-lock.json
 ┃ ┣ 📜package.json
 ┃ ┣ 📜README.md
 ┃ ┗ 📜tsconfig.json
 ┣ 📜.gitignore
 ┣ 📜docker-compose.yml
 ┗ 📜README.md
```

