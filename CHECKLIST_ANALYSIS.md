# Análise do Checklist Funcional - EduTrack

Data: 2026-05-06 | Branch: `feat/hybrid-search`

## 🔐 Autenticação e Acesso

### Pronto ✅
- `functions/auth_context.js` — extrae o contexto de autenticação do request (`req.auth`, `req.user`)
- Validação em todos os endpoints (`requireAuthenticatedUser` aplicado em POST, GET, PATCH, DELETE)
- Enforcement de `user_id == auth.id` implementado

### Faltando ❌
- **Signup com e-mail e senha** — Não há endpoint de registro
- **Login com credenciais** — Não há endpoint de autenticação
- **Perfil de usuário** — Estrutura existe em `pages/3_👤_Perfil.py` mas vazia (sem backend)
- **Editar perfil** — Não implementado
- **Reset de senha via e-mail** — Não implementado
- **Expiração automática de token** — Não implementado

### Pode melhorar 🔧
- Separar lógica de autenticação em um módulo dedicado
- Implementar refresh token strategy
- Adicionar rate limiting para login/signup

---

## 📚 Gestão de Disciplinas

### Pronto ✅
- **CRUD completo** — POST, GET, PATCH, DELETE implementados em `apis/subjects/`
- **Listagem** — `GET /subjects` (via `get_subjects.js`)
- **Busca por nome** — `GET /subjects/search?name=...` implementado
- **Filtro por tarefas atrasadas** — `GET /subjects/search?overdue_tasks=true` implementado
- **Validação de propriedade** — `owner_id` verificado em todos os endpoints
- **Armazenamento no BD** — Schema `tables/subjects.json` com índices e restrições

### Faltando ❌
- **UI de cadastro conectada ao backend** — `pages/1_📚_Disciplinas.py` é simulação, não conecta aos endpoints
- **Prevenção de duplicatas** — Constraint `unique(owner_id, name)` existe no schema, mas não há feedback adequado
- **Edição e exclusão na UI** — Não há componentes Streamlit para essas ações
- **Listagem dinâmica na UI** — A página mostra dados fake, não consome API

### Pode melhorar 🔧
- Implementar soft-delete ou status "archived" em vez de DELETE direto
- Adicionar validação de campos obrigatórios na UI
- Melhorar UX de confirmação antes de deletar

---

## 📝 Gestão de Tarefas

### Pronto ✅
- **Lógica de identificação de tarefas atrasadas** — `scripts/find_overdue_subject_ids.py` + `functions/subject_overdue_helper.js`
- **Endpoint de busca integrado** — Tarefas atrasadas detectadas em `GET /subjects/search?overdue_tasks=true`

### Faltando ❌
- **CRUD de tarefas** — Sem endpoints POST, GET, PATCH, DELETE para `academic_tasks`
- **Criação de tarefa** — Não há endpoint para criar tarefa vinculada a disciplina
- **Listagem de tarefas** — Não há endpoint para listar tarefas do usuário
- **Status (Pendente, Em andamento, Concluída)** — Suporte baseado no schema esperado, mas sem CRUD
- **Filtro por status** — Não há endpoint implementado
- **Marcar como concluída** — Não há endpoint para atualizar status
- **Agrupamento por disciplina/prazo** — Não implementado
- **UI de tarefas** — `pages/2_📝_Tarefas.py` é apenas exemplo com dados fake

### Pode melhorar 🔧
- Criar função helper `tasks_crud.js` similar a `subjects_crud.js`
- Implementar ordenação padrão por `due_date`
- Adicionar indicador visual de atraso na UI

---

## 🏠 Propostas de Melhoria

### Dashboard ❌ (Não iniciado)
- Total de disciplinas ativas — Não calculado
- Total de tarefas pendentes/atrasadas — Não calculado
- Próximas tarefas por prazo — Não listadas
- Indicador de progresso — `scripts/calculate_progress.py` existe, mas não integrado na UI

### Relatórios e Progresso ❌ (Não iniciado)
- Histórico de tarefas — Sem tela de relatórios
- Progresso por disciplina — Sem cálculos agregados
- Exportação CSV/PDF — Não implementada

### Evolução das Disciplinas ❌ (Não iniciado)
- Campo semestre — Existe no schema, mas não usado na UI
- Prioridade de tarefas — Não existe campo nem CRUD
- Progresso visual — Não implementado
- Arquivamento de disciplinas — Não implementado (seria soft-delete)

### Design e UX ❌ (Não iniciado)
- Identidade visual — Streamlit padrão, sem customização
- Layout de login/signup — Não existe
- Tela de boas-vindas — Não existe
- Confirmação antes de deletar — Não implementada

---

## 📊 Resumo de Progresso

| Categoria | Implementado | Faltando | Prioridade |
|-----------|:---:|:---:|:---:|
| **Autenticação** | 30% | 70% | 🔴 Alta |
| **Disciplinas** | 70% | 30% | 🟡 Média |
| **Tarefas** | 20% | 80% | 🔴 Alta |
| **Dashboard** | 0% | 100% | 🟡 Média |
| **Relatórios** | 0% | 100% | 🟢 Baixa |
| **UX/Design** | 10% | 90% | 🟡 Média |

---

## 🎯 Próximos Passos Recomendados

1. **Implementar CRUD de Tarefas** (alta prioridade)
   - Criar `functions/tasks_crud.js`
   - Criar endpoints em `apis/tasks/`
   - Integrar com autenticação

2. **Implementar Dashboard** (média prioridade)
   - Integrar `calculate_progress.py` na UI
   - Mostrar métricas reais (contagem de disciplinas, tarefas)
   - Próximas tarefas com prazo

3. **Conectar UI ao Backend** (alta prioridade)
   - Remover dados fake das páginas
   - Integrar chamadas aos endpoints REST
   - Adicionar feedback visual e tratamento de erros

4. **Autenticação de Usuários** (alta prioridade)
   - Implementar endpoints de signup/login
   - Gerenciar tokens
   - Sessão do usuário
