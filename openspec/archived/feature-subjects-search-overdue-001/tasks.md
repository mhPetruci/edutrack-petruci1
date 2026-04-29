# Tasks - feature-subjects-search-overdue

- [ ] Definir e documentar o endpoint `GET /subjects/search` com parâmetros `name` e `overdue_tasks`
- [ ] Implementar validação de autenticação e propriedade do usuário
- [ ] Criar a lógica Python que identifica `subject_id` de disciplinas com tarefas atrasadas
- [ ] Integrar a função Python ao endpoint REST para compor o filtro de pesquisa
- [ ] Implementar filtro `OR` entre busca por nome e tarefas atrasadas
- [ ] Testar os casos:
  - apenas `name`
  - apenas `overdue_tasks=true`
  - ambos simultâneos
  - nenhum filtro
  - acesso de usuário não autorizado
