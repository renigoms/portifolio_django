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
  
        # COMPANY HASH
        HASH=<company hash>
    ```
  * **Extra:** Na parte de EMAIL_PASSWORD você não vai usar sua senha normal do gmail. Em vez disso, você vai seguir os seguintes passos:
    * Habilitar a verificação de duas etapas;
    * Gerar uma senha de App:
      * [Como fazer no Gmail;](https://youtu.be/Lz6fJChKRtA)
      * [Como fazer no Outlook;](https://youtu.be/u5Xm1LMJOdE)

### Realizar as migrações 
    python manage.py migrate

### Iniciar servidor Django
    python manage.py runserver

### URL principais
    http://127.0.0.1:8000/portfolio
    http://127.0.0.1:8000/admin

### Teste
* Crie um usuário administrador
  ```shell
    python manager.py createsuperuser
  ```
* Acesse http://127.0.0.1:8000/admin e faça o login
* Crie um perfil persoal com seus dados
* Adicione alguns certificados e projetos
* Acesse http://127.0.0.1:8000/portfolio

# Microserviço de Notificação

## Sobre
O microsserviço de noticações foi idealizado para enviar notificações ao portifólio.

## Algumas orientações
### Requsitos Mínimos:
- Python v3+

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
        URL=http://127.0.0.1:8001/api/notificacoes/criar/
        # COMPANY HASH
        HASH=<company hash>
    ```

### Realizar as migrações 
    python manage.py migrate

### Iniciar servidor Django
    python manage.py runserver 8001

### Crie um usuário administrador
    python manager.py createsuperuser

### Testes
* **Teste de criação**
    ```shell
    # Criar notificacoes via API (simulando outro sistema)
        # Substitua SEU_HASH_AQUI pelo hash da empresa
        
        curl -X POST http://127.0.0.1:8001/api/notificacoes/criar/ \
             -H "X-Api-Key: SEU_HASH_AQUI" \
             -H "Content-Type: application/json" \
             -d '{"user_id": 1,  "title": "Nova Notificação1", "message": "Bem-vindo ao sistema de notificacoes!"}'
        
        curl -X POST http://127.0.0.1:8001/api/notificacoes/criar/ \
             -H "X-Api-Key: SEU_HASH_AQUI" \
             -H "Content-Type: application/json" \
             -d '{"user_id": 1,  "title": "Nova Notificação2", "message": "Seu perfil foi atualizado com sucesso."}'
        
        curl -X POST http://127.0.0.1:8001/api/notificacoes/criar/ \
             -H "X-Api-Key: SEU_HASH_AQUI" \
             -H "Content-Type: application/json" \
             -d '{"user_id": 1,  "title": "Nova Notificação3", "message": "Nova aula disponivel: Microservicos"}'
    ```

* **Testar leitura com curl**
    ```shell
     # 1. Contar notificacoes nao lidas
    curl http://127.0.0.1:8001/api/notificacoes/nao-lidas/ \
         -H "X-Api-Key: SEU_HASH_AQUI" \
         -H "X-User-Id: 1"
    
    # Resposta esperada: {"count": 3}
    
    # 2. Listar todas as notificacoes
    curl http://127.0.0.1:8001/api/notificacoes/ \
         -H "X-Api-Key: SEU_HASH_AQUI" \
         -H "X-User-Id: 1"
    
    # 3. Listar somente nao lidas
    curl "http://127.0.0.1:8001/api/notificacoes/?is_read=false" \
         -H "X-Api-Key: SEU_HASH_AQUI" \
         -H "X-User-Id: 1"
    
    # 4. Marcar notificacao como lida (troque 1 pelo ID da notificacao)
    curl -X PATCH http://127.0.0.1:8001/api/notificacoes/1/lida/ \
         -H "X-Api-Key: SEU_HASH_AQUI" \
         -H "X-User-Id: 1"
    
    # 5. Criar mais uma notificacao via API (simulando outro sistema)
    curl -X POST http://127.0.0.1:8001/api/notificacoes/criar/ \
         -H "X-Api-Key: SEU_HASH_AQUI" \
         -H "Content-Type: application/json" \
         -d '{
                "user_id": 1, 
                "title": "Nova Notificação", 
                "message": "Voce tem uma nova tarefa pendente!"
            }'
    ```
  
* ``OBS: Todos os testes vistos aqui pode ser realizados na página admin do Django.``
   


