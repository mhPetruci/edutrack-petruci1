# feature-subjects-crud Specification

## Purpose
Definir requisitos para endpoints CRUD de `subjects` que permitam ao usuário criar, listar, atualizar e excluir suas próprias disciplinas, garantindo controle de acesso baseado em propriedade.

## ADDED Requirements

### Requirement: Subjects CRUD endpoints
The system SHALL provide POST, GET, PATCH, and DELETE endpoints for subject management.

#### Scenario: Create a new subject
- **WHEN** a user sends a POST request with valid subject data
- **THEN** the system creates the subject and associates it with the authenticated user

#### Scenario: List only user subjects
- **WHEN** a user requests GET /subjects
- **THEN** the system returns only subjects belonging to that user

#### Scenario: Update a subject owned by the user
- **WHEN** a user sends PATCH /subjects/{subject_id} with updated fields
- **THEN** the system updates the subject only if it belongs to that user

#### Scenario: Prevent updating a subject owned by another user
- **WHEN** a user sends PATCH /subjects/{subject_id} for a subject they do not own
- **THEN** the system returns a 403 Forbidden error

#### Scenario: Delete a user-owned subject
- **WHEN** a user sends DELETE /subjects/{subject_id}
- **THEN** the system deletes the subject only if it belongs to that user

#### Scenario: Prevent deleting a subject owned by another user
- **WHEN** a user sends DELETE /subjects/{subject_id} for a subject they do not own
- **THEN** the system returns a 403 Forbidden error

### Requirement: Authorization by authenticated user
The system SHALL validate the authenticated user's identity for each CRUD request and enforce that subject operations are restricted to the owner.

#### Scenario: Authorization enforced on subject operations
- **WHEN** a subject CRUD request is received
- **THEN** the system verifies the request user against `subject.owner_id`
- **THEN** it allows the operation only if the user is the owner
