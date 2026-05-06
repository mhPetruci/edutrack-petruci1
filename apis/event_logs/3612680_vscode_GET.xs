// Query all vscode records
query vscode verb=GET {
  api_group = "Event Logs"

  input {
  }

  stack {
    db.query vscode {
      return = {type: "list"}
    } as $vscode
  }

  response = $vscode
}