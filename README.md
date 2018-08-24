# Projeto Interdisciplinar 6º Semestre

## Membros:

- Kauan Alves <br />
- Bruno Silva <br />
- Diogo Silva <br />
- Lucas Lima <br />
- Lucas Borges <br />

## Funcionalidades:
 * Criação da base de dados [X] <br />
 * Criar login [ ] <br />
 * Criar cadastro para hospedes inexistentes [ ] <br />
 * Check-in dos hospedes [ ] <br />
 * Check-out dos hospedes [ ] <br />
 * Cadastro de novos pedidos [ ] <br />
 * Fechamento de caixa [ ] <br />
 * Chat de atendimento (se der tempo) [ ] <br />
 * Implementação com mobile [ ] <br />

## Docker:

### Limpar ambiente postgres

```sh
docker stop $(docker ps -q -a)
docker rm -f $(docker ps -q -a)
docker volume prune -f
docker rmi -f $(docker images -q -a)
```

### Criar container postgres

```sh
docker build . -t sistema_hotel
docker run -p 5432:5432 --name="sistema_hotel" -v local_hotel:/var/lib/postgresql/data sistema_hotel
```

### Comandos para o banco de dados (Após a criação do container)

#### Para executar as migrações (Criar tabelas)
```sh
python migrations.py db init
python migrations.py db migrate
python migrations.py db upgrade
```

#### Para inserir os dados iniciais 
```sh
python manage.py insertions
```

#### Para iniciar o servidor 
```sh
python manage.py runserver
```
