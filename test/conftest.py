
full_raw_swagger = {
    "info": {
        "title": "Swagger Petstore",
        "version": "1.0.0"
    },
    "swagger": "2.0",
    "paths": {
        "/random": {
            "get": {
                "description": "A cute furry animal endpoint.",
                "responses": {
                    "200": {
                        "schema": {
                            "$ref": "#/definitions/Pet"
                        },
                        "description": "A pet to be returned"
                    }
                },
            }
        }
    },
    "definitions": {
        "Pet": {
            "properties": {
                "category": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Category"
                    }
                },
                "name": {
                    "type": "string"
                }
            }
        },
        "Category": {
            "required": [
                "name"
            ],
            "properties": {
                "name": {
                    "type": "string"
                },
                "id": {
                    "type": "integer",
                    "format": "int32"
                }
            }
        }
    },
}
