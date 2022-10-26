
# MONGO DOS

Descrição: o presente trabalho destina-se a avaliação da aprendizagem
dos conteúdos ministrados durante o módulo de Banco de Dados II,
aplicando manipulação sobre dados em bancos NoSQL.

Objetivo: Implementar um software em Linguagem Python, para criação e
manipulação de bancos de dados NoSQL com MongoDB.
## Funcionalidades

- O programa deve ser implementado em Python
- Deve ser utilizado o banco MongoDB como banco NoSQL. Não serão aceitos outros bancos de dados.
- Pode utilizar quantos arquivos julgar necessário.
- Procure organizar o código da melhor forma possível.
- O programa deverá fornecer ao usuário as seguintes opções.
    - a) Criar um ou mais banco de dados, com o nome fornecido pelo usuário.
    - b) Criar uma ou mais coleções, com o nome fornecido pelo usuário.
    - c) Inserir documentos.
        - Deverá ser pedido ao usuário, qual a coleção onde deve ser inserido.
        - Pedir quais os pares de chave-valor a serem inseridos em cada documento.
    - d) Buscar documentos.
        - O usuário deve escolher se busca por todos os documentos, ou se quer aplicar algum filtro (critério de seleção), e nesse caso ele deve fornecer a chave e o valor correspondente do filtro. Obs: apenas são permitidos testes de igualdade e apenas um filtro para busca.
        - Forneça a opção de limitar a busca a uma quantidade informada de registros.

    - e) Deletar documentos.
        - O Usuário deve fornecer qual as chaves utilizadas na condição da remoção e qual o valor correspondente para encontrar o(s) registros a serem deletados. Obs: apenas será considerado o teste de igualdade para encontrar registros e um único filtro para encontrar os registros a serem deletados.

    - f) Remover coleções.
    - g) Listar bancos de dados.
    - h) Listar coleções de um banco de dados.

## Stack utilizada


**Back-end:** Python, MongoDB, PyMongo, Terminal (CMD)


## Licença

[MIT](https://choosealicense.com/licenses/mit/)

 - Name APP - MongoDos 
 - Version BETA 1.0



## Instalação

Requisitos da aplicação:

```bash
    - Ferramentas e biliotecas necessárias: 
        - python
        - MongoDB
        - PyMongo 
```
    
## Deploy

Para fazer o deploy desse projeto:

```bash
    - Start o serviço do MongoDB 
    - Vá ate a diretório do projeto
    - Execute no TERMINAL (CMD) o arquivo app.py

    ... Agora é so usar a aplicação MongoDos...
```


## Suporte

Para ideias de melhorias, informações, e direitos, mande um email para dxdiegofelipe@hotmail.com

