import streamlit as st 

# Trabalhando com textos simples (text)
st.text('Olá, este é um texto simples em Streamlit')

nome = 'Jose'

st.text(f'Boa tarde, {nome}')

# Outros elementos textuais
    ## title
st.title('Este é um título')
st.title(':blue[Este é um título azul]')
st.title(':blue[Este é um título azul] estiloso :sunglasses:')

    ## header
st.header('Este é um cabeçalho. :green[Valem as mesmas regras]')
    
    ## subheader
st.subheader(':red[Os sub-cabeçalhos também são importantes]')
    
    ## markdown
st. markdown('Este é um texto em markdown')
st.markdown(f'Este é um texto :green[estiloso] :sunglasses: em markdown para :orange[{nome}]')
    
    ## write (superfunction)
        ### texto normal 
st.write('Texto normal com a função "st.write()".')
    
        ### texto com ênfase em código
st.write('Texto com a função `st.write` enfatizada em código.')
        ### texto markdown
st.write('### Este é um texto em markdown com a função "st.write()"')
    
        ### texto com expressões
st.write(f'`Este texto foi feito com a função "st.write()" e é referente à expressão 3 + 1 = {3+1}`')
    
        ### escrevendo escopos de objetos
st.write(dir(st)) 

# Mensagens de alerta
    ## info
st.info('Este é um texto de informações')

    ## warning
st.warning('Este é um texto de alerta')
    
    ## error
st.error('Este é um texto de erro')

    ## exception
erro = ImportError('Esta é uma exceção de erro de importação de módulos Python')
st.exception(erro)

# pedindo ajuda
st.help(print)