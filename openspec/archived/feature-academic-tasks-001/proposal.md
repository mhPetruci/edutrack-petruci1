# feature-academic-tasks Proposal

## Why
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
