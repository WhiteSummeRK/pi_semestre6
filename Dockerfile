FROM postgres:latest

# ----------//atualiza o sistema//--------------

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y vim && apt-get install lsof

# ----------//cria o usuario e o database do postgres//--------------

ENV POSTGRES_USER pi_fatec
ENV POSTGRES_PASSWORD pi_fatec123
ENV POSTGRES_DB pi_fatec_db

# ----------//inicializa o banco de dados//--------------

USER postgres

RUN initdb && echo "host all all 0.0.0.0/0 trust" >> /var/lib/postgresql/data/pg_hba.conf
