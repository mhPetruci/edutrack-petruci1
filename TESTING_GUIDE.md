# 🧪 Guia de Teste - EduTrack AI

Este documento fornece instruções passo-a-passo para testar todas as novas funcionalidades implementadas.

---

## ✅ Pré-requisitos

- [ ] Python 3.8+
- [ ] Streamlit instalado
- [ ] Backend (Xano) rodando em `http://localhost:3000`
- [ ] Arquivo `.streamlit/secrets.toml` configurado
- [ ] Dependências do `requirements.txt` instaladas

**Verificar com:**
```bash
python --version
streamlit --version
pip list | grep streamlit
```

---

## 🚀 Como Iniciar os Testes

### 1. Instalar Dependências
```bash
cd c:\Users\2502570\Documents\coding\edutrack-petruci
pip install -r requirements.txt
```

### 2. Executar o App
```bash
streamlit run app.py
```

### 3. Acessar
```
http://localhost:8501
```

---

## 📋 Cenários de Teste

### ✅ Teste 1: Login e Signup

**Objetivo:** Validar design e funcionalidade de autenticação

**Passos:**

1. [ ] Abra `http://localhost:8501`
   - **Verificar:** Vê a tela de login com design profissional?
   - **Verificar:** Paleta de cores roxo/magenta está visível?

2. [ ] Clique em "📝 Criar Conta"
   - **Verificar:** Transição para página de cadastro
   - **Verificar:** Design atraente com card centralizado

3. [ ] Cadastre novo usuário
   - Nome: "Teste Silva"
   - Email: "teste@example.com"
   - Senha: "senha123"
   - Confirme: "senha123"
   - [ ] Aceite os termos

4. [ ] Clique "🎯 Criar Conta"
   - **Verificar:** Mensagem de sucesso
   - **Verificar:** Confetes aparecendo (balloons)
   - **Verificar:** Redirecionado para dashboard

5. [ ] Logout (menu lateral > 🚪 Logout)
   - **Verificar:** Voltou para login

6. [ ] Faça login com credenciais criadas
   - [ ] Email: teste@example.com
   - [ ] Senha: senha123
   - **Verificar:** Login com sucesso

---

### ✅ Teste 2: Dashboard para Usuário Novo

**Objetivo:** Validar tela de boas-vindas

**Passos:**

1. [ ] Após login com novo usuário
   - **Verificar:** Card rosa com mensagem de boas-vindas
   - **Verificar:** Ícones motivacionais
   - **Verificar:** 2 botões de ação rápida

2. [ ] Clique em "📚 Criar Primeira Disciplina"
   - **Verificar:** Vai para aba "Nova" em Disciplinas

3. [ ] Volte para Dashboard (menu lateral)
   - **Verificar:** A tela de boas-vindas ainda aparece

4. [ ] Crie uma disciplina e uma tarefa

5. [ ] Volte para Dashboard
   - **Verificar:** Dashboard agora mostra métricas reais
   - **Verificar:** Nenhuma tela de boas-vindas

---

### ✅ Teste 3: Dashboard com Dados

**Objetivo:** Validar métricas e visualizações

**Passos:**

1. [ ] Crie 3 disciplinas:
   - Disciplina 1: Matemática
   - Disciplina 2: Português
   - Disciplina 3: História

2. [ ] Crie 5 tarefas variadas:
   - 2 na Matemática (1 concluída, 1 pendente)
   - 2 em Português (ambas pendentes)
   - 1 em História (concluída)

3. [ ] Acesse Dashboard e verifique:
   - [ ] **Métrica 1:** "📚 Disciplinas Ativas" = 3
   - [ ] **Métrica 2:** "📋 Tarefas Pendentes" = 3
   - [ ] **Métrica 3:** "⚠️ Tarefas Atrasadas" = 0 ou N
   - [ ] **Métrica 4:** "✅ Progresso Geral" = 40% (2/5 concluídas)

4. [ ] Verifique "Progresso por Disciplina":
   - [ ] **Matemática:** 50% (1/2)
   - [ ] **Português:** 0% (0/2)
   - [ ] **História:** 100% (1/1)

5. [ ] Verifique "Próximas Tarefas":
   - [ ] Mostra as tarefas pendentes/não concluídas
   - [ ] Ordenado por data de vencimento
   - [ ] Ícones de prioridade coloridos

---

### ✅ Teste 4: Página de Disciplinas

**Objetivo:** Validar CRUD e arquivamento

**Passos:**

1. [ ] Acesse "📚 Disciplinas"

2. **Aba "Listar":**
   - [ ] Vê as 3 disciplinas criadas?
   - [ ] Cada card mostra: nome, código, professor, semestre, créditos, descrição?
   - [ ] Mostra progresso com barras visuais?
   - [ ] Botões 📦 (arquivar) e 🗑️ (deletar) estão disponíveis?

3. **Teste Arquivamento:**
   - [ ] Clique em 📦 (arquivar) em "Matemática"
   - **Verificar:** Mensagem "Clique novamente para confirmar o arquivamento"
   - [ ] Clique novamente
   - **Verificar:** "Disciplina arquivada!" e desaparece da lista

4. **Aba "Arquivadas":**
   - [ ] "Matemática" agora aparece aqui
   - [ ] Mostra status "✅ Arquivada"
   - [ ] Clique em 🔄 para restaurar
   - **Verificar:** Volta para "Ativas"

5. **Teste Cadastro:**
   - [ ] Aba "Nova"
   - [ ] Preencha: Nome, Código, Professor, Semestre, Créditos, Descrição
   - [ ] Clique "Salvar Disciplina"
   - **Verificar:** Mensagem de sucesso

6. **Teste Deleção:**
   - [ ] Clique em 🗑️ em uma disciplina
   - **Verificar:** Mensagem vermelha "⚠️ Clique novamente para confirmar!"
   - [ ] Não clique (cancele)
   - **Verificar:** Disciplina permanece

---

### ✅ Teste 5: Página de Tarefas

**Objetivo:** Validar CRUD, filtros e confirmações

**Passos:**

1. [ ] Acesse "📝 Tarefas"

2. **Aba "Listar":**
   - [ ] Todas as 5 tarefas aparecem?
   - [ ] Cada tarefa mostra:
     - Status (✅/⏳/❌)
     - Prioridade (🔴/🟡/🟢)
     - Título
     - Disciplina
     - Data de vencimento
     - Dias restantes/Atrasada

3. **Teste Filtros:**
   - [ ] Filtro por Status "completed"
   - **Verificar:** Mostra apenas 2 tarefas concluídas
   - [ ] Filtro por Status "pending"
   - **Verificar:** Mostra apenas tarefas pendentes
   - [ ] Filtro por Disciplina "Matemática"
   - **Verificar:** Mostra apenas de Matemática
   - [ ] Remova filtros (volta a "Todas")

4. **Teste Cores:**
   - [ ] Tarefas com prioridade "high" têm borda vermelha?
   - [ ] Tarefas com prioridade "medium" têm borda laranja?
   - [ ] Tarefas concluídas têm fundo verde?
   - [ ] Tarefas atrasadas têm fundo vermelho?

5. **Teste Marcar Concluída:**
   - [ ] Clique ✅ em uma tarefa pendente
   - **Verificar:** Status muda para concluída (❌ → ✅)
   - **Verificar:** Card fica verde

6. **Teste Deleção:**
   - [ ] Clique 🗑️ em uma tarefa
   - **Verificar:** Mensagem vermelha "⚠️ Clique novamente para confirmar!"
   - [ ] Clique novamente
   - **Verificar:** Tarefa removida

7. **Aba "Nova":**
   - [ ] Crie nova tarefa com:
     - Disciplina: Português
     - Título: "Ensaio sobre Literatura"
     - Descrição: "Escrever ensaio..."
     - Prazo: Data futura
     - Prioridade: Alta (🔴)
   - **Verificar:** Tarefa criada e aparece na lista

---

### ✅ Teste 6: Página de Relatórios (NOVO)

**Objetivo:** Validar nova página de relatórios

**Passos:**

1. [ ] Acesse "📈 Relatórios" (nova opção no menu)

2. **Aba "Visão Geral":**
   - [ ] Vê os filtros de data (Data Inicial / Data Final)?
   - [ ] Métricas aparecem:
     - [ ] Total Disciplinas
     - [ ] Total Tarefas
     - [ ] Concluídas
     - [ ] Pendentes
     - [ ] Atrasadas
   - [ ] Gráfico de barras mostra distribuição por status?

3. **Aba "Por Disciplina":**
   - [ ] Tabela com colunas:
     - [ ] Disciplina
     - [ ] Código
     - [ ] Tarefas Concluídas
     - [ ] Total Tarefas
     - [ ] Progresso (%)
     - [ ] Status
   - [ ] Gráfico de barras mostra progresso por disciplina?

4. **Aba "Histórico":**
   - [ ] Filtro "Período" com opções (7, 30, 90 dias, Todos)?
   - [ ] Tabela com histórico:
     - [ ] Título
     - [ ] Disciplina
     - [ ] Status
     - [ ] Prioridade
     - [ ] Criada em
     - [ ] Vence em
   - [ ] Dados formatados com datas em DD/MM/YYYY?

5. **Teste Exportação:**
   - [ ] Clique "📥 Exportar CSV"
   - **Verificar:** Botão "📥 Baixar CSV" aparece
   - [ ] Clique em "Baixar CSV"
   - **Verificar:** Arquivo baixado (nome: `edutrack_relatorio_YYYYMMDD.csv`)
   - [ ] Abra em Excel/Google Sheets
   - **Verificar:** Dados estão formatados corretamente

---

### ✅ Teste 7: Design e Cores

**Objetivo:** Validar identidade visual

**Passos:**

1. [ ] Navegar por todo app e verificar:
   - [ ] Cores consistentes em todas as páginas
   - [ ] Roxo (#667eea) como cor primária
   - [ ] Magenta (#764ba2) em gradientes
   - [ ] Verde (#43a047) para sucesso
   - [ ] Laranja (#ffa726) para aviso
   - [ ] Vermelho (#e53935) para erro

2. [ ] Componentes:
   - [ ] Cards com sombras suaves
   - [ ] Botões com bordas arredondadas
   - [ ] Tabs com design moderno
   - [ ] Ícones emojis consistentes

3. [ ] Responsividade:
   - [ ] Redimensione a janela do navegador
   - **Verificar:** Layout se adapta bem
   - **Verificar:** Não há overflow de conteúdo

---

### ✅ Teste 8: Confirmações Duplas

**Objetivo:** Validar sistema de confirmação

**Passos:**

1. **Exclusão de Tarefa:**
   - [ ] Clique 🗑️ em uma tarefa
   - **Verificar:** Primeira mensagem "⚠️ Clique novamente para confirmar!"
   - [ ] Clique novamente
   - **Verificar:** Tarefa removida

2. **Exclusão de Disciplina:**
   - [ ] Clique 🗑️ em uma disciplina
   - **Verificar:** Mensagem em vermelho
   - [ ] Clique novamente
   - **Verificar:** Disciplina removida

3. **Arquivamento:**
   - [ ] Clique 📦 em uma disciplina
   - **Verificar:** Mensagem "Clique novamente para confirmar o arquivamento"
   - [ ] Clique novamente
   - **Verificar:** Arquivada com sucesso

---

### ✅ Teste 9: Perfil

**Objetivo:** Validar página de perfil

**Passos:**

1. [ ] Acesse "👤 Perfil"

2. [ ] Verifique dados:
   - [ ] Nome preenchido
   - [ ] Email desabilitado (apenas leitura)
   - [ ] Data de membro formatada em DD/MM/YYYY

3. [ ] Edite nome:
   - [ ] Mude para "Teste Silva Atualizado"
   - [ ] Clique "Atualizar Perfil"
   - **Verificar:** Mensagem de sucesso

4. [ ] Volte para Dashboard:
   - **Verificar:** Nome atualizado no sidebar

---

## 🎯 Checklist de Validação

### Funcionalidades Principais
- [ ] Login com design atrativo
- [ ] Cadastro com validações
- [ ] Dashboard com boas-vindas
- [ ] Dashboard com 4 métricas
- [ ] Progresso visual por disciplina
- [ ] Próximas tarefas com urgência
- [ ] CRUD de disciplinas
- [ ] Arquivamento de disciplinas
- [ ] CRUD de tarefas
- [ ] Filtros de tarefas
- [ ] Confirmações duplas
- [ ] Página de relatórios (NOVO)
- [ ] Gráficos em relatórios
- [ ] Exportação CSV
- [ ] Página de perfil

### Design
- [ ] Cores consistentes
- [ ] Components estilizados
- [ ] Responsividade
- [ ] Ícones adequados
- [ ] Feedback visual

### Segurança
- [ ] Confirmação dupla para delete
- [ ] User ownership enforcement
- [ ] Validações de entrada
- [ ] Mensagens de erro claras

---

## 📊 Resultados Esperados

### ✅ Todos os Testes Passam Se:
- Dashboard mostra 4 métricas corretas
- Relatórios exportam em CSV
- Disciplinas podem ser arquivadas
- Confirmações duplas funcionam
- Design é profissional e consistente
- Filtros funcionam corretamente
- Gráficos exibem dados

### ❌ Problemas Comuns:
- **Erro de conexão API:** Verifique se backend está rodando
- **Secrets não carregados:** Crie `.streamlit/secrets.toml`
- **Estilo CSS não aplicado:** Limpe cache (Ctrl+Shift+R)
- **Dados não sincronizam:** Recarregue página (F5)

---

## 📝 Relatório de Teste

Após completar todos os testes, preencha este template:

```
Data: ___/___/____
Tester: _____________
Status: [ ] PASSOU [ ] FALHOU

Testes Completos: ___ / 9

Problemas Encontrados:
1. 
2. 
3. 

Observações Adicionais:

Recomendações:
```

---

## 🎉 Conclusão

Após completar todos os testes com sucesso, o EduTrack AI está pronto para:
- ✅ Uso em produção
- ✅ Compartilhamento com usuários
- ✅ Deploy em servidor
- ✅ Integração com Xano

**Parabéns pela conclusão dos testes!** 🚀

---

**Última atualização:** 13 de Maio de 2026  
**Versão:** 1.0.0  
**Status:** Ready for Testing ✅
