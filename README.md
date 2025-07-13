
# Projeto GCES 2025-1 – Aplicação Django + Next.js com CI/CD

Este projeto é parte do trabalho individual da disciplina **Gerência de Configuração de Software (GCES)**. A aplicação é composta por:

- **Backend**: Django + Django REST Framework + JWT Authentication
- **Frontend**: Next.js + TailwindCSS
- **Banco de Dados**: PostgreSQL

Todo o ambiente é containerizado com **Docker** e orquestrado com **Docker Compose**, para desenvolvimento e produção. Também conta com **pipeline de CI/CD automatizado via GitLab CI**, com etapas de build, teste, lint e deploy contínuo para o Container Registry.

---

## 📦 Estrutura do Projeto

```
.
├── api/               # Backend Django
├── www/               # Frontend Next.js
├── docker-compose.yml             # Ambiente de desenvolvimento
├── docker-compose.prod.yml        # Ambiente de produção
├── Dockerfile.dev.api             # Docker dev - backend
├── Dockerfile.dev.www            # Docker dev - frontend
├── Dockerfile.prod.api           # Docker prod - backend
├── Dockerfile.prod.www          # Docker prod - frontend
├── nginx/                        # Configuração para Nginx (produção)
├── .gitlab-ci.yml               # Pipeline de CI/CD
```

---

## 🚀 Desenvolvimento Local (modo DEV)

### Pré-requisitos

- Docker
- Docker Compose

### Rodando o ambiente completo

```bash
docker compose up --build
```

- Frontend: http://localhost:4000
- Backend (API): http://localhost:4001

As alterações no código são refletidas automaticamente (hot reload).

---

## 🧪 Testes e Lint

### Testes Backend

```bash
docker compose exec api python manage.py test
```

### Testes Frontend

```bash
docker compose exec www npm run test
```

### Lint Backend

```bash
docker compose exec api flake8
```

### Lint Frontend

```bash
docker compose exec www npm run lint
```

---

## 📦 Produção (modo PROD)

A produção roda com:

- **Nginx** servindo o frontend exportado (`next export`)
- **Django** com configurações de `DEBUG=False` e banco PostgreSQL
- **Sem exposição de portas exceto 80 e 443**

### Rodando localmente (prod)

```bash
docker compose -f docker-compose.prod.yml up --build
```

---

## 🔄 CI/CD com GitLab

O pipeline de CI está definido em `.gitlab-ci.yml` e realiza:

- **Build** dos serviços
- **Testes automatizados**
- **Análise de estilo (lint)**
- **Deploy contínuo** com envio das imagens para o GitLab Container Registry

---

## 📌 Variáveis de Ambiente

Crie um `.env` na raiz ou configure via GitLab CI:

**Backend (.env):**
```
SECRET_KEY=...
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=postgres://user:password@db:5432/dbname
```

**Frontend (www/.env.local):**
```
NEXT_PUBLIC_API_HOST=http://localhost:4001
```

---

## 🐳 Publicação das Imagens

O deploy contínuo envia as imagens para o GitLab Container Registry:

- `registry.gitlab.com/<user>/<repo>/api`
- `registry.gitlab.com/<user>/<repo>/www`

---

## ✅ Etapas Entregues (Trabalho GCES)

| Etapa | Descrição | Entregue |
|-------|-----------|----------|
| 1     | Containerização DEV (Dockerfiles) | ✅ |
| 2     | Docker Compose (DEV) | ✅ |
| 3.1   | CI - Build | ✅ |
| 3.2   | CI - Testes | ✅ |
| 3.3   | CI - Lint | ✅ |
| 4     | Dockerfiles PROD | ✅ |
| 5     | Compose PROD com Nginx + SSL | ✅ |
| 6     | Deploy Contínuo no GitLab Registry | ✅ |

---

## 👨‍💻 Autor

Vitor Carvalho Pereira  
GitLab: [`vcpVitor`](https://gitlab.com/vcpVitor)
