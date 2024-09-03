# Projeto Prático PMD2024
## Objetivo : Simular uma aplicação bancária internacional para compra e venda de ações.
## Contexto 
- Sendo um usuário brasileiro, ser possível ter acesso a informações sobre ações brasileiras, americanas e europeias. Assim como ser possível acessar a todo seu histórico de transações relacionadas a compra e venda de ações. 
## Ferramentas utilizadas
- Python
- Apache Spark
- MongoDB

## Requisitos necessário para rodar o projeto
- Python 3.
- Bibliotecas do python : pandas, numpy, faker e random.
- MongoDB.
- Apache Sparky.
- Conector spark-mongodb.

## Ambiente em nuvem
### É possivel executar o projeto utilizando ambiente em nuvem databricks para o apache spark e atlas para o mongodb
- Databricks :
   - Necessário instalar no notebook o conector org.mongodb.spark:mongo-spark-connector_2.12:3.0.1
- Atlas :
   - Necessário liberar acesso ao ip utilizado no databricks ou a qualquer ip que tente acessar.
   - Obter string de conexão para acessar o banco de dados.
## Geração dos dados
- Executar os scripts python "transacoes.py" e "acoes.py" para criar os arquivos em formato csv para informações sobre as ações das empresas e sobre as transações feitas por usuários.

## Notebook
 - O arquivo PMD2024.ipynb é um jupyter notebook contendo todos os códigos executados para o processo de ETL das bases de dados,carga e transformação utilizando spark e suas consultas/consumo através do mongodb.
 - A seguir um resumo sobre cada parte do ETL realizada. 
## Processamento 
