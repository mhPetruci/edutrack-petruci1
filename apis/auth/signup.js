const userAuth = require("../../functions/user_auth");

const { email, password, name } = req.body;

if (!email || !password) {
  return res.status(400).json({ error: "Email and password are required" });
}

try {
  const user = userAuth.create_user(email, password, name);
  
  // Remove password from response
  const { password: _, ...userWithoutPassword } = user;
  
  const token = userAuth.generate_token(user.id);
  
  return res.status(201).json({
    user: userWithoutPassword,
    token: token.token,
    expires_at: token.expires_at,
  });
} catch (error) {
  return res.status(400).json({ error: error.message });
}
