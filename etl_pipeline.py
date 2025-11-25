import pandas as pd
import sqlite3

print("Lendo o arquivo CSV...")
df = pd.read_csv('vendas.csv')

#Analisar os dados iniciais
print("--- Tipos de Dados Originais ---")
print(df.info())
print("\n--- Amostra do Caos ---")
print(df.head())

#Arrumando a Coluna "valor_venda"
print("Limpando valores...")
df['valor_venda'] = df['valor_venda'].astype(str)

df['valor_venda'] = df['valor_venda'].str.replace('R$', '', regex=False)
df['valor_venda'] = df['valor_venda'].str.replace(',','.', regex=False)

df['valor_venda'] = pd.to_numeric(df['valor_venda'], errors='coerce')

print(df['valor_venda'])

#Arrumando a coluna "data_venda"
print("Limpando datas...")
df['data_venda'] = pd.to_datetime(df['data_venda'], dayfirst=True, format='mixed', errors='coerce')
print(df['data_venda'])

#Limpando dados Duplicados
print("Removendo Duplicatas")
print(f"Linhas Atuais: {len(df)}")
df = df.drop_duplicates()

print(f"Linhas restantes: {len(df)}")

#Salvando Tudo no Banco de Dados
print("\n--- SALVANDO NO BANCO (LOAD) ---")
conexao = sqlite3.connect('vendas.db')

df.to_sql('vendas_tratadas', conexao, if_exists='replace', index=False)

conexao.close()