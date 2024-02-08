from cerberus import Validator

body = {
    "data": {
        "elemento1": 123.45,
        "elemento2": "Olá Mundo!",
        "elemento3": 123,
    }
}

body_schema = Validator({
    "data": {
        "type": "dict",
        "schema": {
            "elemento1": {
                "type": "float",
                "required": True,
                "empty": False
            },
            "elemento2": {
                "type": "string",
                "required": True,
                "empty": True
            },
            "elemento3": {
                "type": "integer",
                "required": True,
                "empty": False
            }
        }
    }
})

response = body_schema.validate(body)

if response:
    print("body ok!")
else:
    print(body_schema.errors)
