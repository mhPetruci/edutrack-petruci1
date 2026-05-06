const functions = require("../../functions/tasks_crud");
const { requireAuthenticatedUser } = require("../../functions/auth_context");

const authResult = requireAuthenticatedUser(req, res);
if (authResult.error) {
  return res.status(authResult.status).json({ error: authResult.message });
}

const user_id = authResult.user_id;
const task_id = req.params.task_id;

if (!task_id) {
  return res.status(400).json({ error: "task_id is required" });
}

const deleted = functions.delete_task_for_user(task_id, user_id);
if (!deleted) {
  return res.status(403).json({ error: "Access denied or task not found" });
}

return res.status(204).send();
