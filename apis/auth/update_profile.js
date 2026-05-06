const userAuth = require("../../functions/user_auth");
const { requireAuthenticatedUser } = require("../../functions/auth_context");

const authResult = requireAuthenticatedUser(req, res);
if (authResult.error) {
  return res.status(authResult.status).json({ error: authResult.message });
}

const user_id = authResult.user_id;
const { name } = req.body;

try {
  const updated = userAuth.update_user_profile(user_id, { name });
  if (!updated) {
    return res.status(404).json({ error: "User not found" });
  }

  // Remove password from response
  const { password: _, ...userWithoutPassword } = updated;
  
  return res.status(200).json(userWithoutPassword);
} catch (error) {
  return res.status(400).json({ error: error.message });
}
