# feature-academic-tasks Specification

## Purpose
Definir o esquema e os requisitos para a tabela `academic_tasks`, permitindo que os alunos registrem e gerenciem suas obrigações acadêmicas vinculadas a cada disciplina.

## ADDED Requirements

### Requirement: Create academic_tasks table
The system SHALL store academic tasks with title, description, due_date, status, and subject association.

#### Scenario: Student creates an academic task
- **WHEN** a student creates a new academic task with title, description, due_date, status, and subject_id
- **THEN** the system stores the task and links it to the correct subject

### Requirement: Link academic_tasks to subjects
The system SHALL associate each academic task with a subject via `subject_id`.

#### Scenario: Task linked to subject
- **WHEN** an academic task is created with a valid `subject_id`
- **THEN** the system stores the task reference and ensures the subject exists