const userAuth = require("../../functions/user_auth");

const { email, password } = req.body;

if (!email || !password) {
  return res.status(400).json({ error: "Email and password are required" });
}

try {
  const user = userAuth.get_user_by_email(email);
  
  if (!user || !userAuth.verify_password(password, user.password)) {
    return res.status(401).json({ error: "Invalid email or password" });
  }

  const token = userAuth.generate_token(user.id);
  
  // Remove password from response
  const { password: _, ...userWithoutPassword } = user;

  return res.status(200).json({
    user: userWithoutPassword,
    token: token.token,
    expires_at: token.expires_at,
  });
} catch (error) {
  return res.status(400).json({ error: error.message });
}
