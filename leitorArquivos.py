import streamlit as st
from json import loads
from pandas import read_csv

st.markdown('''
# Exibidor de Arquivos
## Suba um arquivo e veja o que acontece
''')

arquivo = st.file_uploader(
    'Suba seu arquivo aqui!',
    type=['jpg', 'png', 'py', 'mp3', 'json', 'csv', 'mp4']
)

if arquivo:
    print(arquivo.type)
    match arquivo.type.split('/'):
        case 'application', 'json':
            st.jason(loads(arquivo.read()))
        case 'image', _:
            st.image(arquivo)
        case 'text', 'csv':
            df = read_csv(arquivo)
            st.dataframe(df)
            st.bar_chart(df)
        case 'text', 'x-python':
            st.code(arquivo.read().decode())
        case 'audio', _:
            st.audio(arquivo)
        case 'video', _:
            st.video(arquivo)
else:
    st.error('Nenhum arquivo carregado!')