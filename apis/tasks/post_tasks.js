const functions = require("../../functions/tasks_crud");
const { requireAuthenticatedUser } = require("../../functions/auth_context");

const authResult = requireAuthenticatedUser(req, res);
if (authResult.error) {
  return res.status(authResult.status).json({ error: authResult.message });
}

const user_id = authResult.user_id;
const { subject_id } = req.body;
const payload = req.body;

if (!subject_id) {
  return res.status(400).json({ error: "subject_id is required" });
}

try {
  const task = functions.create_task_for_user(user_id, subject_id, payload);
  return res.status(201).json(task);
} catch (error) {
  return res.status(400).json({ error: error.message });
}
