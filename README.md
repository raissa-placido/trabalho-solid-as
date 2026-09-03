# Projeto Web Store

Este projeto foi desenvolvido em Django como uma aplicação simples para demonstrar o uso de CRUD (Create, Read, Update e Delete) para duas entidades principais: categorias e produtos. A ideia principal é mostrar como a estrutura de uma aplicação web pode ser organizada de forma clara, com separação entre apresentação, regras de negócio e acesso ao banco de dados.

## Objetivo do projeto

O sistema foi construído para:

- cadastrar categorias;
- cadastrar produtos;
- listar registros em telas de administração;
- alterar e excluir dados;
- exemplificar os princípios SOLID em um contexto prático.

A página inicial também apresenta o diagrama ER do banco de dados, reforçando a estrutura do projeto.

## Funcionalidades implementadas

### 1. Tela inicial

A home da aplicação mostra uma mensagem explicando que a aplicação foi criada para exemplificar os princípios SOLID e exibe a imagem do DER do banco de dados.

### 2. Cadastro de categorias

A aplicação permite:

- listar todas as categorias;
- incluir uma nova categoria;
- alterar uma categoria existente;
- excluir uma categoria.

As operações são acessadas por rotas como:

- /categorias/
- /categorias/incluir/
- /categorias/alterar/<id>/
- /categorias/excluir/<id>/

### 3. Cadastro de produtos

A aplicação também permite:

- listar os produtos cadastrados;
- incluir um novo produto;
- alterar um produto existente;
- excluir um produto.

Os produtos possuem os campos principais:

- descrição;
- preço unitário;
- quantidade em estoque;
- categoria relacionada.

As rotas principais são:

- /produtos/
- /produtos/incluir/
- /produtos/alterar/<id>/
- /produtos/excluir/<id>/

## Estrutura do projeto

A organização do projeto está dividida em partes bem definidas:

- `app/views.py`: controla as páginas e as ações do sistema;
- `app/services.py`: contém a lógica de acesso ao banco e operações de negócios;
- `app/database.py`: gerencia a conexão com o SQLite;
- `app/forms.py`: define os formulários do Django;
- `app/templates/`: arquivos HTML das telas;
- `proj_solid/urls.py`: define as rotas da aplicação;
- `db_solid.sqlite3`: banco de dados SQLite utilizado pela aplicação.

## Arquitetura e lógica

O projeto segue uma abordagem simples de separação de responsabilidades:

- as views cuidam da interação com o usuário e com a requisição HTTP;
- os services executam as operações de banco de dados;
- os formulários validam os dados recebidos;
- os templates renderizam a interface web.

Essa organização facilita a manutenção e torna mais fácil entender como cada camada atua no sistema.

## Tecnologias utilizadas

- Python
- Django
- SQLite
- HTML
- CSS

## Como executar o projeto

1. Acesse a pasta do projeto.
2. Verifique se o ambiente Python está configurado.
3. Instale o Django, caso ainda não tenha:

```bash
pip install django
```

4. Inicie o servidor:

```bash
python manage.py runserver
```

5. Abra no navegador:

```text
http://127.0.0.1:8000/
```

## Observações

- O projeto usa um banco SQLite local já incluído no repositório.
- A aplicação foi criada principalmente como exemplo didático para entender a relação entre Django, banco de dados e CRUD.
- A navegação fica disponível por meio do menu principal da interface.

## Conclusão

Este projeto representa uma aplicação web funcional de cadastro de categorias e produtos, com foco em organização, boas práticas de estrutura e demonstração dos princípios SOLID em um cenário real de desenvolvimento com Django.
