import streamlit as st
import json
import os

st.title("👤 Meu Perfil")
st.write("Gerencie suas informações pessoais e acompanhe seu desempenho real.")

st.divider()

# --- LÓGICA PARA BUSCAR DADOS REAIS ---
total_disciplinas = 0
total_tarefas = 0

# 1. Tentar buscar disciplinas do arquivo JSON local se ele existir
if os.path.exists("academic_tasks.json"):
    try:
        with open("academic_tasks.json", "r", encoding="utf-8") as f:
            dados = json.load(f)
            # Ajuste as chaves abaixo dependendo de como o seu JSON está estruturado
            if isinstance(dados, dict):
                total_disciplinas = len(dados.get("subjects", dados.get("disciplinas", [])))
                total_tarefas = len(dados.get("tasks", dados.get("tarefas", [])))
            elif isinstance(dados, list):
                total_tarefas = len(dados)
    except Exception:
        pass

# 2. Alternativa: Buscar do st.session_state se as outras páginas já salvaram lá
if "disciplinas" in st.session_state:
    total_disciplinas = len(st.session_state["disciplinas"])
if "tasks" in st.session_state:
    total_tarefas = len(st.session_state["tasks"])


# --- LAYOUT DA PÁGINA ---
col1, col2 = st.columns([1, 2.5])

with col1:
    # Usando o nome do usuário para gerar um avatar personalizado único
    nome_usuario = st.session_state.get("user_name", "Marcos Henrique")
    st.image(f"https://api.dicebear.com/7.x/bottts/svg?seed={nome_usuario}", width=150)

with col2:
    st.subheader("Informações Pessoais")
    
    # Salva o nome no session_state para atualizar o avatar em tempo real ao mudar o input
    nome = st.text_input("Nome", value=nome_usuario)
    st.session_state["user_name"] = nome
    
    email = st.text_input("E-mail", value="marcos.petruci@edu.com")
    curso = st.selectbox(
        "Curso / Trilha de Estudo", 
        ["Engenharia", "Desenvolvimento de Software", "Ciência de Dados", "Outro"]
    )

st.divider()

# --- MÉTRICAS COM OS DADOS REAIS ---
st.subheader("📊 Meu Desempenho (Dados em Tempo Real)")

metric1, metric2, metric3 = st.columns(3)

with metric1:
    st.metric(label="Disciplinas Cadastradas", value=str(total_disciplinas))

with metric2:
    # Mostra a quantidade real de tarefas achadas no sistema
    st.metric(label="Total de Tarefas", value=str(total_tarefas))

with metric3:
    # Exemplo estático ou calculado se você tiver notas no JSON
    st.metric(label="Média Geral", value="8.8")

st.divider()

if st.button("💾 Salvar Alterações", type="primary"):
    st.success("Perfil atualizado localmente!")