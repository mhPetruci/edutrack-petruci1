import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard", page_icon="📊")
st.title("📊 Dashboard Analítico")
st.write("Acompanhe o seu progresso geral de estudos.")

st.divider() # Linha para separar

# --- 🚀 AQUI ESTÃO AS SUAS MÉTRICAS NOVAS ---
st.subheader("Visão Geral")
col1, col2 = st.columns(2)
col1.metric(label="Disciplinas Cadastradas", value="5", delta="2 novas")
col2.metric(label="Tarefas Pendentes", value="12", delta="-3", delta_color="inverse")

st.divider() # Outra linha para separar

# Recuperar disciplinas do st.session_state (simulação)
disciplinas = st.session_state.get("disciplinas", [])

if not disciplinas:
    st.info("Cadastre disciplinas para ver o gráfico!")
else:
    df = pd.DataFrame(disciplinas)
    st.subheader("Disciplinas por Dia da Semana")
    contagem_dias = df['Dia'].value_counts()
    st.bar_chart(contagem_dias)