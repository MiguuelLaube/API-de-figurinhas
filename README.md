# ⚽ API Figurinhas da Copa 🏆

API REST para gerenciamento de figurinhas do álbum da Copa do Mundo.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

---

## 📋 Pré-requisitos

| Software | Versão | Download |
|----------|--------|----------|
| Python | 3.10+ | [python.org](https://www.python.org/downloads/) |
| XAMPP | 8.0+ | [apachefriends.org](https://www.apachefriends.org/pt_br/index.html) |
| Git | qualquer | [git-scm.com](https://git-scm.com/downloads) |

> Na instalação do Python, marque a opção **"Add Python to PATH"**.

---

## 🗄️ Configuração do Banco de Dados (XAMPP)

**1.** Abra o **XAMPP Control Panel** e inicie o **Apache** e o **MySQL**

**2.** Acesse o phpMyAdmin no navegador: http://localhost/phpmyadmin

**3.** Clique na aba **Importar** → **Escolher arquivo** → selecione o `banco_figurinhas.sql` → **Executar**

Isso criará o banco `db_time`, a tabela `tb_figurinhas` e populará com 30 figurinhas de exemplo.

---

## 🚀 Instalação

```bash
# Clonar o repositório
git clone <URL_DO_REPOSITORIO>
cd API

# Criar o ambiente virtual
python -m venv venv
#Liberar a política de execução
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
# Ativar o ambiente virtual
venv\Scripts\activate            # Windows CMD
# venv\Scripts\Activate.ps1      # Windows PowerShell
# source venv/bin/activate       # Linux / macOS

# Instalar as dependências
pip install fastapi uvicorn sqlalchemy pymysql python-dotenv
```

### Configurar o `.env`

Crie o arquivo `.env` na raiz do projeto:

```env
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
DB_NAME=db_time
```

> No XAMPP o usuário padrão é `root` com senha vazia.

---

## ▶️ Executando

```bash
uvicorn main:app --reload
```

Acesse:

| Recurso | URL |
|---------|-----|
| API | http://127.0.0.1:8000 |
| Swagger (documentação interativa) | http://127.0.0.1:8000/docs |
| ReDoc | http://127.0.0.1:8000/redoc |

---

## 📡 Rotas

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/figurinhas/` | Listar todas as figurinhas |
| `POST` | `/figurinhas/` | Criar uma nova figurinha |
| `GET` | `/figurinhas/{id}` | Buscar figurinha por ID |
| `PUT` | `/figurinhas/{id}` | Atualizar uma figurinha |
| `DELETE` | `/figurinhas/{id}` | Deletar uma figurinha |
| `GET` | `/figurinhas/busca/?nome=...` | Buscar por nome do jogador |
| `GET` | `/figurinhas/pais/{pais}` | Buscar por país |

---

## 💡 Exemplos

**Listar todas:**
```bash
curl http://127.0.0.1:8000/figurinhas/
```

**Criar figurinha:**
```bash
curl -X POST http://127.0.0.1:8000/figurinhas/ \
  -H "Content-Type: application/json" \
  -d '{
    "nome_jogador": "Ronaldinho Gaúcho",
    "pais": "Brasil",
    "posicao": "Meio-campo",
    "numero_camisa": 10,
    "raridade": "Lendária",
    "repetida": false
  }'
```

**Buscar por ID:**
```bash
curl http://127.0.0.1:8000/figurinhas/1
```

**Buscar por país:**
```bash
curl http://127.0.0.1:8000/figurinhas/pais/Brasil
```

**Atualizar:**
```bash
curl -X PUT http://127.0.0.1:8000/figurinhas/1 \
  -H "Content-Type: application/json" \
  -d '{
    "nome_jogador": "Neymar Jr",
    "pais": "Brasil",
    "posicao": "Atacante",
    "numero_camisa": 10,
    "raridade": "Lendária",
    "repetida": true
  }'
```

**Deletar:**
```bash
curl -X DELETE http://127.0.0.1:8000/figurinhas/1
```

---

## 📁 Estrutura do Projeto

```
API/
├── .env                    # Variáveis de ambiente (conexão com o banco)
├── .gitignore              # Arquivos ignorados pelo Git
├── banco_figurinhas.sql    # Script SQL para criar e popular o banco
├── database.py             # Configuração da conexão com o MySQL
├── main.py                 # Rotas da API (endpoints)
├── models.py               # Modelo da tabela (SQLAlchemy)
├── schemas.py              # Schemas de validação (Pydantic)
└── README.md               # Documentação
```

---

## 🛠️ Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/) — Framework web
- [Uvicorn](https://www.uvicorn.org/) — Servidor ASGI
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM
- [PyMySQL](https://pymysql.readthedocs.io/) — Driver MySQL
- [Pydantic](https://docs.pydantic.dev/) — Validação de dados
- [XAMPP](https://www.apachefriends.org/) — Servidor MySQL local
