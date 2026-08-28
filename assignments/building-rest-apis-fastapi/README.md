# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objetivo

Aprender a criar uma API REST simples com FastAPI, definir modelos de dados, implementar endpoints de CRUD e testar a aplicação localmente usando boas práticas de desenvolvimento web.

## 📝 Tarefas

### 🛠️ Configure the FastAPI App

#### Descrição
Crie uma aplicação FastAPI mínima com um endpoint de saúde e a estrutura básica para servir uma API REST.

#### Requisitos
O programa concluído deve:

- Criar uma instância de `FastAPI`.
- Definir um endpoint `GET /health` que retorne um JSON com o status da API.
- Preparar o projeto para rodar com `uvicorn`.
- Usar uma estrutura clara e fácil de expandir para novos endpoints.

### 🛠️ Implement the Item Resource

#### Descrição
Defina um modelo para os dados de um item e implemente endpoints para listar, criar e consultar recursos da API.

#### Requisitos
O programa concluído deve:

- Criar um modelo de dados com campos como `id`, `name`, `description`, `price` e `available`.
- Implementar `GET /items` para listar todos os itens.
- Implementar `GET /items/{item_id}` para buscar um item por ID.
- Implementar `POST /items` para criar um novo item.
- Retornar dados em JSON com o formato esperado.

### 🛠️ Add Validation and Error Handling

#### Descrição
Melhore a API adicionando validação, tratamento de erros e comportamento mais robusto para requisições inválidas.

#### Requisitos
O programa concluído deve:

- Validar que `price` seja maior que zero.
- Validar campos obrigatórios e mensagens adequadas para entradas inválidas.
- Retornar `404` quando um item solicitado não existir.
- Dar suporte a filtros ou buscas simples por query parameters, se necessário.
- Garantir que a API responda de forma previsível e legível.
