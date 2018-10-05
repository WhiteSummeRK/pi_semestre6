# Projeto Interdisciplinar 6º Semestre

## Membros:

- Kauan Alves <br />
- Bruno Silva <br />
- Diogo Silva <br />
- Lucas Lima <br />
- Lucas Borges <br />

## Funcionalidades:
 * Criação da base de dados [X] <br />
 * Criar login [X] <br />
 * Criar cadastro para hospedes inexistentes [X] <br />
 * Check-in dos hospedes [ ] <br />
 * Check-out dos hospedes [ ] <br />
 * Cadastro de novos pedidos [ ] <br />
 * Fechamento de caixa [ ] <br />
 * Chat de atendimento (se der tempo) [ ] <br />
 * Implementação com mobile [ ] <br />

## Como Iniciar a Aplicação:

Antes de tudo, você deve instalar as dependencias do projeto, sugere-se criar um ambiente virtual antes, para isso execute o comando de instalação do pipenv:
```sh
pip install pipenv
```
Apos isso, vá até a pasta raiz do projeto e execute
```sh
pipenv shell
```
Enfim, execute a instalação das dependencias:
```sh
pip install -r requirements.txt
```


### Limpar ambiente postgres

```sh
docker stop $(docker ps -q -a)
docker rm -f $(docker ps -q -a)
docker volume prune -f
docker rmi -f $(docker images -q -a)
```

### Realizar o build da imagem do docker

```sh
docker build . -t sistema_hotel
```

### Criar o container
```sh
docker run -p 5432:5432 --name="sistema_hotel" -v local_hotel:/var/lib/postgresql/data sistema_hotel
```

### Comandos para o banco de dados (Após a criação do container)

#### Para executar as migrações (Criar tabelas)
```sh
python migrations.py db init
python migrations.py db migrate
python migrations.py db upgrade
```
O comando "python migrations.py db init" poderá disparar um erro dizendo que a pasta migrations ja existe no projeto. caso haja alguma mudança nas tabelas do banco de dados, sugere-se excluir essa pasta e executar os comandos novamente... caso contrário, pode-se ignorar esse erro.

#### Para inserir os dados iniciais no BD
```sh
python manage.py insertions
```

#### Para iniciar o servidor
```sh
python manage.py runserver
```
