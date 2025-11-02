# Workout API

API REST para gerenciamento de atletas, categorias e centros de treinamento. O projeto permite cadastrar atletas com suas informações físicas, associá-los a categorias competitivas e centros de treinamento.

## Sobre o Projeto

A Workout API é uma aplicação desenvolvida para facilitar o gerenciamento de atletas em competições esportivas. Através dela é possível:

- Cadastrar e gerenciar atletas com informações como nome, CPF, idade, peso, altura e sexo
- Organizar atletas por categorias
- Associar atletas a centros de treinamento
- Consultar, atualizar e remover registros

## Tecnologias Utilizadas

- **Python 3.10+** 
- **FastAPI 0.100.1** 
- **SQLAlchemy 2.0.19** 
- **Alembic 1.11.1**
- **Pydantic 2.1.1**
- **PostgreSQL**
- **AsyncPG 0.28.0**
- **Uvicorn 0.23.1** 
- **Docker**


## Pré-requisitos

- Python 3.10 ou superior
- Docker e Docker Compose
- pip (gerenciador de pacotes Python)

## Instalação e Configuração

### 1. Clone o repositório

```bash
cd /home/gilvania/projects/workout_api
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Inicie o banco de dados

```bash
docker-compose up -d
```

### 4. Execute as migrações

```bash
make run-migrations
```

### 5. Inicie a aplicação

```bash
make run
```

A API estará disponível em `http://localhost:8001`

## Documentação da API

Após iniciar a aplicação, acesse:

- **Swagger UI**: `http://localhost:8001/docs`
- **ReDoc**: `http://localhost:8001/redoc`

## Endpoints Disponíveis

### Atletas

- `POST /atletas/` - Criar novo atleta
- `GET /atletas/` - Listar todos os atletas
- `GET /atletas/{id}` - Consultar atleta por ID
- `PATCH /atletas/{id}` - Atualizar atleta
- `DELETE /atletas/{id}` - Remover atleta

### Categorias

- `POST /categorias/` - Criar nova categoria
- `GET /categorias/` - Listar todas as categorias
- `GET /categorias/{id}` - Consultar categoria por ID

### Centros de Treinamento

- `POST /centros_treinamento/` - Criar novo centro de treinamento
- `GET /centros_treinamento/` - Listar todos os centros
- `GET /centros_treinamento/{id}` - Consultar centro por ID

## Exemplos de Uso

### Criar uma Categoria

```bash
curl -X POST "http://localhost:8001/categorias/" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Scale"
  }'
```

### Criar um Centro de Treinamento

```bash
curl -X POST "http://localhost:8001/centros_treinamento/" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "CT King",
    "endereco": "Rua X, Q02",
    "proprietario": "Marcos"
  }'
```

### Criar um Atleta

```bash
curl -X POST "http://localhost:8001/atletas/" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "João Silva",
    "cpf": "12345678900",
    "idade": 25,
    "peso": 75.5,
    "altura": 1.75,
    "sexo": "M",
    "categoria": {
      "nome": "Scale"
    },
    "centro_treinamento": {
      "nome": "CT King"
    }
  }'
```

### Listar Atletas

```bash
curl -X GET "http://localhost:8001/atletas/"
```

## Comandos Úteis (Makefile)

```bash
# Iniciar a aplicação
make run

# Criar nova migração
make create-migrations d="descrição da migração"

# Aplicar migrações
make run-migrations
```

## Configurações do Banco de Dados

As configurações padrão do banco de dados estão definidas em `configs/settings.py`:

```python
DB_URL = "postgresql+asyncpg://workout:workout@localhost/workout"
```

Para alterar, você pode definir variáveis de ambiente ou modificar o arquivo de configuração.



