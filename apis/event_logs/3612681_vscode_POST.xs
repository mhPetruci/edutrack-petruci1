// Add vscode record
query vscode verb=POST {
  api_group = "Event Logs"

  input {
    dblink {
      table = "vscode"
    }
  }

  stack {
    db.add vscode {
      data = {created_at: "now"}
    } as $vscode
  }

  response = $vscode
}