const functions = require("../../functions/tasks_crud");
const { requireAuthenticatedUser } = require("../../functions/auth_context");

const authResult = requireAuthenticatedUser(req, res);
if (authResult.error) {
  return res.status(authResult.status).json({ error: authResult.message });
}

const user_id = authResult.user_id;

try {
  const pendingCount = functions.get_pending_tasks_count(user_id);
  const overdueCount = functions.get_overdue_tasks_count(user_id);
  
  return res.status(200).json({
    pending: pendingCount,
    overdue: overdueCount,
  });
} catch (error) {
  return res.status(500).json({ error: error.message });
}
