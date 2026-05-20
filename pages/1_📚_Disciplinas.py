import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Disciplinas", page_icon="📚")
st.title("Gestão de Disciplinas")

# Pega a URL do Xano configurada no secrets.toml
# Substitua "/academic_tasks" se o endpoint no seu Xano tiver outro nome
API_URL = st.secrets["API_BASE_URL"].rstrip("/") + "/academic_tasks"

# --- FUNÇÕES PARA COMUNICAR COM O XANO ---
def carregar_disciplinas_do_xano():
    try:
        resposta = requests.get(API_URL)
        if resposta.status_code == 200:
            return resposta.json() # Retorna a lista de registros do Xano
        else:
            st.error("Erro ao carregar dados do Xano.")
            return []
    except Exception as e:
        st.error(f"Erro de conexão: {e}")
        return []

def salvar_disciplina_no_xano(nome, professor, dia):
    # Formato dos dados que o Xano espera receber
    dados = {
        "title": nome,
        "Professor": professor,
        "Dia": dia,
        "due_date": None   # <-- Tiramos as aspas e colocamos None
    }
    try:
        resposta = requests.post(API_URL, json=dados)
        if resposta.status_code == 200 or resposta.status_code == 201:
            return True
        else:
            st.error(f"Erro ao salvar: {resposta.text}")
            return False
    except Exception as e:
        st.error(f"Erro de conexão ao salvar: {e}")
        return False

# Abas para separar Listagem e Cadastro
tab_lista, tab_novo = st.tabs(["📄 Listar", "➕ Nova Disciplina"])

with tab_novo:
    st.subheader("Cadastrar Nova Matéria")

    with st.form("form_disciplina", clear_on_submit=True):
        nome = st.text_input("Nome da Disciplina")
        professor = st.text_input("Nome do Professor")
        dia_semana = st.selectbox("Dia da Aula", ["Seg", "Ter", "Qua", "Qui", "Sex"])
        submitted = st.form_submit_button("Guardar")

    if submitted:
        if nome != "" and professor != "":
            # ... (seu código que salva a disciplina) ...
            
            st.success(f"Disciplina '{nome}' cadastrada com sucesso!")
            
            # --- 🚀 COLOQUE OS ENFEITES AQUI ---
            st.toast('Sua disciplina foi salva com sucesso!', icon='🎉')
            st.balloons() 
            # -----------------------------------
            
        else:
            st.warning("Por favor, preencha o nome da disciplina e o professor.")

with tab_lista:
    st.info("Conectado ao Banco de Dados Xano! ☁️")
    
    # Carrega os dados sempre fresquinhos do Xano
    dados_xano = carregar_disciplinas_do_xano()
    
    if dados_xano:
        # Se os dados no Xano tiverem colunas extras (como id, created_at), 
        # o Pandas mostra tudo. Depois podemos filtrar se preferir.
        df = pd.DataFrame(dados_xano)
        st.dataframe(df, use_container_width=True)
    else:
        st.write("Nenhuma disciplina cadastrada no banco de dados ainda.")