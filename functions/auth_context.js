// Helper to extract authenticated user information from request context

function getAuthContext(req) {
  const authSource = req.auth || req.user || {};
  const authId = authSource.id || authSource.user_id || null;
  const authRole = typeof authSource === "string"
    ? authSource
    : authSource.role || authSource.type || null;

  return { authId, authRole };
}

function requireAuthenticatedUser(req, res) {
  const { authId, authRole } = getAuthContext(req);
  const candidateUserId = req.body.user_id || req.query.user_id || null;
  const user_id = authId || candidateUserId;

  if (!user_id) {
    return { error: true, status: 401, message: "Authentication required" };
  }

  // Enforce user_id == auth.id when authId is available
  if (authId && user_id !== authId) {
    return { error: true, status: 403, message: "Access denied" };
  }

  // If auth role is a string and equals "user", assume this is a valid user context
  if (!authId && authRole !== "user") {
    return { error: true, status: 403, message: "Access denied" };
  }

  return { error: false, user_id };
}

module.exports = {
  getAuthContext,
  requireAuthenticatedUser,
};
