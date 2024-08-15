# libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu as om
import io

# page config
st.set_page_config(page_title='NutriClin',
                   page_icon=':bellhop_bell:',
                   layout='wide')

# dataset and other files
def main():

    df = pd.read_excel('./obesity.xlsx')
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()

    photo_url = 'https://images.pexels.com/photos/262978/pexels-photo-262978.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'
    st.sidebar.title(':green[NutriClin]')
    st.sidebar.write(':orange[Saúde para tempo de qualidade]')
    st.sidebar.image(photo_url)

    with st.sidebar:

        opcoes = om('Menu', ['Dados', 'KPIs', 'Plots', 'Sobre'])

    if opcoes == 'Dados':
        st.subheader('Base de Dados')
        with st.expander('Informações gerais sobre os dados', icon='✅'): # :white_check_mark:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write('Visão geral do Dataset')
                st.dataframe(df.head())    
            with col2:
                st.write('Informações Gerais sobre a base de dados')
                st.text(s)
            with col3:
                st.write('Sumário estatístico descritivo')
                st.dataframe(df.describe().T.round(2))

    elif opcoes == 'KPIs':
        st.subheader('Relatório de Desempenho - Agosto 2024')

        with st.expander('Indicadores de Arrecadação', icon='💲'):
            faturamento_total_periodo = df['total_bill'].sum().round(2)
            meta_total_periodo = faturamento_total_periodo * 0.9
            faturamento_medio_diario = round(df['total_bill'].sum() / df['day'].nunique(), 2)
            meta_media_diaria = faturamento_medio_diario * 0.85
            faturamento_por_reserva = round(df['total_bill'].sum() / df.shape[0], 2)
            meta_por_reserva = faturamento_por_reserva * 0.9
            faturamento_por_cliente = round(df['total_bill'].sum() / df['size'].sum(), 2)
            meta_por_cliente = faturamento_por_cliente * 0.85
            
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.metric('Faturamento total no período', value=faturamento_total_periodo,
                        delta=round((faturamento_total_periodo - meta_total_periodo), 2))
                #st.success(f'## US$ {faturamento_total_periodo}')
            with c2:
                st.metric('Faturamento médio diário', value=faturamento_medio_diario,
                        delta=(round((faturamento_medio_diario - meta_media_diaria), 2)))
            with c3: 
                st.metric('Faturamento por reserva', value=faturamento_por_reserva,
                        delta=round((faturamento_por_reserva-meta_por_reserva), 2))
            with c4:
                st.metric('Faturamento por cliente', value=faturamento_por_cliente,
                        delta=round((faturamento_por_cliente - meta_por_cliente), 2))

        with st.expander('Indicadores de Gorjeta', icon='🪙'):
            gorjeta_total_periodo = df['tip'].sum().round(2)
            gorjeta_media_diaria = round(df['tip'].sum() / df['day'].nunique(), 2)
            gorjeta_por_reserva = round(df['tip'].sum() / df.shape[0], 2)
            gorjeta_por_cliente = round(df['tip'].sum() / df['size'].sum(), 2)
            
            c5, c6, c7, c8 = st.columns(4)
            with c5:
                st.metric('Total de gorjetas do período', value=gorjeta_total_periodo)
            with c6:
                st.metric('Média de gorjetas por dia', value=gorjeta_media_diaria)
            with c7:
                st.metric('Média de gorjetas por mesa reservada', value=gorjeta_por_reserva)
            with c8:
                st.metric('Media de gorjetas por cliente', value=gorjeta_por_cliente)

        with st.expander('Principais insights', icon='💡'):
            maior_publico = df['sex'].mode()[0]
            dia_maior_freq = df['day'].mode()[0]
            horario_maior_freq = df['time'].mode()[0]
            mesa_mais_freq = df['size'].mode()[0]

            c9, c10, c11, c12 = st.columns(4)
            with c9: 
                st.metric('Público que mais frequenta', value=maior_publico)
            with c10:
                st.metric('Dia mais frequentado', value=dia_maior_freq)
            with c11:
                st.metric('Horário mais frequentado', value=horario_maior_freq)
            with c12:
                st.metric('Mesa mais reservada', value=mesa_mais_freq)

    elif opcoes == 'Plots':
        st.subheader('Visualizações')
        with st.expander('Distribuição dos clientes categoricas (Conta)', icon='📊'):
            ax = sns.catplot(data=df, x='sex', y='total_bill', row='smoker', col='day',
            hue='size', kind='box', palette='Set1')
            st.pyplot(ax, use_container_width=True)

        with st.expander('Distribuição dos clientes categoricas (Gorjeta)', icon='🪙'):
            ax = sns.catplot(data=df, x='sex', y='tip', row='smoker', col='day',
            hue='size', kind='box', palette='Set1')
            st.pyplot(ax, use_container_width=True)

        with st.expander('Análise da relação entre variáveis numéricas', icon='📈'):
            
            corr_vars_total = df[['total_bill', 'tip']].corr().iloc[0, 1].round(4)
            r2_vars_total = round(corr_vars_total **2, 4)
            
            corr_vars_male = df.loc[df['sex'] == 'Male'][['total_bill', 'tip']].corr().iloc[0, 1].round(4)
            r2_vars_male = round(corr_vars_male ** 2, 4)

            corr_vars_female = df.loc[df['sex'] == 'Female'][['total_bill', 'tip']].corr().iloc[0, 1].round(4)
            r2_vars_female = round(corr_vars_female ** 2, 4)

            c13, c14, c15 = st.columns(3)
            with c13:
                f, ax = plt.subplots()
                ax = sns.regplot(data=df, x='total_bill', y='tip',
                                 scatter_kws={'color':'black', 'alpha':0.4},
                                 line_kws={'color':'black'}, label='Geral')
                plt.title(f'Relação entre conta e gorjeta - Geral \n R²={r2_vars_total}')
                plt.xlim(right=60)
                plt.ylim(top=12)
                plt.legend()
                st.pyplot(f, use_container_width=True)

            with c14:
                f, ax = plt.subplots()
                ax = sns.regplot(data=df[df['sex'] == 'Male'],
                x='total_bill', y='tip', 
                label='Masculino', scatter_kws={'color':'dodgerblue', 'alpha':0.7},
                line_kws={'color':'black', 'ls': '--'})
                plt.title(
                    f'Relação entre conta e gorjeta - Masculino \n R²={r2_vars_male}')
                plt.legend()
                plt.xlim(right=60)
                plt.ylim(top=12)
                st.pyplot(f, use_container_width=True)
            
            with c15:
                f, ax = plt.subplots()
                ax = sns.regplot(data=df[df['sex'] == 'Female'],
                x='total_bill', y='tip', 
                label='Feminino', scatter_kws={'color':'darkorange', 'alpha':0.7},
                line_kws={'color':'black', 'ls': '--'})
                plt.title(
                    f'Relação entre conta e gorjeta - Feminino \n R²={r2_vars_female}')
                plt.legend()
                plt.xlim(right=60)
                plt.ylim(top=12)
                st.pyplot(f, use_container_width=True)

    elif opcoes == 'Sobre':
        st.subheader('Informações complementares')
    
if __name__ == '__main__':
    main()    