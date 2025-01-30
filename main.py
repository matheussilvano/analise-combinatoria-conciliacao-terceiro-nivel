import pandas as pd
import numpy as np
import time

# Registrar o tempo de início
inicio_execucao = time.time()
print("Execução iniciada...")

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

# Lista de valores de depósitos e números de resumo
depositos = extrato_df["Valor"].tolist()
creditos = creditos_df["Valor Pago"].tolist()
resumos_creditos = creditos_df["Nº Resumo"].tolist()

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

# Inicializar contadores
depositos_analizados = 0
depositos_conciliados = 0
depositos_nao_conciliados = 0

# Verificar para cada valor do extrato
resultado = {}
for deposito in depositos:
    print(f"Analisando extrato de R$ {deposito:.2f}...")
    combinacao = encontrar_combinacoes_dp(creditos, deposito)
    depositos_analizados += 1
    if combinacao:
        resultado[deposito] = combinacao
        depositos_conciliados += 1
        # Encontrar o número de resumo correspondente aos créditos conciliados
        creditos_conciliados = [
            f"{credito:.2f} ({resumos_creditos[i]})" for i, credito in enumerate(creditos) if credito in combinacao
        ]
        print(f"Depósito R$ {deposito:.2f} - Encontrados registros congruentes: {', '.join(creditos_conciliados)}")
    else:
        depositos_nao_conciliados += 1
        print(f"Depósito R$ {deposito:.2f} - Não encontrados registros congruentes.")

# Exibir o resumo final
total_encontrado = sum(resultado.keys())
tempo_execucao = time.time() - inicio_execucao

print("\nResumo da execução:")
print(f"Total de depósitos analisados: {depositos_analizados}")
print(f"Total de depósitos conciliados: {depositos_conciliados}")
print(f"Total de depósitos não conciliados: {depositos_nao_conciliados}")
print(f"Total encontrado: R$ {total_encontrado:.2f}")
print(f"Tempo de execução: {tempo_execucao:.2f} segundos.")
