# Tasks - feature-academic-tasks

## Implementation Tasks

### Phase 1: Database Setup
- [ ] Create `academic_tasks` table in database
- [ ] Add all fields and constraints as specified
- [ ] Create indexes on owner_id, subject_id, status, due_date
- [ ] Create trigger for automatic updated_at maintenance
- [ ] Verify foreign key relationships with users and subjects tables
- [ ] Test constraint enforcement (NOT NULL, CHECK, unique, FK)

### Phase 2: Backend Functions (CRUD)
- [ ] Create `get_tasks_for_user(user_id)` function
- [ ] Create `get_tasks_by_subject(subject_id, user_id)` function
- [ ] Create `get_task_by_id(task_id, user_id)` function
- [ ] Create `create_task(user_id, subject_id, data)` function with validation
- [ ] Create `update_task(task_id, user_id, data)` function
- [ ] Create `delete_task(task_id, user_id)` function
- [ ] Create `mark_task_completed(task_id, user_id)` function
- [ ] Create helper functions for analytics (overdue count, completion rate)

### Phase 3: API Endpoints
- [ ] `POST /tasks` — create new task
- [ ] `GET /tasks` — list all user tasks (with optional filters)
- [ ] `GET /tasks/:id` — get single task details
- [ ] `PATCH /tasks/:id` — update task fields
- [ ] `DELETE /tasks/:id` — delete task
- [ ] `POST /tasks/:id/complete` — mark as completed
- [ ] `GET /tasks/stats` — get task statistics (pending, overdue, completed)
- [ ] `GET /tasks/by-subject/:subject_id` — list tasks for a subject

### Phase 4: Frontend Integration
- [ ] Create task listing page
- [ ] Create task creation form
- [ ] Create task editing interface
- [ ] Implement task status toggle
- [ ] Add priority and status filters
- [ ] Add deadline warning indicators
- [ ] Implement task search/search
- [ ] Show overdue tasks with visual warning

### Phase 5: Testing
- [ ] Unit tests for CRUD functions
- [ ] Integration tests for API endpoints
- [ ] Test authorization (user can only access own tasks)
- [ ] Test data validation
- [ ] Test constraint enforcement
- [ ] Test cascade delete behavior
- [ ] Performance tests (large dataset handling)
- [ ] Edge case tests (invalid dates, duplicate titles, etc.)

### Phase 6: Documentation
- [ ] Document API endpoints with examples
- [ ] Create user guide for task management
- [ ] Add troubleshooting section
- [ ] Document data migration process (if applicable)

## Acceptance Criteria

### User Stories

#### Story 1: Create Task
- **As a** student
- **I want to** create a new academic task/obligation
- **So that** I can keep track of my assignments

**Acceptance Criteria:**
- [ ] Can specify title, description, due_date, priority, subject
- [ ] Task is linked to the correct subject
- [ ] Task is linked to the authenticated user
- [ ] Default status is 'pending'
- [ ] Validation prevents empty titles
- [ ] System prevents due_date in the past (optional, app layer)

#### Story 2: List Tasks
- **As a** student
- **I want to** see all my academic tasks
- **So that** I can organize my work

**Acceptance Criteria:**
- [ ] Retrieve only tasks owned by authenticated user
- [ ] Display tasks sorted by due_date (ascending)
- [ ] Show task title, subject, due_date, priority, status
- [ ] Filter by subject, status, or priority
- [ ] Highlight overdue tasks

#### Story 3: Update Task
- **As a** student
- **I want to** modify task details
- **So that** I can keep information accurate

**Acceptance Criteria:**
- [ ] Can update title, description, due_date, priority, status
- [ ] Cannot update other users' tasks
- [ ] Automatic timestamp update on modification
- [ ] Validation on all fields

#### Story 4: Complete Task
- **As a** student
- **I want to** mark a task as completed
- **So that** I can track my progress

**Acceptance Criteria:**
- [ ] Status changes to 'completed'
- [ ] `completed_at` timestamp is set to NOW()
- [ ] Cannot mark others' tasks as complete
- [ ] Task remains visible but marked as done

#### Story 5: Delete Task
- **As a** student
- **I want to** remove a task
- **So that** I can manage my task list

**Acceptance Criteria:**
- [ ] Can only delete own tasks
- [ ] Deletion is permanent
- [ ] No orphaned references remain
- [ ] Deleting subject deletes its tasks (cascade)

## Success Metrics

- ✅ All CRUD operations working
- ✅ Zero data corruption issues
- ✅ Proper authorization enforcement
- ✅ Response times < 200ms for typical queries
- ✅ 100% test coverage for core functions
- ✅ No broken foreign key constraints
