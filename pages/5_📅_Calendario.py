import streamlit as st
import datetime

st.set_page_config(page_title="Calendário", page_icon="📅")
st.title("📅 Cronograma Semanal")
st.write("Organize seus prazos e tarefas importantes.")

st.divider()

# Selecionar uma data
data_selecionada = st.date_input("Selecione uma data para ver os compromissos:", datetime.date.today())

st.subheader(f"Compromissos para {data_selecionada.strftime('%d/%m/%Y')}")

# Simulando tarefas dinâmicas usando st.expander
with st.expander("🔴 Urgente: Entregar Trabalho de Python", expanded=True):
    st.write("**Disciplina:** Python Basics")
    st.write("**Prazo:** 23:59 de hoje")
    st.write("**Detalhes:** Fazer o upload do código no GitHub e enviar o link no portal.")
    if st.button("Marcar como concluído"):
        st.success("Trabalho entregue!")

with st.expander("🟡 Estudar para a Prova: No-Code"):
    st.write("**Disciplina:** No-Code Advanced")
    st.write("**Detalhes:** Revisar o material do Xano e integrações via API.")
    st.button("Iniciar Pomodoro (25 min)")
    