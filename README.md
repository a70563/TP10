# TP10

# Aplicação Call Center

App Call Center feita para realizar registos de pedidos, clientes e hamburgueres de um restaurante, utilizando um banco de base de dados.

## Utilização

Esta aplicação tem:

**Servidor Web**: Responsável por intermediar as acções entre App e Banco de Dados.
**Banco de Dados**: Armazena informações sobre os pedidos, hamburgueres, utilizadores e métricas de vendas.
**Aplicação Kivy**: Interface local para os funcionários do Siri Cascudo gerenciarem as operações do call center de maneira eficiente.

## Estrutura do TP10

Para este projeto foram feitos vários ficheiros para ser possivel a sua execução, sendo eles:


```
app.py
Cliente.py
Hamburguer.py
Pedido.py
database.py
main.py
models.py
README.md
```
Em cada um desses ficheiros, foi atribuído um determinado código para em conjunto ser possível executar o projeto.

### Cliente, Hamburguer e Pedido

Nestes ficheiros consta o código onde vai ser possível registar e adicionar o conteúdo/informações pedidas.


### Database (Banco de Dados)

Através do database é possivel criar a tabela do banco de dados, onde estes vão ser guardados/armazenados, à medida que vão sendo registados através da aplicação.

### Kivy App

Com a app e o main.py vai ser possivel executar uma aplicação propriamente estruturada para a utilização neste Call Center.

### Requirimentos 

- Python 
- Flask
- SQLite3
- Kivy
- Requests

Os requirimentos são apresentados também no ficheiro requirements.txt
