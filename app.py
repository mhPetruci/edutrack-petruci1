import streamlit as st
import requests
import json
from datetime import datetime, timedelta
import pandas as pd
import time

# Configuração da API
API_BASE_URL = st.secrets.get("API_BASE_URL", "http://localhost:3000")

# Configuração com tema customizado
st.set_page_config(
    page_title="EduTrack AI", 
    page_icon="🎓", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Tema customizado
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        margin: 0.5rem 0;
    }
    .welcome-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
    }
    .stButton>button {
        border-radius: 8px;
        font-weight: 500;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px 8px 0 0;
    }
</style>
""", unsafe_allow_html=True)

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
    """Página de login com design atrativo"""
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="color: #667eea; font-size: 3rem; margin-bottom: 0;">🎓 EduTrack AI</h1>
        <p style="color: #666; font-size: 1.2rem;">Seu assistente acadêmico inteligente</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Container centralizado
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div style="background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h2 style="text-align: center; color: #333; margin-bottom: 2rem;">👋 Bem-vindo de volta!</h2>
        </div>
        """, unsafe_allow_html=True)
        
        email = st.text_input("📧 Email", placeholder="seu@email.com", label_visibility="collapsed")
        password = st.text_input("🔒 Senha", type="password", placeholder="Digite sua senha", label_visibility="collapsed")
        
        if st.button("🚀 Entrar", use_container_width=True, type="primary"):
            if email and password:
                with st.spinner("Verificando credenciais..."):
                    result = make_request("POST", "auth/login", {"email": email, "password": password})
                if result and "token" in result:
                    st.session_state.token = result["token"]
                    st.session_state.user = result["user"]
                    st.success("🎉 Login realizado com sucesso!")
                    st.balloons()
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("❌ Email ou senha incorretos.")
            else:
                st.error("❌ Preencha todos os campos!")
        
        st.markdown("---")
        
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("📝 Criar Conta", use_container_width=True):
                st.session_state.show_signup = True
                st.rerun()
        with col_b:
            if st.button("🔑 Esqueci a Senha", use_container_width=True, help="Funcionalidade em desenvolvimento"):
                st.info("🔧 Funcionalidade de recuperação de senha em desenvolvimento.")
        
        st.markdown("""
        <div style="text-align: center; margin-top: 2rem; color: #666; font-size: 0.9rem;">
            💡 <strong>Dica:</strong> Mantenha suas tarefas organizadas e nunca perca um prazo!
        </div>
        """, unsafe_allow_html=True)

def signup_page():
    """Página de cadastro com design atrativo"""
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="color: #667eea; font-size: 3rem; margin-bottom: 0;">🎓 EduTrack AI</h1>
        <p style="color: #666; font-size: 1.2rem;">Junte-se à nossa comunidade acadêmica</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div style="background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h2 style="text-align: center; color: #333; margin-bottom: 2rem;">✨ Criar Nova Conta</h2>
        </div>
        """, unsafe_allow_html=True)
        
        name = st.text_input("👤 Nome Completo", placeholder="Seu nome completo")
        email = st.text_input("📧 Email", placeholder="seu@email.com")
        password = st.text_input("🔒 Senha", type="password", placeholder="Mínimo 6 caracteres")
        password_confirm = st.text_input("🔒 Confirmar Senha", type="password", placeholder="Digite a senha novamente")
        
        # Termos de uso
        agree = st.checkbox("✅ Concordo com os termos de uso e política de privacidade")
        
        if st.button("🎯 Criar Conta", use_container_width=True, type="primary"):
            if not name or not email or not password:
                st.error("❌ Preencha todos os campos!")
            elif password != password_confirm:
                st.error("❌ As senhas não conferem!")
            elif len(password) < 6:
                st.error("❌ A senha deve ter no mínimo 6 caracteres!")
            elif not agree:
                st.error("❌ Você deve concordar com os termos!")
            else:
                with st.spinner("Criando sua conta..."):
                    result = make_request("POST", "auth/signup", {
                        "name": name,
                        "email": email,
                        "password": password
                    })
                if result and "token" in result:
                    st.session_state.token = result["token"]
                    st.session_state.user = result["user"]
                    st.success("🎉 Conta criada com sucesso! Bem-vindo ao EduTrack!")
                    st.balloons()
                    st.session_state.show_signup = False
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("❌ Erro ao criar conta. Tente novamente.")
        
        st.markdown("---")
        
        if st.button("⬅️ Voltar ao Login", use_container_width=True):
            st.session_state.show_signup = False
            st.rerun()
        
        st.markdown("""
        <div style="text-align: center; margin-top: 2rem; color: #666; font-size: 0.9rem;">
            🔒 Seus dados estão seguros conosco. Nunca compartilhamos informações pessoais.
        </div>
        """, unsafe_allow_html=True)

def main_app():
    """Aplicação principal após login"""
    st.sidebar.title(f"👤 {st.session_state.user['name'] or st.session_state.user['email']}")
    
    menu = st.sidebar.radio("Menu", [
        "📊 Dashboard",
        "📚 Disciplinas", 
        "📝 Tarefas",
        "📈 Relatórios",
        "👤 Perfil",
        "🚪 Logout"
    ])
    
    if menu == "📊 Dashboard":
        dashboard_page()
    elif menu == "📚 Disciplinas":
        subjects_page()
    elif menu == "📝 Tarefas":
        tasks_page()
    elif menu == "📈 Relatórios":
        reports_page()
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
    st.markdown('<div class="main-header"><h1>🎓 EduTrack AI - Seu Assistente Acadêmico</h1><p>Gerencie suas disciplinas e tarefas de forma inteligente</p></div>', unsafe_allow_html=True)
    
    # Buscar dados da API
    subjects_response = make_request("GET", "subjects")
    tasks_response = make_request("GET", "tasks")
    stats_response = make_request("GET", "tasks/stats")
    
    subjects = subjects_response if subjects_response else []
    tasks = tasks_response if tasks_response else []
    stats = stats_response if stats_response else {"pending": 0, "overdue": 0}
    
    # Verificar se é usuário novo (sem dados)
    has_subjects = len(subjects) > 0
    has_tasks = len(tasks) > 0
    
    if not has_subjects and not has_tasks:
        # Tela de boas-vindas para usuários novos
        st.markdown("""
        <div class="welcome-card">
            <h2>👋 Bem-vindo ao EduTrack AI!</h2>
            <p>Comece sua jornada acadêmica organizando suas disciplinas e tarefas.</p>
            <p>📚 Adicione suas primeiras disciplinas no menu lateral</p>
            <p>📝 Crie tarefas para acompanhar seu progresso</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📚 Criar Primeira Disciplina", use_container_width=True, type="primary"):
                st.session_state.show_subjects_tab = True
                st.rerun()
        with col2:
            if st.button("📝 Criar Primeira Tarefa", use_container_width=True, type="secondary"):
                st.session_state.show_tasks_tab = True
                st.rerun()
        return
    
    # Métricas principais
    st.subheader("📊 Visão Geral")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        active_subjects = len([s for s in subjects if s.get("status") == "active"])
        st.markdown(f"""
        <div class="metric-card">
            <h3>📚 Disciplinas Ativas</h3>
            <h2 style="color: #667eea;">{active_subjects}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        pending = stats.get("pending", 0)
        st.markdown(f"""
        <div class="metric-card">
            <h3>📋 Tarefas Pendentes</h3>
            <h2 style="color: #ffa726;">{pending}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        overdue = stats.get("overdue", 0)
        st.markdown(f"""
        <div class="metric-card">
            <h3>⚠️ Tarefas Atrasadas</h3>
            <h2 style="color: #e53935;">{overdue}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        completed = len([t for t in tasks if t.get("status") == "completed"])
        total = len(tasks)
        progress = (completed / total * 100) if total > 0 else 0
        st.markdown(f"""
        <div class="metric-card">
            <h3>✅ Progresso Geral</h3>
            <h2 style="color: #43a047;">{progress:.0f}%</h2>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Progresso por disciplina
    if has_subjects:
        st.subheader("📈 Progresso por Disciplina")
        progress_cols = st.columns(min(len(subjects), 3))
        
        for i, subject in enumerate(subjects[:3]):
            with progress_cols[i]:
                subject_tasks = [t for t in tasks if t.get("subject_id") == subject["id"]]
                if subject_tasks:
                    completed_tasks = len([t for t in subject_tasks if t.get("status") == "completed"])
                    subject_progress = (completed_tasks / len(subject_tasks) * 100) if subject_tasks else 0
                    
                    st.markdown(f"""
                    <div class="metric-card">
                        <h4>{subject.get('name', 'Disciplina')}</h4>
                        <div style="background: #e0e0e0; border-radius: 10px; height: 8px; margin: 8px 0;">
                            <div style="background: linear-gradient(90deg, #43a047, #66bb6a); width: {subject_progress}%; height: 100%; border-radius: 10px;"></div>
                        </div>
                        <small>{completed_tasks}/{len(subject_tasks)} tarefas • {subject_progress:.0f}%</small>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="metric-card">
                        <h4>{subject.get('name', 'Disciplina')}</h4>
                        <p style="color: #666;">Nenhuma tarefa ainda</p>
                    </div>
                    """, unsafe_allow_html=True)
    
    # Próximas tarefas
    st.subheader("📌 Próximas Tarefas")
    if tasks:
        upcoming = sorted([t for t in tasks if t.get("status") != "completed"], 
                         key=lambda t: t.get("due_date", ""))[:5]
        
        if upcoming:
            for task in upcoming:
                due_date = datetime.fromisoformat(task.get("due_date", "")).strftime("%d/%m/%Y")
                days_left = (datetime.fromisoformat(task.get("due_date", "")) - datetime.now()).days
                
                priority_color = "#e53935" if task.get("priority") == "high" else "#ffa726" if task.get("priority") == "medium" else "#43a047"
                urgency_icon = "🔴" if days_left < 0 else "🟡" if days_left <= 2 else "🟢"
                
                st.markdown(f"""
                <div style="background: #f8f9fa; padding: 12px; border-radius: 8px; margin: 8px 0; border-left: 4px solid {priority_color};">
                    <strong>{task.get('title')}</strong><br>
                    <small>📅 {due_date} • {urgency_icon} {'Atrasada' if days_left < 0 else f'Faltam {days_left} dias'}</small>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.success("🎉 Parabéns! Todas as tarefas estão concluídas!")
    else:
        st.info("📝 Nenhuma tarefa pendente. Que tal criar uma nova?")

def subjects_page():
    """Página de disciplinas"""
    st.title("📚 Minhas Disciplinas")
    
    tab1, tab2, tab3 = st.tabs(["📋 Listar", "➕ Nova", "📦 Arquivadas"])
    
    with tab2:
        st.subheader("Cadastrar Nova Disciplina")
        with st.form("form_subject"):
            name = st.text_input("Nome da Disciplina", placeholder="Ex: Matemática Discreta")
            code = st.text_input("Código", placeholder="Ex: MAT123")
            professor = st.text_input("Professor", placeholder="Ex: Prof. Silva")
            semester = st.text_input("Semestre", placeholder="Ex: 2024.1")
            credits = st.number_input("Créditos", min_value=0, max_value=20, value=4)
            description = st.text_area("Descrição", placeholder="Descrição da disciplina...")
            
            if st.form_submit_button("Salvar Disciplina", use_container_width=True):
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
                        st.success("✅ Disciplina cadastrada com sucesso!")
                        st.rerun()
                    else:
                        st.error("❌ Erro ao cadastrar disciplina.")
                else:
                    st.error("❌ O nome da disciplina é obrigatório!")
    
    with tab1:
        st.subheader("Disciplinas Ativas")
        subjects = make_request("GET", "subjects")
        
        if subjects:
            active_subjects = [s for s in subjects if s.get("status") == "active"]
            
            if active_subjects:
                for subject in active_subjects:
                    with st.container():
                        col1, col2, col3 = st.columns([3, 1, 1])
                        
                        with col1:
                            st.markdown(f"**{subject.get('name')}**")
                            details = []
                            if subject.get('code'):
                                details.append(f"📋 {subject.get('code')}")
                            if subject.get('professor'):
                                details.append(f"👨‍🏫 {subject.get('professor')}")
                            if subject.get('semester'):
                                details.append(f"📅 {subject.get('semester')}")
                            if subject.get('credits'):
                                details.append(f"⭐ {subject.get('credits')} créditos")
                            
                            if details:
                                st.caption(" • ".join(details))
                            if subject.get('description'):
                                st.caption(subject.get('description'))
                        
                        with col2:
                            # Calcular progresso da disciplina
                            tasks_response = make_request("GET", "tasks")
                            if tasks_response:
                                subject_tasks = [t for t in tasks_response if t.get("subject_id") == subject["id"]]
                                if subject_tasks:
                                    completed = len([t for t in subject_tasks if t.get("status") == "completed"])
                                    total = len(subject_tasks)
                                    progress = (completed / total * 100) if total > 0 else 0
                                    st.metric("Progresso", f"{progress:.0f}%", f"{completed}/{total}")
                                else:
                                    st.caption("Sem tarefas")
                        
                        with col3:
                            col_edit, col_archive, col_delete = st.columns(3)
                            
                            with col_edit:
                                if st.button("✏️", key=f"edit_{subject['id']}", help="Editar"):
                                    st.session_state.edit_subject_id = subject['id']
                            
                            with col_archive:
                                if st.button("📦", key=f"archive_{subject['id']}", help="Arquivar"):
                                    if st.session_state.get(f"confirm_archive_{subject['id']}", False):
                                        result = make_request("PATCH", f"subjects/{subject['id']}", {"status": "completed"})
                                        if result:
                                            st.success("Disciplina arquivada!")
                                            st.session_state[f"confirm_archive_{subject['id']}"] = False
                                            st.rerun()
                                        else:
                                            st.error("Erro ao arquivar disciplina.")
                                    else:
                                        st.session_state[f"confirm_archive_{subject['id']}"] = True
                                        st.warning("Clique novamente para confirmar o arquivamento.")
                            
                            with col_delete:
                                if st.button("🗑️", key=f"delete_{subject['id']}", help="Excluir"):
                                    if st.session_state.get(f"confirm_delete_{subject['id']}", False):
                                        result = make_request("DELETE", f"subjects/{subject['id']}")
                                        if result is not None:  # DELETE retorna None em sucesso
                                            st.success("Disciplina excluída!")
                                            st.session_state[f"confirm_delete_{subject['id']}"] = False
                                            st.rerun()
                                        else:
                                            st.error("Erro ao excluir disciplina.")
                                    else:
                                        st.session_state[f"confirm_delete_{subject['id']}"] = True
                                        st.error("⚠️ Clique novamente para confirmar a exclusão. Esta ação não pode ser desfeita!")
            else:
                st.info("📚 Nenhuma disciplina ativa. Crie uma nova para começar!")
        else:
            st.info("📚 Nenhuma disciplina cadastrada. Crie uma nova para começar!")
    
    with tab3:
        st.subheader("Disciplinas Arquivadas/Concluídas")
        subjects = make_request("GET", "subjects")
        
        if subjects:
            archived_subjects = [s for s in subjects if s.get("status") in ["completed", "dropped"]]
            
            if archived_subjects:
                for subject in archived_subjects:
                    with st.container():
                        col1, col2 = st.columns([4, 1])
                        
                        with col1:
                            status_icon = "✅" if subject.get("status") == "completed" else "❌"
                            st.markdown(f"{status_icon} **{subject.get('name')}** (Arquivada)")
                            if subject.get('semester'):
                                st.caption(f"Semestre: {subject.get('semester')}")
                        
                        with col2:
                            if st.button("🔄", key=f"restore_{subject['id']}", help="Restaurar"):
                                result = make_request("PATCH", f"subjects/{subject['id']}", {"status": "active"})
                                if result:
                                    st.success("Disciplina restaurada!")
                                    st.rerun()
                                else:
                                    st.error("Erro ao restaurar disciplina.")
            else:
                st.info("📦 Nenhuma disciplina arquivada.")

def tasks_page():
    """Página de tarefas"""
    st.title("📝 Minhas Tarefas")
    
    tab1, tab2 = st.tabs(["📋 Listar", "➕ Nova"])
    
    with tab2:
        st.subheader("Cadastrar Nova Tarefa")
        subjects = make_request("GET", "subjects")
        subject_names = {s['id']: s['name'] for s in subjects} if subjects else {}
        
        with st.form("form_task"):
            subject_id = st.selectbox("Disciplina", options=list(subject_names.keys()), 
                                    format_func=lambda x: subject_names.get(x, "Selecione uma disciplina"))
            title = st.text_input("Título da Tarefa", placeholder="Ex: Estudar capítulo 5")
            description = st.text_area("Descrição", placeholder="Detalhes da tarefa...")
            due_date = st.date_input("Prazo de Entrega", value=datetime.now() + timedelta(days=7))
            priority = st.selectbox("Prioridade", 
                                  options=["low", "medium", "high"],
                                  format_func=lambda x: {"low": "Baixa 🟢", "medium": "Média 🟡", "high": "Alta 🔴"}.get(x, x))
            
            if st.form_submit_button("Salvar Tarefa", use_container_width=True):
                if title and subject_id:
                    result = make_request("POST", "tasks", {
                        "subject_id": subject_id,
                        "title": title,
                        "description": description,
                        "due_date": due_date.isoformat(),
                        "priority": priority
                    })
                    if result:
                        st.success("✅ Tarefa criada com sucesso!")
                        st.rerun()
                    else:
                        st.error("❌ Erro ao criar tarefa.")
                else:
                    st.error("❌ Título e Disciplina são obrigatórios!")
    
    with tab1:
        st.subheader("Suas Tarefas")
        tasks = make_request("GET", "tasks")
        subjects = make_request("GET", "subjects")
        subject_names = {s['id']: s['name'] for s in subjects} if subjects else {}
        
        if tasks:
            # Filtros
            col1, col2 = st.columns([2, 2])
            with col1:
                status_filter = st.selectbox("Filtrar por Status", 
                                           ["Todas", "pending", "in_progress", "completed"],
                                           format_func=lambda x: {
                                               "Todas": "Todas as tarefas",
                                               "pending": "❌ Pendentes", 
                                               "in_progress": "⏳ Em andamento", 
                                               "completed": "✅ Concluídas"
                                           }.get(x, x))
            
            with col2:
                subject_filter = st.selectbox("Filtrar por Disciplina", 
                                            ["Todas"] + list(subject_names.values()),
                                            index=0)
            
            # Aplicar filtros
            filtered = tasks
            if status_filter != "Todas":
                filtered = [t for t in filtered if t.get('status') == status_filter]
            if subject_filter != "Todas":
                subject_id = [k for k, v in subject_names.items() if v == subject_filter][0]
                filtered = [t for t in filtered if t.get('subject_id') == subject_id]
            
            if filtered:
                for task in sorted(filtered, key=lambda t: (
                    0 if t.get('status') == 'completed' else 1,
                    t.get('due_date', ''),
                    {'high': 0, 'medium': 1, 'low': 2}.get(t.get('priority'), 3)
                )):
                    with st.container():
                        # Calcular urgência
                        due_date_obj = datetime.fromisoformat(task.get('due_date', ''))
                        days_left = (due_date_obj - datetime.now()).days
                        is_overdue = days_left < 0
                        
                        # Definir cores baseado na prioridade e urgência
                        priority_color = "#e53935" if task.get("priority") == "high" else "#ffa726" if task.get("priority") == "medium" else "#43a047"
                        if is_overdue and task.get('status') != 'completed':
                            border_color = "#d32f2f"
                            bg_color = "#ffebee"
                        elif task.get('status') == 'completed':
                            border_color = "#43a047"
                            bg_color = "#e8f5e8"
                        else:
                            border_color = priority_color
                            bg_color = "#fafafa"
                        
                        st.markdown(f"""
                        <div style="background: {bg_color}; border: 2px solid {border_color}; border-radius: 10px; padding: 15px; margin: 10px 0;">
                        """, unsafe_allow_html=True)
                        
                        col1, col2 = st.columns([4, 1])
                        
                        with col1:
                            # Título e status
                            status_icon = "✅" if task.get('status') == 'completed' else "⏳" if task.get('status') == 'in_progress' else "❌"
                            priority_icon = "🔴" if task.get('priority') == 'high' else "🟡" if task.get('priority') == 'medium' else "🟢"
                            
                            st.markdown(f"{status_icon} {priority_icon} **{task.get('title')}**")
                            
                            # Detalhes
                            details = []
                            subject_name = subject_names.get(task.get('subject_id'), 'N/A')
                            details.append(f"📚 {subject_name}")
                            
                            due_date_str = due_date_obj.strftime("%d/%m/%Y")
                            if is_overdue and task.get('status') != 'completed':
                                details.append(f"📅 {due_date_str} (ATRASADA)")
                            else:
                                details.append(f"📅 {due_date_str}")
                            
                            if days_left >= 0 and task.get('status') != 'completed':
                                details.append(f"⏰ Faltam {days_left} dias")
                            
                            st.caption(" • ".join(details))
                            
                            if task.get('description'):
                                st.write(task.get('description'))
                        
                        with col2:
                            # Ações
                            if task.get('status') != 'completed':
                                if st.button("✅", key=f"complete_{task['id']}", help="Marcar como concluída"):
                                    result = make_request("PATCH", f"tasks/{task['id']}", {"status": "completed"})
                                    if result:
                                        st.success("Tarefa concluída!")
                                        st.rerun()
                                    else:
                                        st.error("Erro ao atualizar tarefa.")
                            
                            if st.button("✏️", key=f"edit_task_{task['id']}", help="Editar"):
                                st.session_state.edit_task_id = task['id']
                            
                            if st.button("🗑️", key=f"delete_task_{task['id']}", help="Excluir"):
                                if st.session_state.get(f"confirm_delete_task_{task['id']}", False):
                                    result = make_request("DELETE", f"tasks/{task['id']}")
                                    if result is not None:
                                        st.success("Tarefa excluída!")
                                        st.session_state[f"confirm_delete_task_{task['id']}"] = False
                                        st.rerun()
                                    else:
                                        st.error("Erro ao excluir tarefa.")
                                else:
                                    st.session_state[f"confirm_delete_task_{task['id']}"] = True
                                    st.error("⚠️ Clique novamente para confirmar a exclusão!")
                        
                        st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.info("📝 Nenhuma tarefa encontrada com os filtros aplicados.")
        else:
            st.info("📝 Nenhuma tarefa cadastrada. Crie uma nova para começar!")

def reports_page():
    """Página de relatórios e analytics"""
    st.title("📈 Relatórios e Análises")
    
    # Buscar dados
    subjects_response = make_request("GET", "subjects")
    tasks_response = make_request("GET", "tasks")
    
    subjects = subjects_response if subjects_response else []
    tasks = tasks_response if tasks_response else []
    
    if not subjects and not tasks:
        st.info("📊 Crie algumas disciplinas e tarefas para ver os relatórios!")
        return
    
    tab1, tab2, tab3 = st.tabs(["📊 Visão Geral", "📈 Por Disciplina", "📅 Histórico"])
    
    with tab1:
        st.subheader("Visão Geral do Período")
        
        # Filtros de período
        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input("Data Inicial", value=datetime.now() - timedelta(days=30))
        with col2:
            end_date = st.date_input("Data Final", value=datetime.now() + timedelta(days=30))
        
        # Estatísticas gerais
        total_subjects = len(subjects)
        total_tasks = len(tasks)
        completed_tasks = len([t for t in tasks if t.get("status") == "completed"])
        pending_tasks = len([t for t in tasks if t.get("status") in ["pending", "in_progress"]])
        overdue_tasks = len([t for t in tasks if t.get("status") != "completed" and 
                           datetime.fromisoformat(t.get("due_date", "")) < datetime.now()])
        
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("📚 Total Disciplinas", total_subjects)
        col2.metric("📝 Total Tarefas", total_tasks)
        col3.metric("✅ Concluídas", completed_tasks)
        col4.metric("⏳ Pendentes", pending_tasks)
        col5.metric("⚠️ Atrasadas", overdue_tasks)
        
        # Gráfico de distribuição por status
        if tasks:
            status_counts = {
                "Concluídas": completed_tasks,
                "Pendentes": len([t for t in tasks if t.get("status") == "pending"]),
                "Em Andamento": len([t for t in tasks if t.get("status") == "in_progress"]),
                "Atrasadas": overdue_tasks
            }
            
            st.subheader("Distribuição por Status")
            st.bar_chart(status_counts)
    
    with tab2:
        st.subheader("Progresso por Disciplina")
        
        if subjects:
            progress_data = []
            for subject in subjects:
                subject_tasks = [t for t in tasks if t.get("subject_id") == subject["id"]]
                if subject_tasks:
                    completed = len([t for t in subject_tasks if t.get("status") == "completed"])
                    total = len(subject_tasks)
                    progress = (completed / total * 100) if total > 0 else 0
                    
                    progress_data.append({
                        "Disciplina": subject.get("name", "N/A"),
                        "Código": subject.get("code", ""),
                        "Tarefas Concluídas": completed,
                        "Total Tarefas": total,
                        "Progresso (%)": round(progress, 1),
                        "Status": subject.get("status", "active").title()
                    })
            
            if progress_data:
                df = pd.DataFrame(progress_data)
                st.dataframe(df, use_container_width=True)
                
                # Gráfico de progresso
                st.subheader("Gráfico de Progresso")
                chart_data = df.set_index("Disciplina")["Progresso (%)"]
                st.bar_chart(chart_data)
            else:
                st.info("Nenhuma tarefa encontrada para as disciplinas.")
    
    with tab3:
        st.subheader("Histórico de Tarefas")
        
        if tasks:
            # Filtro por período
            period_filter = st.selectbox("Período", ["Últimos 7 dias", "Últimos 30 dias", "Últimos 90 dias", "Todos"])
            
            now = datetime.now()
            if period_filter == "Últimos 7 dias":
                filter_date = now - timedelta(days=7)
            elif period_filter == "Últimos 30 dias":
                filter_date = now - timedelta(days=30)
            elif period_filter == "Últimos 90 dias":
                filter_date = now - timedelta(days=90)
            else:
                filter_date = datetime.min
            
            # Filtrar tarefas por período
            filtered_tasks = []
            for task in tasks:
                created_at = datetime.fromisoformat(task.get("created_at", ""))
                if created_at >= filter_date:
                    filtered_tasks.append(task)
            
            if filtered_tasks:
                # Preparar dados para tabela
                history_data = []
                for task in sorted(filtered_tasks, key=lambda t: t.get("created_at", ""), reverse=True):
                    subject_name = "N/A"
                    for subject in subjects:
                        if subject["id"] == task.get("subject_id"):
                            subject_name = subject.get("name", "N/A")
                            break
                    
                    history_data.append({
                        "Título": task.get("title", ""),
                        "Disciplina": subject_name,
                        "Status": task.get("status", "").replace("_", " ").title(),
                        "Prioridade": task.get("priority", "").title(),
                        "Criada em": datetime.fromisoformat(task.get("created_at", "")).strftime("%d/%m/%Y"),
                        "Vence em": datetime.fromisoformat(task.get("due_date", "")).strftime("%d/%m/%Y") if task.get("due_date") else "N/A"
                    })
                
                df_history = pd.DataFrame(history_data)
                st.dataframe(df_history, use_container_width=True)
                
                # Botão de exportação
                if st.button("📥 Exportar CSV", type="primary"):
                    csv = df_history.to_csv(index=False)
                    st.download_button(
                        label="📥 Baixar CSV",
                        data=csv,
                        file_name=f"edutrack_relatorio_{datetime.now().strftime('%Y%m%d')}.csv",
                        mime="text/csv"
                    )
            else:
                st.info(f"Nenhuma tarefa encontrada no período selecionado ({period_filter}).")

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