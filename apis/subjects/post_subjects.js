const functions = require("../../functions/subjects_crud");
const { requireAuthenticatedUser } = require("../../functions/auth_context");

const authResult = requireAuthenticatedUser(req, res);
const payload = req.body;

if (authResult.error) {
  return res.status(authResult.status).json({ error: authResult.message });
}

const user_id = authResult.user_id;

try {
  const subject = functions.create_subject_for_user(user_id, payload);
  return res.status(201).json(subject);
} catch (error) {
  return res.status(400).json({ error: error.message });
}
