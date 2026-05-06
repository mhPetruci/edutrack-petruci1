const userAuth = require("../../functions/user_auth");
const { requireAuthenticatedUser } = require("../../functions/auth_context");

const authResult = requireAuthenticatedUser(req, res);
if (authResult.error) {
  return res.status(authResult.status).json({ error: authResult.message });
}

const user_id = authResult.user_id;

try {
  const user = userAuth.get_user_by_id(user_id);
  if (!user) {
    return res.status(404).json({ error: "User not found" });
  }

  // Remove password from response
  const { password: _, ...userWithoutPassword } = user;
  
  return res.status(200).json(userWithoutPassword);
} catch (error) {
  return res.status(500).json({ error: error.message });
}
