# Importing libraries
import streamlit as st
from io import StringIO

# Setting page details
st.set_page_config(page_title='Traduton',
                    page_icon='https://cdn-icons-png.flaticon.com/512/1372/1372756.png',
                    layout="wide",
                    menu_items={
                        'Get Help': None,
                        'Report a bug': None,
                        'About': '''
                        
                        
                        Made by Yago Gomes de Moraes'''
                    }
                    )

# Hiding "Made with Streamlit"
hide_streamlit_style = """<style>#MainMenu {visibility: show;}footer {visibility: hidden;}</style>"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Translating the file
def converter_programacao(linhas,nome_arquivo):

    serie = nome_arquivo[nome_arquivo.find('_')+len('_'):nome_arquivo.rfind('_')]
    mensagem_inicial = 'Segue a programação para a série '+ str(serie) +':\n'
    linha_senha = 'Senha = '+linhas[0].replace('E ',' / ').replace('E','')
    programacao_serie = ''

    for linha in linhas[1:]:
        numero_antes_do_ponto = linha.replace('EE ','.').split('.')[0]
        nova_linha = linha.replace('EE ','.').replace('E#',' = ').replace('EE','').replace('E E','').replace('#','00 = ').replace('E','\n'+str(numero_antes_do_ponto)+'.')
        for algarismo in range(10):
            nova_linha = nova_linha.replace('.'+str(algarismo)+' ','.0'+str(algarismo)+' ')
        programacao_serie += nova_linha

    mensagem_final = mensagem_inicial + linha_senha + programacao_serie
    return (mensagem_final)

# Uploading file and retrieving translation
uploaded_file = st.sidebar.file_uploader('')
if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    try:
        st.code(converter_programacao(stringio.readlines(),uploaded_file.name))
    except:
        st.warning('Formato de arquivo não reconhecido.')
