import streamlit as st
import requests
import json
from datetime import datetime, timedelta

# Configuração
API_BASE_URL = st.secrets.get("API_BASE_URL", "http://localhost:3000")
st.set_page_config(page_title="EduTrack AI", page_icon="🎓", layout="wide")

# Session state para autenticação
if "token" not in st.session_state:
    st.session_state.token = None
if "user" not in st.session_state:
    st.session_state.user = None

def make_request(method, endpoint, data=None, params=None):
    """Helper para fazer requisições à API"""
    headers = {
        "Content-Type": "application/json",
    }
    if st.session_state.token:
        headers["Authorization"] = f"Bearer {st.session_state.token}"
    
    try:
        url = f"{API_BASE_URL}/{endpoint}"
        if method == "GET":
            response = requests.get(url, params=params, headers=headers, timeout=5)
        elif method == "POST":
            response = requests.post(url, json=data, headers=headers, timeout=5)
        elif method == "PATCH":
            response = requests.patch(url, json=data, headers=headers, timeout=5)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, timeout=5)
        
        response.raise_for_status()
        return response.json() if method != "DELETE" else None
    except requests.exceptions.RequestException as e:
        st.error(f"Erro na requisição: {str(e)}")
        return None

def login_page():
    """Página de login"""
    st.title("🎓 EduTrack AI - Login")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        email = st.text_input("Email", placeholder="seu@email.com")
        password = st.text_input("Senha", type="password", placeholder="Digite sua senha")
        
        if st.button("Entrar", use_container_width=True):
            if email and password:
                result = make_request("POST", "auth/login", {"email": email, "password": password})
                if result and "token" in result:
                    st.session_state.token = result["token"]
                    st.session_state.user = result["user"]
                    st.success("Login realizado com sucesso!")
                    st.rerun()
    
    with col2:
        st.markdown("---")
        if st.button("Criar Conta", use_container_width=True):
            st.session_state.show_signup = True
            st.rerun()

def signup_page():
    """Página de cadastro"""
    st.title("🎓 EduTrack AI - Cadastro")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        name = st.text_input("Nome", placeholder="Seu nome completo")
        email = st.text_input("Email", placeholder="seu@email.com")
        password = st.text_input("Senha", type="password", placeholder="Mínimo 6 caracteres")
        password_confirm = st.text_input("Confirmar Senha", type="password")
        
        if st.button("Criar Conta", use_container_width=True):
            if not name or not email or not password:
                st.error("Preencha todos os campos!")
            elif password != password_confirm:
                st.error("Senhas não conferem!")
            elif len(password) < 6:
                st.error("Senha deve ter no mínimo 6 caracteres!")
            else:
                result = make_request("POST", "auth/signup", {
                    "name": name,
                    "email": email,
                    "password": password
                })
                if result and "token" in result:
                    st.session_state.token = result["token"]
                    st.session_state.user = result["user"]
                    st.success("Conta criada com sucesso!")
                    st.session_state.show_signup = False
                    st.rerun()
    
    with col2:
        if st.button("Voltar", use_container_width=True):
            st.session_state.show_signup = False
            st.rerun()

def main_app():
    """Aplicação principal após login"""
    st.sidebar.title(f"👤 {st.session_state.user['name'] or st.session_state.user['email']}")
    
    menu = st.sidebar.radio("Menu", [
        "📊 Dashboard",
        "📚 Disciplinas",
        "📝 Tarefas",
        "👤 Perfil",
        "🚪 Logout"
    ])
    
    if menu == "📊 Dashboard":
        dashboard_page()
    elif menu == "📚 Disciplinas":
        subjects_page()
    elif menu == "📝 Tarefas":
        tasks_page()
    elif menu == "👤 Perfil":
        profile_page()
    elif menu == "🚪 Logout":
        st.session_state.token = None
        st.session_state.user = None
        st.session_state.show_signup = False
        st.success("Logout realizado!")
        st.rerun()

def dashboard_page():
    """Página de dashboard com métricas reais"""
    st.title("📊 Dashboard")
    
    # Buscar dados da API
    subjects_response = make_request("GET", "subjects")
    tasks_response = make_request("GET", "tasks")
    stats_response = make_request("GET", "tasks/stats")
    
    subjects = subjects_response if subjects_response else []
    tasks = tasks_response if tasks_response else []
    stats = stats_response if stats_response else {"pending": 0, "overdue": 0}
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📚 Disciplinas Ativas", len([s for s in subjects if s.get("status") == "active"]))
    col2.metric("📋 Tarefas Pendentes", stats.get("pending", 0))
    col3.metric("⚠️ Tarefas Atrasadas", stats.get("overdue", 0))
    
    completed = len([t for t in tasks if t.get("status") == "completed"])
    total = len(tasks)
    progress = (completed / total * 100) if total > 0 else 0
    col4.metric("✅ Progresso", f"{progress:.0f}%")
    
    st.markdown("---")
    
    # Próximas tarefas
    st.subheader("📌 Próximas Tarefas")
    if tasks:
        upcoming = sorted(tasks, key=lambda t: t.get("due_date", ""))[:5]
        for task in upcoming:
            if task.get("status") != "completed":
                due_date = datetime.fromisoformat(task.get("due_date", "")).strftime("%d/%m/%Y")
                priority_color = "🔴" if task.get("priority") == "high" else "🟡" if task.get("priority") == "medium" else "🟢"
                st.write(f"{priority_color} **{task.get('title')}** - Vencimento: {due_date}")
    else:
        st.info("Nenhuma tarefa cadastrada!")

def subjects_page():
    """Página de disciplinas"""
    st.title("📚 Minhas Disciplinas")
    
    tab1, tab2 = st.tabs(["📋 Listar", "➕ Nova"])
    
    with tab2:
        st.subheader("Cadastrar Nova Disciplina")
        with st.form("form_subject"):
            name = st.text_input("Nome da Disciplina")
            code = st.text_input("Código")
            professor = st.text_input("Professor")
            semester = st.text_input("Semestre", placeholder="ex: 2024.1")
            credits = st.number_input("Créditos", min_value=0, max_value=20, value=4)
            description = st.text_area("Descrição")
            
            if st.form_submit_button("Salvar"):
                if name:
                    result = make_request("POST", "subjects", {
                        "name": name,
                        "code": code,
                        "professor": professor,
                        "semester": semester,
                        "credits": credits,
                        "description": description
                    })
                    if result:
                        st.success("Disciplina cadastrada!")
                        st.rerun()
                else:
                    st.error("Nome é obrigatório!")
    
    with tab1:
        st.subheader("Suas Disciplinas")
        subjects = make_request("GET", "subjects")
        
        if subjects:
            for subject in subjects:
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.write(f"**{subject.get('name')}**")
                    if subject.get('code'):
                        st.caption(f"Código: {subject.get('code')}")
                    if subject.get('description'):
                        st.caption(subject.get('description'))
                
                with col2:
                    if st.button("✏️", key=f"edit_{subject['id']}"):
                        st.session_state.edit_subject_id = subject['id']
                    if st.button("🗑️", key=f"delete_{subject['id']}"):
                        make_request("DELETE", f"subjects/{subject['id']}")
                        st.success("Disciplina removida!")
                        st.rerun()
        else:
            st.info("Nenhuma disciplina cadastrada! Crie uma nova para começar.")

def tasks_page():
    """Página de tarefas"""
    st.title("📝 Minhas Tarefas")
    
    tab1, tab2 = st.tabs(["📋 Listar", "➕ Nova"])
    
    with tab2:
        st.subheader("Cadastrar Nova Tarefa")
        subjects = make_request("GET", "subjects")
        subject_names = {s['id']: s['name'] for s in subjects} if subjects else {}
        
        with st.form("form_task"):
            subject_id = st.selectbox("Disciplina", options=list(subject_names.keys()), format_func=lambda x: subject_names.get(x, ""))
            title = st.text_input("Título da Tarefa")
            description = st.text_area("Descrição")
            due_date = st.date_input("Prazo", value=datetime.now() + timedelta(days=7))
            priority = st.selectbox("Prioridade", ["low", "medium", "high"], format_func=lambda x: "Baixa" if x == "low" else "Média" if x == "medium" else "Alta")
            
            if st.form_submit_button("Salvar"):
                if title and subject_id:
                    result = make_request("POST", "tasks", {
                        "subject_id": subject_id,
                        "title": title,
                        "description": description,
                        "due_date": due_date.isoformat(),
                        "priority": priority
                    })
                    if result:
                        st.success("Tarefa criada!")
                        st.rerun()
                else:
                    st.error("Título e Disciplina são obrigatórios!")
    
    with tab1:
        st.subheader("Suas Tarefas")
        tasks = make_request("GET", "tasks")
        
        if tasks:
            status_filter = st.selectbox("Filtrar por Status", ["Todas", "pending", "in_progress", "completed"])
            
            filtered = tasks if status_filter == "Todas" else [t for t in tasks if t.get('status') == status_filter]
            
            for task in sorted(filtered, key=lambda t: t.get('due_date', '')):
                col1, col2 = st.columns([4, 1])
                with col1:
                    due_date = datetime.fromisoformat(task.get('due_date', '')).strftime("%d/%m/%Y")
                    priority_icon = "🔴" if task.get('priority') == 'high' else "🟡" if task.get('priority') == 'medium' else "🟢"
                    status_icon = "✅" if task.get('status') == 'completed' else "⏳" if task.get('status') == 'in_progress' else "❌"
                    
                    st.write(f"{status_icon} {priority_icon} **{task.get('title')}** - {due_date}")
                
                with col2:
                    if st.button("✏️", key=f"edit_task_{task['id']}"):
                        st.session_state.edit_task_id = task['id']
                    if st.button("🗑️", key=f"delete_task_{task['id']}"):
                        make_request("DELETE", f"tasks/{task['id']}")
                        st.success("Tarefa removida!")
                        st.rerun()
        else:
            st.info("Nenhuma tarefa cadastrada! Crie uma nova.")

def profile_page():
    """Página de perfil do usuário"""
    st.title("👤 Meu Perfil")
    
    user = st.session_state.user
    
    with st.form("form_profile"):
        name = st.text_input("Nome", value=user.get('name', ''))
        email = st.text_input("Email", value=user.get('email', ''), disabled=True)
        created_at = datetime.fromisoformat(user.get('created_at', '')).strftime("%d/%m/%Y")
        st.caption(f"Membro desde: {created_at}")
        
        if st.form_submit_button("Atualizar Perfil"):
            result = make_request("PATCH", "auth/profile", {"name": name})
            if result:
                st.session_state.user = result
                st.success("Perfil atualizado!")
                st.rerun()

# Lógica principal
if __name__ == "__main__":
    if not st.session_state.token:
        if st.session_state.get("show_signup", False):
            signup_page()
        else:
            login_page()
    else:
        main_app()