from jsonschema import RefResolver
from swagger_diff.restructure import resolve_ref
from test.conftest import full_raw_swagger

full_swagger = RefResolver.from_schema(full_raw_swagger)


def test_valid():
    reference = {'$ref': '#/definitions/Category'}    
    category = full_raw_swagger['definitions']['Category']
    
    assert resolve_ref(reference, full_swagger) == category
    
