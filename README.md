# Projeto Prático PMD2024
## Objetivo : Simular uma aplicação bancária internacional para compra e venda de ações.
## Contexto 
- Sendo um usuário brasileiro, ser possível ter acesso a informações sobre ações brasileiras, americanas e europeias. Assim como ser possível acessar a todo seu histórico de transações relacionadas a compra e venda de ações. 
## Ferramentas utilizadas
- Python
- Apache Spark
- MongoDB

## Requisitos necessários para rodar o projeto
- Python versão 3.12. Documentação: https://docs.python.org/3/
- Java versão 8.0. Documentação: https://docs.oracle.com/en/java/
- Bibliotecas do python : pandas, numpy, faker, random e mplfinance.
- MongoDB versão 7.0. Documentação: https://www.mongodb.com/pt-br/docs/manual/
- Apache Sparky versão 3.0. Documentação: https://spark.apache.org/docs/latest/
- Conector spark-mongodb : org.mongodb.spark:mongo-spark-connector_2.12:3.0.1.

## Ambiente em nuvem
### É possivel executar o projeto utilizando ambiente em nuvem databricks para o apache spark e atlas para o mongodb
- Databricks : https://docs.databricks.com/en/index.html
   - Necessário instalar no notebook o conector org.mongodb.spark:mongo-spark-connector_2.12:3.0.1
- Atlas : https://www.mongodb.com/pt-br/docs/atlas/
   - Necessário liberar acesso ao ip utilizado no databricks ou a qualquer ip que tente acessar.
   - Obter string de conexão para acessar o banco de dados.
## Geração dos dados
- Executar os scripts python "transacoes.py" e "acoes.py" para criar os arquivos em formato csv para informações sobre as ações das empresas e sobre as transações feitas por usuários.

## Notebook
 - O arquivo PMD2024.ipynb é um jupyter notebook contendo todos os códigos executados para o processo de ETL das bases de dados, extração através do python, transformações e cargas utilizando spark e suas consultas/consumo através do mongodb.
 - A seguir um resumo sobre cada parte do ETL realizada.
   
## Extração
- Os dados foram criados através de bibliotecas python para simular dados sobre ações e transações de usuários sobre compra e venda de determinadas ações.

## Transformação
- Este processo teve dois pontos principais:
   - Moeda:
      - Normalização dos valores relacionados as ações e transações, como há valores em real, dolar e euro, esta etapa se concentrou na conversão de todos os valores para a moeda real.
      - Neste processo foi utilizado a Awesome API para adquirir os dados sobre taxa de câmbio. Disponivel em : https://docs.awesomeapi.com.br/api-de-moedas
   - Data:
        - Normalização das datas, visto que o formato de data utilizado no Brasil e utilizado tanto nos EUA quanto na Europa são diferentes, esta etapa se concentrou em converter todas as datas para o formato utilizado no Brasil (DD/MM/AAAA).

## Carga
- Após o processamento dos dados, a carga foi feita no MongoDB através do spark utilizando um conector.

## Consultas/Resultados
- Foram criadas duas consultas para serem realizadas no mongodb:
   - 1 : Quanto um determinado usuário lucrou/perdeu vendendo ações?
   - 2 : Quais são as 10 melhores ações em um determinado mês? Levando em consideração o critério para avaliar as ações a variação de preço em porcentagem(sendo a melhor a que teve maior aumento em %) que a ação teve no período determinado.   
