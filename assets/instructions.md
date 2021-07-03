# Coding Challenge Vaga Full-time 42 São Paulo

Sua tarefa é construir uma API e banco de dados para uma aplicação de cadastro de alunos. A aplicação é um simples repositório para gerenciar alunos com seus respectivos nomes, intra ids, e projetos que estão trabalhando atualmente.

A aplicação pode ser construída utilizando qualquer linguagem, banco de dados, frameworks, libraries e ferramentas de sua preferência (Ex: Node + Express + Mongoose + MongoDB, etc). Apesar disso, a stack mais comum na 42 São Paulo é **Golang,** seguida por **Python**.

## O que será avaliado

Queremos avaliar sua capacidade de desenvolver e documentar um back-end para uma aplicação. Serão avaliados:

- Código bem escrito e limpo;
- Quais ferramentas foram usadas, como e por quê;
- Sua criatividade e capacidade de lidar com problemas diferentes;
- Sua capacidade de se comprometer com o que foi fornecido;
- Sua capacidade de documentação da sua aplicação.

## O mínimo necessário

- Uma aplicação contendo uma API simples, sem autenticação, que atenda os requisitos descritos abaixo, fazendo requisições à um banco de dados para persistência;
- README.md contendo informações básicas do projeto e como executá-lo;

## Bônus

Os seguintes itens não são obrigatórios, mas darão mais valor ao seu trabalho (os em negrito são mais significativos para nós)

- Uso de ferramentas externas que facilitem o seu trabalho;
- Cuidados especiais com otimização, padrões, entre outros;
- Migrations ou script para configuração do banco de dados utilizado;
- **Testes**;
- **Conteinerização da aplicação**;
- **Autenticação e autorização** (**OAuth, JWT**);
- Sugestões sobre o challenge embasadas em alguma argumentação.

# Requisitos

## 0: A API deve responder na porta 3000

## 1: Deve haver uma rota para listar todos os alunos cadastrados

`GET /students`

Resposta:

```jsx
[
    {
        id: 1,
        name: "Gustavo Belfort",
        intra_id: "gus",
        projects: [
            "42cursus_libft",
            "42cursus_get-next-line",
            "42cursus_ft-printf",
        ]
    },
    {
        id: 2,
        name: "Guilhemar Caixeta",
        intra_id: "guiga",
        projects: [
            "cub3d",
        ]
    }
]
```

## 2: Deve ser possível filtrar alunos utilizando uma busca por projeto

`GET /students?projects=42cursus_libft`   (*42cursus_libft* é a tag sendo buscada neste exemplo)

Resposta:

```jsx
[
    {
        id: 1,
        name: "Gustavo Belfort",
        intra_id: "gus",
        projects: [
            "42cursus_libft",
            "42cursus_get-next-line",
            "42cursus_ft-printf",
        ]
    }
]
```

## 3: Deve haver uma rota para cadastrar um novo aluno

O corpo da requisição deve conter as informações do aluno a ser cadastrado, sem o ID (gerado automaticamente pelo servidor). A resposta, em caso de sucesso, deve ser o mesmo objeto, com seu novo ID gerado.

`POST /students
Content-Type: application/json`

```jsx
    {
        "name": "Gustavo Belfort",
        "intra_id": "gus",
        "projects": ["42cursus_libft","42cursus_get-next-line","42cursus_ft-printf"]
    }
```

Resposta:

`Status: 201 Created`

`Content-Type: application/json`

```jsx
    {
        "name": "Gustavo Belfort",
        "intra_id": "gus",
        "projects": ["42cursus_libft","42cursus_get-next-line","42cursus_ft-printf"],
        "id": 1
    }
```

## 4: O usuário deve poder remover um aluno por ID

`DELETE /students/:id`

Resposta:

`Status: 200 OK`

```jsx
{}
```

## Critérios de Aceitação

- A API deve ser real e escrita por você. Ferramentas que criam APIs automaticamente (Loopback, json-server, etc) não são aceitas;
- Todos os requisitos acima devem ser cumpridos, seguindo o padrão de rotas estabelecido;
- Deve haver uma documentação descrevendo sua API;
- Se você julgar necessário, adequado ou quiser deixar a aplicação mais completa (bônus!) você pode adicionar outras rotas, métodos, meios de autenticação com usuários, etc.

## Formato de entrega

Seu código deverá ser submetido neste repositório, sinta-se livre pare substituir este README.md com o seu próprio.
