# feature-calculate-progress Specification

## Purpose
Definir os requisitos para o script Python `scripts/calculate_progress.py`, que calcula o progresso de tarefas como porcentagem de itens concluídos em relação ao total e retorna os dados em formato JSON.

## ADDED Requirements

### Requirement: Calculate progression percentage
The system SHALL calculate task progress as completed divided by total tasks.

#### Scenario: Compute progress for a task list
- **WHEN** a list of tasks is provided with status values
- **THEN** the script computes the total number of tasks and the number of completed tasks
- **THEN** it returns a JSON object with the progress percentage

### Requirement: Return JSON output
The system SHALL return the progress result as a JSON structure.

#### Scenario: Output progress result
- **WHEN** the progress is computed
- **THEN** the script returns JSON with fields for `completed`, `total`, and `progress_percentage`
