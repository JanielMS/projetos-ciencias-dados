# pacotes principais
import streamlit as st
import pandas as pd
import matplotlib.pyplot as pyplot
import seaborn as sns

# carregamento do dataset iris
df = sns.load_dataset('iris')

# tabela estática
st.table(df.head())
st.table(df.describe().T)

# tabela dinamica
st.dataframe(df)
st.dataframe(df.describe().T)

# adicionando estilos de cores ao dataframe
st.dataframe(df.head().style.background_gradient(cmap='RdYlGn', axis=1))

# exibindo arquivos json
st.json({'chave1': 'valor1',
         'chave2': ['valor2', 'valor3', 'valor4']})

# exibindo texto em formato de código
meu_codigo = """
def OlaMundo(msg: str) -> str:
    return msg
"""

st.code(body=meu_codigo,
        language='python',
        line_numbers=True)

