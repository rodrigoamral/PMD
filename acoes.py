import numpy as np
import pandas as pd
import mplfinance as mpf
from datetime import datetime, timedelta

# Função para gerar dados realistas de uma ação
def gerar_dados_acao(data_inicio, preco_inicial, ticker, sigla_preco):
    data_atual = datetime.now()
    num_dias = (data_atual - data_inicio).days
    
    datas = []
    
    for i in range(num_dias):
        data = data_inicio + timedelta(days=i)
        
        if sigla_preco == "R$":
            data_formatada = data.strftime("%d/%m/%Y")
        else:
            data_formatada = data.strftime("%Y-%m-%d")
        
        datas.append(data_formatada)
    
    dados = []
    preco_fechamento_anterior = preco_inicial
    for _ in range(num_dias):
        preco_abertura = preco_fechamento_anterior
        preco_fechamento = preco_abertura + np.random.uniform(-0.01 * preco_abertura, 0.01 * preco_abertura)
        
        if(preco_abertura > preco_fechamento):
            max = preco_abertura
            min = preco_fechamento
        else:
            max = preco_fechamento
            min = preco_abertura

        variacao = np.random.uniform(-0.02 * preco_abertura, 0.02 * preco_abertura)
        preco_maximo = max + variacao
        preco_minimo = min - variacao
        
        if sigla_preco == "R$":
            dados.append([f"{sigla_preco} {preco_abertura:,.2f}".replace('.', ','), 
                          f"{sigla_preco} {preco_fechamento:,.2f}".replace('.', ','), 
                          f"{sigla_preco} {preco_maximo:,.2f}".replace('.', ','), 
                          f"{sigla_preco} {preco_minimo:,.2f}".replace('.', ','), 
                          ticker])
        else:
            dados.append([f"{sigla_preco} {preco_abertura:.2f}", 
                          f"{sigla_preco} {preco_fechamento:.2f}", 
                          f"{sigla_preco} {preco_maximo:.2f}", 
                          f"{sigla_preco} {preco_minimo:.2f}", 
                          ticker])

        preco_fechamento_anterior = preco_fechamento
    
    df = pd.DataFrame(dados, columns=['Open', 'Close', 'High', 'Low', 'Ticker'], index=datas)
    return df

# Configurações
data_inicio = datetime(2020, 1, 1)

# Lista de tickers de ações brasileiras (BR), americanas (EUA) e europeias (EU)
tickers_br = ["PETR4", "VALE3", "ITUB4", "BBDC4", "BBAS3", "ABEV3", "MGLU3", "WEGE3", "RENT3", "EQTL3",
              "VVAR3", "LREN3", "HAPV3", "BRML3", "RAIL3", "SBSP3", "ELET3", "CPLE6", "CMIG4", "USIM5",
              "GGBR4", "ENBR3", "B3SA3", "BRKM5", "GNDI3", "CIEL3", "CSAN3", "HYPE3", "PRIO3", "SUZB3"]

tickers_eua = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NFLX", "NVDA", "AMD", "INTC",
               "JNJ", "XOM", "JPM", "DIS", "BA", "V", "MA", "PYPL", "ADBE", "CRM"]

tickers_eu = [ "SIE.DE", "MC.PA", "VOW.DE", "NESN.S", "SAP.DE", "ULVR.L", "TTE.PA", "ALV.DE", 
              "SAN.MC", "AZN.L", "BNP.PA", "GSK.L", "DAI.DE", "HEIA.AS", "AIR.PA"]

# Gerar dados para todas as ações com preço inicial aleatório
dfs = []
for ticker in tickers_br:
    preco_inicial = np.random.uniform(50, 150)
    df_acao = gerar_dados_acao(data_inicio, preco_inicial, ticker, "R$")
    dfs.append(df_acao)

for ticker in tickers_eua:
    preco_inicial = np.random.uniform(50, 150)
    df_acao = gerar_dados_acao(data_inicio, preco_inicial, ticker, "$")
    dfs.append(df_acao)

    
for ticker in tickers_eu:
    preco_inicial = np.random.uniform(50, 150)
    df_acao = gerar_dados_acao(data_inicio, preco_inicial, ticker, "€")
    dfs.append(df_acao)

df_total = pd.concat(dfs)

df_total.reset_index(inplace=True)
df_total.rename(columns={'index': 'Date'}, inplace=True)

arquivo_csv = "dados_acoes.csv"
df_total.to_csv(arquivo_csv, index=False)

print(df_total.head())

# Plotar o gráfico de velas
acao_para_plotar = "AAPL"
df_plot = df_total[df_total['Ticker'] == acao_para_plotar]

df_candle = df_plot.copy()
df_candle['Open'] = df_candle['Open'].str.replace('[R$ ]', '', regex=True).replace('[€ ]', '', regex=True).astype(float)
df_candle['Close'] = df_candle['Close'].str.replace('[R$ ]', '', regex=True).replace('[€ ]', '', regex=True).astype(float)
df_candle['High'] = df_candle['High'].str.replace('[R$ ]', '', regex=True).replace('[€ ]', '', regex=True).astype(float)
df_candle['Low'] = df_candle['Low'].str.replace('[R$ ]', '', regex=True).replace('[€ ]', '', regex=True).astype(float)
df_candle.set_index('Date', inplace=True)

mpf.plot(df_candle[['Open', 'High', 'Low', 'Close']], type='candle', style='charles', title=f'Gráfico de Velas - {acao_para_plotar}', ylabel='Preço (USD)', volume=False)
