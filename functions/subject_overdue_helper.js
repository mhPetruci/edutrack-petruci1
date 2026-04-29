const { spawnSync } = require("child_process");
const path = require("path");

function findOverdueSubjectIds(tasks) {
  const scriptPath = path.resolve(__dirname, "../scripts/find_overdue_subject_ids.py");
  const payload = JSON.stringify(tasks || []);
  const result = spawnSync("python", [scriptPath], {
    input: payload,
    encoding: "utf8",
    maxBuffer: 10 * 1024 * 1024,
  });

  if (result.error) {
    throw result.error;
  }

  if (result.status !== 0) {
    const message = result.stderr || result.stdout || "Python helper failed";
    throw new Error(message.trim());
  }

  try {
    return JSON.parse(result.stdout || "[]");
  } catch (error) {
    throw new Error("Invalid JSON returned from overdue task helper");
  }
}

module.exports = {
  findOverdueSubjectIds,
};
