const functions = require("../../functions/tasks_crud");
const { requireAuthenticatedUser } = require("../../functions/auth_context");

const authResult = requireAuthenticatedUser(req, res);
if (authResult.error) {
  return res.status(authResult.status).json({ error: authResult.message });
}

const user_id = authResult.user_id;
const { subject_id } = req.query;

try {
  let tasks;
  if (subject_id) {
    tasks = functions.get_tasks_by_subject(subject_id, user_id);
  } else {
    tasks = functions.get_tasks_for_user(user_id);
  }
  return res.status(200).json(tasks);
} catch (error) {
  return res.status(500).json({ error: error.message });
}
