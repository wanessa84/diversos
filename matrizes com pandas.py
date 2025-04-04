import pandas as pd
# Necessario instalar o pacote pandas: pip install pandas

dados = {
    "Nome": ["Alice", "Bob", "Carlos"],
    "Idade": [25, 30, 35],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Curitiba"]
}

df = pd.DataFrame(dados)
print(df)

