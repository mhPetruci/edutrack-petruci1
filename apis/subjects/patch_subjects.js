const functions = require("../../functions/subjects_crud");
const { requireAuthenticatedUser } = require("../../functions/auth_context");

const authResult = requireAuthenticatedUser(req, res);
const subject_id = req.params.subject_id;

if (authResult.error) {
  return res.status(authResult.status).json({ error: authResult.message });
}

const user_id = authResult.user_id;

if (!subject_id) {
  return res.status(400).json({ error: "subject_id is required" });
}

try {
  const updated = functions.update_subject_for_user(subject_id, user_id, req.body);
  if (!updated) {
    return res.status(403).json({ error: "Access denied or subject not found" });
  }
  return res.status(200).json(updated);
} catch (error) {
  return res.status(400).json({ error: error.message });
}
