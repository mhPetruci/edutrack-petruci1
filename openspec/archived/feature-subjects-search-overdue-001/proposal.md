# feature-subjects-search-overdue Proposal

## Why
Usuários precisam buscar disciplinas de forma mais inteligente: por nome ou por tarefas associadas que já estão atrasadas.

Um endpoint de pesquisa unificado melhora a experiência, permitindo consulta por texto livre e também a descoberta rápida de disciplinas que demandam atenção imediata.

## What Changes
- Adicionar endpoint `GET /subjects/search` com filtros:
  - `name` — pesquisa por nome de disciplina
  - `overdue_tasks=true` — busca disciplinas que têm tarefas atrasadas
- Integrar lógica Python para identificar `subjects` com tarefas atrasadas a partir da base de tarefas acadêmicas.
- Garantir que a pesquisa seja feita apenas sobre disciplinas do usuário autenticado.
- Implementar a seleção lógica `OR`: retornar disciplinas cujo nome case com o filtro `name` ou que tenham tarefas atrasadas.

## Impact
- Permite pesquisa combinada e descoberta orientada por prioridade.
- Reforça controle de acesso por usuário.
- Cria um ponto de integração entre o backend JS/REST e lógica Python especializada.
- Prepara o sistema para futuras melhorias de recomendação e alertas de estudos.
