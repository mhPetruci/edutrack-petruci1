# feature-academic-tasks Proposal

## Why
Os alunos precisam registrar e gerenciar suas obrigações acadêmicas (lições, provas, trabalhos) de forma organizada e vinculada à disciplina correspondente. Sem essa funcionalidade, não há um lugar único para controlar prazos, status e relacionamento entre tarefas e subjects.

## What Changes
Será adicionada a nova tabela `academic_tasks` para armazenar as obrigações acadêmicas dos alunos. O esquema incluirá os campos `title`, `description`, `due_date`, `status` e `subject_id` para referenciar a disciplina. Esta mudança permitirá que o sistema vincule cada obrigação a uma disciplina existente.

## Impact
- **Baixo risco**: funcionalidade isolada como nova tabela de dados.
- **Compatibilidade**: não altera a tabela `subjects`, apenas estabelece uma referência a ela.
- **Usuários afetados**: alunos, que poderão gerenciar tarefas acadêmicas, e o backend, que passará a suportar essa nova entidade.
- **Evolução**: prepara o caminho para futuras funcionalidades como notificações de prazo, filtros por status e relatórios de pendências.