// XanoScript-like helper functions for academic tasks CRUD

function get_tasks_for_user(user_id) {
  return db.query(
    "SELECT * FROM academic_tasks WHERE owner_id = ? ORDER BY due_date ASC, priority DESC",
    [user_id]
  );
}

function get_tasks_by_subject(subject_id, user_id) {
  return db.query(
    "SELECT * FROM academic_tasks WHERE subject_id = ? AND owner_id = ? ORDER BY due_date ASC",
    [subject_id, user_id]
  );
}

function get_task_by_id(task_id) {
  return db.query("SELECT * FROM academic_tasks WHERE id = ?", [task_id])[0] || null;
}

function create_task_for_user(user_id, subject_id, data) {
  if (!data || !data.title || !data.title.trim()) {
    throw new Error("Task title is required");
  }

  if (!data.due_date) {
    throw new Error("Due date is required");
  }

  const result = db.query(
    "INSERT INTO academic_tasks (owner_id, subject_id, title, description, due_date, priority, status, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, NOW(), NOW()) RETURNING *",
    [
      user_id,
      subject_id,
      data.title.trim(),
      data.description || null,
      data.due_date,
      data.priority || "medium",
      data.status || "pending",
    ]
  );

  return result[0];
}

function update_task_for_user(task_id, user_id, data) {
  const task = get_task_by_id(task_id);
  if (!task || task.owner_id !== user_id) {
    return null;
  }

  const fields = [];
  const params = [];

  if (data.title !== undefined) {
    if (!data.title || !data.title.trim()) {
      throw new Error("Task title cannot be empty");
    }
    fields.push("title = ?");
    params.push(data.title.trim());
  }

  if (data.description !== undefined) {
    fields.push("description = ?");
    params.push(data.description || null);
  }

  if (data.due_date !== undefined) {
    fields.push("due_date = ?");
    params.push(data.due_date);
  }

  if (data.priority !== undefined) {
    fields.push("priority = ?");
    params.push(data.priority);
  }

  if (data.status !== undefined) {
    fields.push("status = ?");
    params.push(data.status);

    if (data.status === "completed" && !data.completed_at) {
      fields.push("completed_at = NOW()");
    } else if (data.status !== "completed" && data.completed_at === null) {
      fields.push("completed_at = NULL");
    }
  }

  if (data.completed_at !== undefined) {
    fields.push("completed_at = ?");
    params.push(data.completed_at);
  }

  if (fields.length === 0) {
    return task;
  }

  fields.push("updated_at = NOW()");

  db.query(
    `UPDATE academic_tasks SET ${fields.join(", ")} WHERE id = ? AND owner_id = ?`,
    [...params, task_id, user_id]
  );

  return get_task_by_id(task_id);
}

function delete_task_for_user(task_id, user_id) {
  const task = get_task_by_id(task_id);
  if (!task || task.owner_id !== user_id) {
    return false;
  }

  db.query("DELETE FROM academic_tasks WHERE id = ? AND owner_id = ?", [task_id, user_id]);
  return true;
}

function get_overdue_tasks_count(user_id) {
  const result = db.query(
    "SELECT COUNT(*) as count FROM academic_tasks WHERE owner_id = ? AND due_date < NOW() AND status != 'completed'",
    [user_id]
  );
  return result[0]?.count || 0;
}

function get_pending_tasks_count(user_id) {
  const result = db.query(
    "SELECT COUNT(*) as count FROM academic_tasks WHERE owner_id = ? AND status IN ('pending', 'in_progress')",
    [user_id]
  );
  return result[0]?.count || 0;
}

module.exports = {
  get_tasks_for_user,
  get_tasks_by_subject,
  get_task_by_id,
  create_task_for_user,
  update_task_for_user,
  delete_task_for_user,
  get_overdue_tasks_count,
  get_pending_tasks_count,
};
