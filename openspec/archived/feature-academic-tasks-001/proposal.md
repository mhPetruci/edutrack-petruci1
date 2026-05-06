# feature-academic-tasks Proposal

## Why
<<<<<<< HEAD
Os alunos precisam registrar e gerenciar suas obrigações acadêmicas (lições, provas, trabalhos, projetos) de forma centralizada e vinculada às disciplinas. Um sistema de gestão de tarefas permite:

- Acompanhar prazos e prioridades
- Visualizar carga de trabalho por disciplina
- Identificar conflitos de prazos
- Calcular progresso acadêmico
- Receber alertas de tarefas vencidas

## What Changes
- Criar tabela `academic_tasks` no banco de dados
- Definir schema com campos obrigatórios e opcionais
- Estabelecer relacionamento com tabela `subjects` (foreign key)
- Criar índices para otimizar queries de listagem e filtro
- Implementar triggers para atualização automática de timestamps

## Schema Overview
```
academic_tasks
├── id (UUID, PK)
├── owner_id (UUID, FK → users.id)
├── subject_id (UUID, FK → subjects.id)
├── title (VARCHAR, required)
├── description (TEXT)
├── due_date (TIMESTAMP, required)
├── priority (VARCHAR: low/medium/high)
├── status (VARCHAR: pending/in_progress/completed/cancelled)
├── completed_at (TIMESTAMP, nullable)
├── created_at (TIMESTAMP)
└── updated_at (TIMESTAMP)
```

## Impact
- **Baixo risco**: tabela isolada, sem alterar dados existentes
- **Performance**: índices em owner_id, subject_id, status, due_date
- **Escalabilidade**: suporta milhões de tarefas com queries otimizadas
- **Integridade**: foreign keys e constraints garantem consistência
=======
Os alunos precisam registrar e gerenciar suas obrigações acadêmicas (lições, provas, trabalhos) de forma organizada e vinculada à disciplina correspondente. Sem essa funcionalidade, não há um lugar único para controlar prazos, status e relacionamento entre tarefas e subjects.

## What Changes
Será adicionada a nova tabela `academic_tasks` para armazenar as obrigações acadêmicas dos alunos. O esquema incluirá os campos `title`, `description`, `due_date`, `status` e `subject_id` para referenciar a disciplina. Esta mudança permitirá que o sistema vincule cada obrigação a uma disciplina existente.

## Impact
- **Baixo risco**: funcionalidade isolada como nova tabela de dados.
- **Compatibilidade**: não altera a tabela `subjects`, apenas estabelece uma referência a ela.
- **Usuários afetados**: alunos, que poderão gerenciar tarefas acadêmicas, e o backend, que passará a suportar essa nova entidade.
- **Evolução**: prepara o caminho para futuras funcionalidades como notificações de prazo, filtros por status e relatórios de pendências.
>>>>>>> 3d755528621c54d0b7806704a438b276fa0f9707
