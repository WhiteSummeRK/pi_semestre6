# COMANDO PARA CRIAR O CONTAINER:
# sudo docker run -p 5432:5432 --name={NOME_DO_CONTAINER} -v {NOME_PARA_O_VOLUME}:/var/lib/postgresql/data {ID_IMAGEM}

FROM postgres:latest

# ----------//atualiza o sistema//--------------

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y vim

# ----------//cria o usuario e o database do postgres//--------------

ENV POSTGRES_USER pi_fatec
ENV POSTGRES_PASSWORD pi_fatec123
ENV POSTGRES_DB pi_fatec_db

# ----------//inicializa o banco de dados//--------------

USER postgres

RUN initdb && echo "host all all 0.0.0.0/0 trust" >> /var/lib/postgresql/data/pg_hba.conf
