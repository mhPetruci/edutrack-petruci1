// Delete vscode record.
query "vscode/{vscode_id}" verb=DELETE {
  api_group = "Event Logs"

  input {
    int vscode_id? filters=min:1
  }

  stack {
    db.del vscode {
      field_name = "id"
      field_value = $input.vscode_id
    }
  }

  response = null
}