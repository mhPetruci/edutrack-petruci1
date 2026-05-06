# Specs - academic_tasks Table Design

## Database Schema

### Table: `academic_tasks`

#### Primary Key
- `id` (UUID)
  - Auto-generated using `gen_random_uuid()`
  - Unique identifier for each task

#### Foreign Keys
- `owner_id` (UUID) → `users.id`
  - Links task to the user who created it
  - ON DELETE: CASCADE (deleting user removes all their tasks)
  - NOT NULL, indexed
  
- `subject_id` (UUID) → `subjects.id`
  - Links task to a specific subject/discipline
  - ON DELETE: CASCADE (deleting subject removes associated tasks)
  - NOT NULL, indexed

#### Core Fields
- `title` (VARCHAR, 255 characters)
  - Task name/description (e.g., "Prova de Cálculo", "Trabalho de Física")
  - NOT NULL
  - CHECK: length > 0 after trim
  - Indexed for search performance

- `description` (TEXT)
  - Detailed information about the task
  - Optional
  - Supports markdown or plain text

- `due_date` (TIMESTAMP)
  - When the task is due
  - NOT NULL
  - Essential for sorting and filtering
  - Indexed for range queries

#### Status & Priority
- `priority` (VARCHAR, 20 characters)
  - Allowed values: 'low', 'medium', 'high'
  - Default: 'medium'
  - NOT NULL
  - Helps users prioritize work

- `status` (VARCHAR, 20 characters)
  - Allowed values: 'pending', 'in_progress', 'completed', 'cancelled'
  - Default: 'pending'
  - NOT NULL
  - CHECK constraint enforces valid values
  - Indexed for filtering

#### Completion Tracking
- `completed_at` (TIMESTAMP)
  - When the task was marked as completed
  - Optional (NULL until completion)
  - Auto-set when status changes to 'completed'

#### Timestamps
- `created_at` (TIMESTAMP)
  - Set to NOW() on insert
  - NOT NULL
  - Immutable

- `updated_at` (TIMESTAMP)
  - Set to NOW() on insert and update
  - NOT NULL
  - Automatically maintained by trigger

## Indexes

1. **idx_tasks_owner_id** (`owner_id`)
   - Purpose: Fetch all tasks for a user
   - Query: "SELECT * FROM academic_tasks WHERE owner_id = ?"
   - Speed: O(log n)

2. **idx_tasks_subject_id** (`subject_id`)
   - Purpose: Fetch tasks for a specific subject
   - Query: "SELECT * FROM academic_tasks WHERE subject_id = ?"
   - Speed: O(log n)

3. **idx_tasks_status** (`status`)
   - Purpose: Filter by task status
   - Query: "SELECT * FROM academic_tasks WHERE status = 'pending'"
   - Speed: O(log n)

4. **idx_tasks_due_date** (`due_date`)
   - Purpose: Sort and filter by deadline
   - Query: "SELECT * FROM academic_tasks WHERE due_date > NOW()"
   - Speed: O(log n)

## Constraints

1. **Primary Key Constraint**
   - Ensures `id` uniqueness

2. **Foreign Key Constraints**
   - `owner_id` → `users.id`: Ensures task belongs to valid user
   - `subject_id` → `subjects.id`: Ensures task belongs to valid subject

3. **NOT NULL Constraints**
   - `title`, `due_date`, `priority`, `status` are required
   - Ensures data completeness

4. **CHECK Constraints**
   - `title`: length(trim(title)) > 0
   - `priority`: priority IN ('low', 'medium', 'high')
   - `status`: status IN ('pending', 'in_progress', 'completed', 'cancelled')

5. **Unique Constraints**
   - None (users can have multiple tasks with same title in different subjects)

## Triggers

1. **update_academic_tasks_updated_at**
   - Event: BEFORE UPDATE
   - Function: Sets `updated_at` to NOW()
   - Purpose: Automatically track modification time

## Data Integrity Rules

1. A task always belongs to exactly one user (owner_id)
2. A task always belongs to exactly one subject (subject_id)
3. If a subject is deleted, its tasks are deleted
4. If a user is deleted, their tasks are deleted
5. `completed_at` should only be set when `status` = 'completed'
6. `due_date` should be in the future at creation time (validated at application layer)

## Query Patterns

### List all tasks for a user (ordered by due date)
```sql
SELECT * FROM academic_tasks 
WHERE owner_id = ? 
ORDER BY due_date ASC
```

### List overdue tasks
```sql
SELECT * FROM academic_tasks 
WHERE owner_id = ? AND due_date < NOW() AND status != 'completed'
```

### List pending tasks for a subject
```sql
SELECT * FROM academic_tasks 
WHERE subject_id = ? AND owner_id = ? AND status = 'pending'
```

### Calculate task completion rate
```sql
SELECT 
  COUNT(CASE WHEN status = 'completed' THEN 1 END) as completed,
  COUNT(*) as total
FROM academic_tasks 
WHERE owner_id = ?
```
