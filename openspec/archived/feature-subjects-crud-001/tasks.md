# Tasks - feature-subjects-crud

- [ ] Criar endpoints CRUD para `subjects`:
  - POST /subjects
  - GET /subjects
  - PATCH /subjects/{subject_id}
  - DELETE /subjects/{subject_id}
- [ ] Garantir que cada endpoint só acesse subjects pertencentes ao usuário autenticado
- [ ] Retornar 403 Forbidden se o usuário tentar alterar ou excluir subject de outro proprietário
