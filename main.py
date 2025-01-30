import pandas as pd
import numpy as np

# Carregar os arquivos
extrato_df = pd.read_excel("extrato.ods", engine="odf")
creditos_df = pd.read_csv("creditos.csv", sep="\t", dtype=str)

# Remover espaços extras dos nomes das colunas
creditos_df.columns = creditos_df.columns.str.strip()

# Remover símbolos monetários e formatar valores
creditos_df["Valor Pago"] = (
    creditos_df["Valor Pago"]
    .replace({"R\\$ ": "", "\\.": "", ",": "."}, regex=True)  # Corrigir formato monetário
    .replace("", np.nan)  # Substituir strings vazias por NaN
    .astype(float)  # Converter para float
)

# Converter valores para números
extrato_df["Valor"] = extrato_df["Valor"].replace({"R$ ": "", ".": "", ",": "."}, regex=True).astype(float)
creditos_df["Valor Pago"] = creditos_df["Valor Pago"].replace({"R$ ": "", ".": "", ",": "."}, regex=True).astype(float)

# Lista de valores de depósitos
depositos = extrato_df["Valor"].tolist()
# Lista de valores de créditos
creditos = creditos_df["Valor Pago"].tolist()

# Função para encontrar combinações que somam um alvo usando programação dinâmica (knapsack)
def encontrar_combinacoes_dp(creditos, alvo):
    dp = {0: []}  # Inicializa o dp com a soma 0 e uma lista vazia
    for credito in creditos:
        # Atualiza a tabela dp com as novas somas possíveis
        for soma in list(dp.keys()):
            nova_soma = soma + credito
            if nova_soma <= alvo and nova_soma not in dp:
                dp[nova_soma] = dp[soma] + [credito]
        # Se encontramos uma combinação, podemos interromper a busca
        if alvo in dp:
            return dp[alvo]
    return None

# Verificar para cada valor do extrato
resultado = {}
for deposito in depositos:
    combinacao = encontrar_combinacoes_dp(creditos, deposito)
    if combinacao:
        resultado[deposito] = combinacao

# Exibir os resultados
total_encontrado = sum(resultado.keys())
print(f"Total encontrado: R$ {total_encontrado:.2f}")
for deposito, combinacao in resultado.items():
    print(f"Depósito R$ {deposito:.2f} corresponde à soma dos créditos: {combinacao}")
