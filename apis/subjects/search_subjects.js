const functions = require("../../functions/subjects_crud");
const { requireAuthenticatedUser } = require("../../functions/auth_context");
const { findOverdueSubjectIds } = require("../../functions/subject_overdue_helper");

const authResult = requireAuthenticatedUser(req, res);
if (authResult.error) {
  return res.status(authResult.status).json({ error: authResult.message });
}

const user_id = authResult.user_id;
const name = typeof req.query.name === "string" ? req.query.name.trim() : null;
const overdueTasksFlag = String(req.query.overdue_tasks).toLowerCase() === "true";

let overdueSubjectIds = [];
if (overdueTasksFlag) {
  try {
    const tasks = functions.get_academic_tasks_for_user(user_id);
    overdueSubjectIds = findOverdueSubjectIds(tasks);
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
}

try {
  const subjects = functions.search_subjects_for_user(user_id, {
    name,
    overdueSubjectIds,
  });

  const subjectSet = new Set(overdueSubjectIds);
  const response = subjects.map((subject) => ({
    ...subject,
    has_overdue_tasks: subjectSet.has(subject.id),
  }));

  return res.status(200).json(response);
} catch (error) {
  return res.status(500).json({ error: error.message });
}
