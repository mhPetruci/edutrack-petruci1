// Get vscode record
query "vscode/{vscode_id}" verb=GET {
  api_group = "Event Logs"

  input {
    int vscode_id? filters=min:1
  }

  stack {
    db.get vscode {
      field_name = "id"
      field_value = $input.vscode_id
    } as $vscode
  
    precondition ($vscode != null) {
      error_type = "notfound"
      error = "Not Found."
    }
  }

  response = $vscode
}