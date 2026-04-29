# Specs - feature-subjects-search-overdue

## Endpoint
- `GET /subjects/search`
- Query parameters:
  - `name` (string, optional): texto de busca parcial ou completo para o campo `subjects.name`
  - `overdue_tasks` (boolean, optional): quando `true`, incluir disciplinas com tarefas atrasadas

## Behavior
- O endpoint deve retornar apenas disciplinas cujo `owner_id` seja o usuário autenticado.
- Se `name` for fornecido, incluir disciplinas cujo `name` contenha o termo (case-insensitive).
- Se `overdue_tasks=true`, incluir disciplinas que tenham pelo menos uma tarefa acadêmica atrasada.
- A lógica de inclusão deve ser `OR`:
  - disciplinas que correspondam ao filtro de nome,
  - ou disciplinas que tenham tarefas atrasadas.
- Se nenhum filtro for passado, o endpoint deve retornar todas as disciplinas do usuário.

## Python Integration
- Criar uma função Python responsável por avaliar tarefas atrasadas com base em `academic_tasks`:
  - campos esperados: `subject_id`, `due_date`, `completed_at`, `status`
  - condição de atraso: `due_date` no passado e a tarefa ainda não está concluída (`completed_at` vazio ou `status` diferente de `completed`).
- O endpoint REST chamará essa função Python para obter um conjunto de `subject_id` com tarefas atrasadas.
- Em seguida, o endpoint fará a consulta SQL em `subjects` usando esses IDs como parte do filtro.

## Response
- Retornar array JSON de disciplinas com os campos principais:
  - `id`, `name`, `code`, `description`, `status`, `credits`, `semester`, `created_at`, `updated_at`
- Incluir um campo opcional `has_overdue_tasks` quando o filtro `overdue_tasks` estiver ativo.

## Security
- O endpoint deve validar autenticação e garantir que o usuário só acesse os próprios registros.
- Retornar `401 Unauthorized` se a autenticação estiver ausente.
- Retornar `403 Forbidden` se houver tentativa de acessar dados de outro usuário.
