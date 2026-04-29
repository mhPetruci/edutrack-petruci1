// XanoScript-like helper functions for subjects CRUD

function get_subjects_for_user(user_id) {
  return db.query(
    "SELECT * FROM subjects WHERE owner_id = ? ORDER BY name",
    [user_id]
  );
}

function get_academic_tasks_for_user(user_id) {
  return db.query(
    "SELECT subject_id, due_date, completed_at, status FROM academic_tasks WHERE owner_id = ?",
    [user_id]
  );
}

function get_subject_by_id(subject_id) {
  return db.query("SELECT * FROM subjects WHERE id = ?", [subject_id])[0] || null;
}

function create_subject_for_user(user_id, data) {
  if (!data || !data.name || !data.name.trim()) {
    throw new Error("Subject name is required");
  }

  const result = db.query(
    "INSERT INTO subjects (owner_id, name, code, description, status, credits, semester, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, NOW(), NOW()) RETURNING *",
    [
      user_id,
      data.name.trim(),
      data.code || null,
      data.description || null,
      data.status || "active",
      data.credits || null,
      data.semester || null,
    ]
  );

  return result[0];
}

function update_subject_for_user(subject_id, user_id, data) {
  const subject = get_subject_by_id(subject_id);
  if (!subject || subject.owner_id !== user_id) {
    return null;
  }

  const fields = [];
  const params = [];

  if (data.name !== undefined) {
    if (!data.name || !data.name.trim()) {
      throw new Error("Subject name cannot be empty");
    }
    fields.push("name = ?");
    params.push(data.name.trim());
  }
  if (data.code !== undefined) {
    fields.push("code = ?");
    params.push(data.code || null);
  }
  if (data.description !== undefined) {
    fields.push("description = ?");
    params.push(data.description || null);
  }
  if (data.status !== undefined) {
    fields.push("status = ?");
    params.push(data.status);
  }
  if (data.credits !== undefined) {
    fields.push("credits = ?");
    params.push(data.credits);
  }
  if (data.semester !== undefined) {
    fields.push("semester = ?");
    params.push(data.semester || null);
  }

  if (fields.length === 0) {
    return subject;
  }

  fields.push("updated_at = NOW()");

  db.query(
    `UPDATE subjects SET ${fields.join(", ")} WHERE id = ? AND owner_id = ?`,
    [...params, subject_id, user_id]
  );

  return get_subject_by_id(subject_id);
}

function delete_subject_for_user(subject_id, user_id) {
  const subject = get_subject_by_id(subject_id);
  if (!subject || subject.owner_id !== user_id) {
    return false;
  }

  db.query("DELETE FROM subjects WHERE id = ? AND owner_id = ?", [subject_id, user_id]);
  return true;
}

function search_subjects_for_user(user_id, options = {}) {
  const name = options.name ? options.name.trim().toLowerCase() : null;
  const overdueSubjectIds = Array.isArray(options.overdueSubjectIds) ? options.overdueSubjectIds : [];

  if (!name && overdueSubjectIds.length === 0) {
    return get_subjects_for_user(user_id);
  }

  const filters = [];
  const params = [user_id];

  if (name) {
    filters.push("LOWER(name) LIKE ?");
    params.push(`%${name}%`);
  }

  if (overdueSubjectIds.length > 0) {
    const placeholders = overdueSubjectIds.map(() => "?").join(", ");
    filters.push(`id IN (${placeholders})`);
    params.push(...overdueSubjectIds);
  }

  const clause = filters.length === 1 ? filters[0] : `(${filters.join(" OR ")})`;
  const query = `SELECT * FROM subjects WHERE owner_id = ? AND ${clause} ORDER BY name`;
  return db.query(query, params);
}

module.exports = {
  get_subjects_for_user,
  create_subject_for_user,
  update_subject_for_user,
  delete_subject_for_user,
  get_academic_tasks_for_user,
  search_subjects_for_user,
};
