FROM mongodb/mongodb-community-server:latest@sha256:2ecdb05189e8e615e0216ba7bb639459b285ef009d088b6be8d0de643a6c309c

USER root
WORKDIR /home
COPY emplacement-des-gares-idf.csv .
RUN echo "cat emplacement-des-gares-idf.csv | tr ';' '\t' | mongoimport --db mongo_db --collection jeu_des_trains_collections --type tsv --headerline" >> trim.sh
RUN chmod +x trim.sh
RUN groupadd -r common_user && useradd --no-log-init -r -g common_user user
RUN chown -R user /data/db
USER user
RUN chmod -R u+rwx /data/db


