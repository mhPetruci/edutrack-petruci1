# Specs de API / DB para Subjects

## Modelo de dados
```jsonc
{
  "subjects": {
    "id": "uuid",
    "owner_id": "uuid",
    "name": "string",
    "code": "string | null",
    "description": "string | null",
    "status": "enum(active, completed, dropped)",
    "credits": "integer | null",
    "semester": "string | null",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
}
```

## Contratos de endpoints (REST)

1. GET /users/{user_id}/subjects
   - Retorna lista de subjects do usuário
   - Resposta 200 JSON: `[ {subject}, ... ]`

2. POST /users/{user_id}/subjects
   - Cria subject para o usuário
   - Input JSON: `{ "name": "String", "code": "String?", "description": "String?", "status": "active", "credits": 4, "semester": "2024-1" }`
   - Resposta 201 JSON: objeto subject criado

3. PUT /subjects/{subject_id}
   - Atualiza subject (validação de owner)
   - Input JSON similar ao POST
   - Resposta 200 JSON: objeto subject atualizado

4. DELETE /subjects/{subject_id}
   - Marca `status=dropped` ou exclui conforme política
   - Resposta 204

## Regras de autorização
- `user_id` Extraído de sessão/token JWT
- Validar `subject.owner_id == user_id` para update/delete
- Manipulação de subject não pertence a outro usuário retorna 403

## Indicadores para automações
- `status` (enum)
- `semester` (string) - para agrupamento
- `credits` (integer) - para cálculos de carga horária
