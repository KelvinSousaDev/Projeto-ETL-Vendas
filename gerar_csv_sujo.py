import pandas as pd

# Simulando dados SUJOS de um sistema legado
dados = {
    'id_transacao': [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 11, 12], #ID 6 repetido
    'data_venda': [
        '2025-01-01', '2025-01-02', '03/01/2025', '2025-01-04', # Formatos misturados
        None, '2025-01-06', '2025-01-06', '2025-01-07', '2025-01-08',
        '2025-01-09', 'Data Inválida', '2025-01-11', '2025-01-12'
    ],
    'nome_produto': [
        'Notebook', 'Mouse', 'Teclado', 'Monitor', 'Mouse', 
        'Notebook', 'Notebook', 'Cadeira Gamer', 'Headset', 
        'Mouse', 'Teclado', None, 'Webcam' # Produto vazio
    ],
    'valor_venda': [
        '3500.00', '50,00', '150.00', '1200.00', 'R$ 50,00', # Mistura de ponto, vírgula e R$
        '3500.00', '3500.00', '800.00', '250.00', 
        '50.00', '150.00', '100.00', 'texto_errado' # Texto no meio do número
    ],
    'cidade_cliente': [
        'São Paulo', 'Rio de Janeiro', 'São Paulo', 'Curitiba', 'Belo Horizonte',
        'São Paulo', 'São Paulo', 'Curitiba', 'Rio de Janeiro',
        'Sao Paulo', 'São Paulo', 'Curitiba', 'Rio de Janeiro' # 'Sao Paulo' sem acento
    ]
}

df = pd.DataFrame(dados)

df.to_csv('vendas.csv', index=False)

print("Arquivo 'vendas.csv' gerado com sucesso! (E está uma bagunça)")