# Portfolio em Django

## Sobre
Portfolio idealizado como forma de avaliação para a 1° verificação de aprendizagem da disciplina optativa de **Projetos de Sistemas Web** ministrado pelo prof. Héldon José no curso de **Bacharelado em Sistemas de Informação** da **UFRPE-UAST**.

## Algumas orientações
### Requsitos Mínimos:
- Python v3+
- Banco PostgreSQL
### Fazer o clone:
    git clone git@github.com:renigoms/portifolio_django.git

### Gerar o venv:

    python -m venv .venv

## Instalar Bibliotecas:
    pip install -r requirements.txt

### Gerar arquivo .env:
- Crie o arquivo na raiz do projeto:
    - Windows:
        ```shell
            notepad .env
        ```
    - Linux:
        ```shell
            touch .env
        ```
- Coloque nele os seguintes dados:
    ```shell
        HOST=<host>
        NAME=<name>
        USER_DB=<username>
        PASSWORD=<password>
        PORT=<port>

        # Email Credential
        EMAIL_USER=<useremail>
        EMAIL_PASSWORD=<password>
    ```
### Iniciar servidor Django
    python manage.py runserver
### URL principais
    <caminho_gerado_gerado_pelo_django>/portfolio
    <caminho_gerado_gerado_pelo_django>/admin
