const functions = require("../../functions/subjects_crud");
const { requireAuthenticatedUser } = require("../../functions/auth_context");

const authResult = requireAuthenticatedUser(req, res);
if (authResult.error) {
  return res.status(authResult.status).json({ error: authResult.message });
}

const user_id = authResult.user_id;

try {
  const subjects = functions.get_subjects_for_user(user_id);
  return res.status(200).json(subjects);
} catch (error) {
  return res.status(500).json({ error: error.message });
}
