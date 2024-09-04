import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()
Faker.seed(0)
np.random.seed(0)

df = pd.read_csv('dados_acoes.csv')

df['Low'] = df['Low'].str.replace('R$', '').str.replace('$', '').str.replace('€', '').str.replace(',', '.').astype(float)
df['High'] = df['High'].str.replace('R$', '').str.replace('$', '').str.replace('€', '').str.replace(',', '.').astype(float)

num_users = 500
users = [fake.name() for _ in range(num_users)]

# Prepara a estrutura para as transações
transactions = []
purchase_records = {user: {} for user in users}  # Para rastrear compras

# Itera sobre os usuários
for user in users:
    num_transactions = random.randint(5, 100)
    
    for _ in range(num_transactions):
        # Escolhe um dia aleatório e um ticker
        row = df.sample().iloc[0]
        date = row['Date']
        ticker = row['Ticker']
        low = row['Low']
        high = row['High']
        sigla = str(row['Open']).split(" ")[0]

        transaction_type = random.choice(['buy', 'sell'])
        
        if transaction_type == 'buy':
            
            price = np.random.uniform(low, high)
            quantity = np.random.randint(1, 100)
            
            if ticker not in purchase_records[user]:
                purchase_records[user][ticker] = []
            purchase_records[user][ticker].append((date, price, quantity))
            
            if sigla == "R$":
                final_price = f"{sigla} {price:,.2f}".replace('.', ',')
            else:
                final_price = f"{sigla} {price:,.2f}"

            transactions.append([user, date, ticker, transaction_type, final_price, quantity])
        
        elif transaction_type == 'sell':
            # Verifica se o usuário possui ações para vender
            if ticker in purchase_records[user] and purchase_records[user][ticker]:
                
                price = np.random.uniform(low, high)
                quantity = np.random.randint(1, 100)
                
                # Verifica se a quantidade disponível é suficiente para venda
                total_quantity = sum(q for _, _, q in purchase_records[user][ticker])
                
                if quantity <= total_quantity:
                    quantity = total_quantity

                if sigla == "R$":
                    final_price = f"{sigla} {price:,.2f}".replace('.', ',')
                else:
                    final_price = f"{sigla} {price:,.2f}"

                # Adiciona a venda à lista
                transactions.append([user, date, ticker, transaction_type, final_price, quantity])
                
                # Remove a quantidade vendida
                remaining_quantity = quantity
                new_purchases = []
                for purchase_date, purchase_price, purchase_quantity in purchase_records[user][ticker]:
                    if remaining_quantity <= 0:
                        new_purchases.append((purchase_date, purchase_price, purchase_quantity))
                    elif purchase_quantity > remaining_quantity:
                        new_purchases.append((purchase_date, purchase_price, purchase_quantity - remaining_quantity))
                        remaining_quantity = 0
                    else:
                        remaining_quantity -= purchase_quantity
                purchase_records[user][ticker] = new_purchases

transactions_df = pd.DataFrame(transactions, columns=['User', 'Date', 'Ticker', 'TransactionType', 'Price', 'Quantity'])
transactions_df.to_csv('transacoes.csv', index=False)
