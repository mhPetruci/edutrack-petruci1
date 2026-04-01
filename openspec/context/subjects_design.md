# Design de Subjects (Disciplinas)

## Objetivo
Criar a base de dados e o fluxo de gestão de disciplinas (subjects) vinculadas a usuários, com controle de propriedade, integridade referencial e suporte a automações futuras.

## Entidades
- users
  - id (PK)
  - username
  - email
  - created_at
- subjects
  - id (PK)
  - owner_id (FK -> users.id)
  - name
  - code
  - description
  - status (active/completed/dropped)
  - credits
  - semester
  - created_at
  - updated_at

## Relacionamentos
- users 1..n subjects
- Cada subject pertence a um único owner_id

## Regras de negócio
1. O campo `name` de subject é obrigatório
2. Cada usuário só vê/gerencia suas próprias subjects
3. `status` controla visibilidade e automações (apenas ativos por padrão)
4. Criação/atualização deve ajustar `updated_at`

## Evolução
- Adicionar tarefas agendadas para nudge de estudo (via `status` e `due_date`)
- API REST / GraphQL para criar, ler, atualizar, deletar disciplines
- Permitir multi-categoria, tags, carga horária, semestres
