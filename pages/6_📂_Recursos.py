import streamlit as st

st.set_page_config(page_title="Recursos", page_icon="📂")
st.title("📂 Central de Materiais")
st.write("Guarde seus links, referências e arquivos de estudo em um só lugar.")

st.divider()

col_links, col_arquivos = st.columns(2)

with col_links:
    st.subheader("🔗 Links Úteis")
    st.link_button("Acessar Documentação do Streamlit", "https://docs.streamlit.io/")
    st.link_button("Portal do Aluno", "https://google.com")
    st.link_button("Canal de Dicas de Python (YouTube)", "https://youtube.com")

with col_arquivos:
    st.subheader("📄 Meus Arquivos")
    
    # Widget para fazer upload de arquivos
    arquivo = st.file_uploader("Fazer upload de resumo ou PDF", type=["pdf", "docx", "txt", "png"])
    
    if arquivo is not None:
        st.success(f"Arquivo '{arquivo.name}' recebido com sucesso!")
        # Em um sistema real, aqui você usaria código para salvar o arquivo na sua pasta do PC ou nuvem
        
st.divider()

st.subheader("📚 Biblioteca Recomendada")
# Exibindo um vídeo do YouTube embutido direto na página!
st.video("https://www.youtube.com/watch?v=BSpXCRT3w4M") # Vídeo genérico de introdução ao Streamlit