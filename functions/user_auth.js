// User authentication helper functions

function hash_password(password) {
  // In a real scenario, use bcrypt: require('bcryptjs').hashSync(password, 10)
  // For now, using a placeholder that should be replaced with proper hashing
  const crypto = require('crypto');
  return crypto.createHash('sha256').update(password).digest('hex');
}

function verify_password(password, hash) {
  // In a real scenario, use bcrypt: require('bcryptjs').compareSync(password, hash)
  return hash_password(password) === hash;
}

function generate_token(user_id, expiresIn = 3600) {
  // Placeholder for JWT generation
  // In production: require('jsonwebtoken').sign({ user_id }, SECRET_KEY, { expiresIn })
  const crypto = require('crypto');
  const token = crypto.randomBytes(32).toString('hex');
  const payload = {
    user_id,
    token,
    issued_at: Math.floor(Date.now() / 1000),
    expires_at: Math.floor(Date.now() / 1000) + expiresIn,
  };
  return payload;
}

function get_user_by_email(email) {
  if (!email || !email.trim()) {
    throw new Error("Email is required");
  }

  const result = db.query(
    "SELECT * FROM users WHERE LOWER(email) = LOWER(?)",
    [email.trim()]
  );
  return result[0] || null;
}

function get_user_by_id(user_id) {
  return db.query("SELECT * FROM users WHERE id = ?", [user_id])[0] || null;
}

function create_user(email, password, name = null) {
  if (!email || !email.trim()) {
    throw new Error("Email is required");
  }

  if (!password || password.length < 6) {
    throw new Error("Password must be at least 6 characters");
  }

  const existing = get_user_by_email(email);
  if (existing) {
    throw new Error("Email already registered");
  }

  const hashedPassword = hash_password(password);

  const result = db.query(
    "INSERT INTO users (email, password, name, created_at, updated_at) VALUES (?, ?, ?, NOW(), NOW()) RETURNING *",
    [email.trim(), hashedPassword, name || null]
  );

  return result[0];
}

function update_user_profile(user_id, data) {
  const user = get_user_by_id(user_id);
  if (!user) {
    return null;
  }

  const fields = [];
  const params = [];

  if (data.name !== undefined) {
    fields.push("name = ?");
    params.push(data.name || null);
  }

  if (fields.length === 0) {
    return user;
  }

  fields.push("updated_at = NOW()");

  db.query(
    `UPDATE users SET ${fields.join(", ")} WHERE id = ?`,
    [...params, user_id]
  );

  return get_user_by_id(user_id);
}

module.exports = {
  hash_password,
  verify_password,
  generate_token,
  get_user_by_email,
  get_user_by_id,
  create_user,
  update_user_profile,
};
