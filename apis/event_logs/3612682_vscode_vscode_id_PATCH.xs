// Edit vscode record
query "vscode/{vscode_id}" verb=PATCH {
  api_group = "Event Logs"

  input {
    int vscode_id? filters=min:1
    dblink {
      table = "vscode"
    }
  }

  stack {
    util.get_raw_input {
      encoding = "json"
      exclude_middleware = false
    } as $raw_input
  
    db.patch vscode {
      field_name = "id"
      field_value = $input.vscode_id
      data = `$input|pick:($raw_input|keys)`|filter_null|filter_empty_text
    } as $vscode
  }

  response = $vscode
}