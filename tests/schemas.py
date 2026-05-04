login_schema = {
    "type": "object",
    "properties": {
        "status": {"type": "string"},
        "status_code": {"type": "integer"},
        "message": {"type": "string"},
        "data": {
            "type": "object",
            "properties": {
                "access_token": {"type": "string"},
                "access_token_expires_in": {"type": "string"},
                "user": {"type": "object"},
                "user_id": {"type": "string"}
            },
            "required": ["access_token"]
        }
    },
    "required": ["status", "data"]
}


error_schema = {
    "type": "object",
    "properties": {
        "status": {"type": "string"},
        "status_code": {"type": "integer"},
        "message": {"type": "string"}
    },
    "required": ["status", "message"]
}