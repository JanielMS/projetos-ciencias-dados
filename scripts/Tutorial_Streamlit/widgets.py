# pacotes principais
import streamlit as st 

# trabalhando com elementos interativos (widgets)
st.title('Trabalhando com elementos interativos (widgets)')

## button

st.code('st.button()')
botao = st.button(label='aperte-me e terá uma surpresa')
if botao:
    st.success('o botao foi apertado kkk :wink:')

## radio
st.code('st.radio()')
opcoes = ['Alegria :joy:', 'Apaixonado :heart_eyes:', 'Neutro :neutral_face:']

radio = st.radio(label='Marque uma opção:',
         options=opcoes)

if radio == opcoes[0]:
        st.success(f'Sua expressao é de {opcoes[0]}')
elif radio == opcoes[1]:
        st.success(f'Sua expressao é de {opcoes[1]}')
else:
        st.success(f'Sua expressao é de {opcoes[2]}')

## toggle
st.code('st.toggle()')
interruptor = st.toggle(label='ativar')
if interruptor:
       st.success('função ativada com sucesso')
else:
       st.warning('ative a função para continuar')

## selectbox
st.code('st.selectbox()')
alternativas = ['Palmeiras', 'Flamengo', 'Gremio', 'Santa Cruz']
times = st.selectbox(label='Escolha seu adversário no PES2024', options=alternativas)
if times == alternativas[0]:
       st.warning('Pensa que tem titulo mundial')
elif times == alternativas[1]:
       st.warning('Flamengo de 1981 foi o melhor time')
elif times == alternativas[2]:
       st.warning('Renato Gaucho na Seleção para conseguir o Hexa!!!')
else:
       st.warning('Melhor time do Nordeste')
       

## multiselect
st.code('st.multiselect()')
lista = ['Areia Branca', 'São Gonçalo', 'João de Deus']
bairros = st.multiselect(label='Selecione os bairros', options=lista, placeholder='Escolha um ou mais bairros')
if bairros:
       st.info(f'Você escolheu o(s) bairro(s) {bairros}')
## checkbox
st.code('st.checkbox()')
permissao = st.checkbox('Li e concordo com os termos do contrato')
if permissao:
       st.success('Termos do contrato aceitos')

## slider
st.text('st.slider()')
score = st.slider(label='Informe seu percentual de sucesso',
                  min_value=0,
                  max_value=100,
                  value=50, step=1)

if score < 50: st.info('Você está abaixo da média')
elif score == 50: st.info('Você está na média')
else: st.info('Você está acima da média')

## number_input
st.text('st.number_input()')
maximo = 10
parcelas = st.number_input(label='Informe o número de parcelas',
                           value=None,
                           min_value=0,
                           max_value=10,
                           step=1,
                           placeholder='Digite o numero aqui')
if parcelas == None:
       pass
elif parcelas == 1:
       st.info(f'A compra será paga em {parcelas} parcela')
elif parcelas > 1:
    st.info(f'O valor da compra será dividido em {parcelas} parcelas')

## date_input
st.text('st.date_input()')
entrada = st.date_input(label='Informe a data de check-in', format='DD/MM/YYYY')

saida = st.date_input(label='Informe a data de check-out', format='DD/MM/YYYY')

estadia = saida - entrada

if estadia is not None:
    st.write(f'Período de hospedagem: {estadia}')

## text_input
st.text('st.text_input()')
texto_entrada = st.text_input(label='Escreva em uma palavra como você está se sentindo hoje?')
if texto_entrada:
       st.write(f'Você escreveu: :blue[{texto_entrada}]')

## text_area
st.text('st.text_area()')
texto = st.text_area('Digite seu texto', placeholder='Escreva aqui')
if texto:
       st.write(f'Seu texto tem :green[{len(texto)}] caracteres')

## expander
st.text('st.expander()')
with st.expander('Clique para ver o que tem aqui dentro'):
       st.write('#### :blue[Temos um grafico de Barras]')
       st.bar_chart({'data':[1, 2, 3, 4, 5, 4, 3, 2, 1]})