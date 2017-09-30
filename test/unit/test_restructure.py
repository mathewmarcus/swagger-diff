from mock import Mock, MagicMock
from swagger_diff.restructure import _resolve_ref

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

def test_resolve_ref_valid():
    category = full_raw_swagger['definitions']['Category']
    
    full_swagger = MagicMock()
    def return_resolved_object(ref):
        return full_raw_swagger['definitions']['Category']

    full_swagger.resolve_fragment = return_resolved_object
    reference = {'$ref': '#/definitions/Category'}
    
    assert _resolve_ref(reference, full_swagger) == category
