# Tasks - Subjects

1. [x] Implementar tabela `subjects` no Xano
   - Criar campos: owner_id (FK), name, code, description, status, credits, semester, created_at, updated_at
   - Incluir índices `owner_id`, `name`
   - Adicionar restrições de unicidade (user_id + name)

2. [ ] Implementar funções de acesso a dados (CRUD)
   - get_subjects_by_owner(owner_id)
   - create_subject(data)
   - update_subject(id, data, owner_id)
   - delete_subject(id, owner_id) (soft delete via status)

3. [ ] Implementar API REST (Xano API group)
   - GET /users/{user_id}/subjects
   - POST /users/{user_id}/subjects
   - PUT /subjects/{subject_id}
   - DELETE /subjects/{subject_id}
   - Incluir autenticação JWT e validação de propriedade

4. [ ] Adicionar validações e segurança
   - Sanitização de entrada
   - Rate limiting
   - Logs de auditoria
   - Tratamento de erros

5. [ ] Testes automatizados
   - Testes unitários para funções
   - Testes de integração para APIs
   - Testes de autorização (acesso negado)

6. [ ] Documentação + Exemplo de fluxo
   - README com uso das APIs
   - Exemplos de requests/responses
   - Plano para automações futuras
