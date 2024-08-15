# bibliotecas
import streamlit as st
import pandas as pd 
import seaborn as sns

# 1. titulo da aula
st.title('Trabalhando com carregamento de arquivos')
st.write('Para mais detalhes, consulte a [página oficial do Stremalit](https://docs.streamlit.io/)')

# 2. carregamento da base de dados built-in da biblioteca Seaborn
df = sns.load_dataset('iris')

# 3. salvando um exemplo de dataset em *.csv
iris_csv = df.head().to_csv('iris.csv', index=False)

# 4. salvando um exemplo de dataset em *.xlsx
iris_xls = df.head().to_excel('iris.xlsx', index=False)

# 5. criando funções para o carregamento de dados
@st.cache_data
def carregar_csv(arquivo):
    tabela = pd.read_csv(arquivo)
    return tabela

@st.cache_data
def carregar_excel(arquivo):
    tabela = pd.read_excel(arquivo)
    return tabela

# carregando arquivos
opcao = st.sidebar.selectbox(label='Selecione o arquivo conforme a extensao', 
                             options=['csv', 'xlsx'])

arquivo = st.file_uploader('Carregue o arquivo')

if arquivo is not None:
    st.write(f'Nome: :blue[{arquivo.name}] | Tipo: :orange[{arquivo.type}] | Tamanho: :green[{arquivo.size}B]')

    if opcao == 'csv':
        iris = carregar_csv(arquivo)
        with st.expander('Clique para visualizar os dados'): 
            st.dataframe(iris)
    elif opcao == 'xlsx':
        iris = carregar_excel(arquivo)
        with st.expander(f'Clique para visualizar os dados'):
            st.dataframe(iris)