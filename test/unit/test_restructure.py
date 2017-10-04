from mock import Mock, MagicMock
from swagger_diff.restructure import resolve_ref
from test.conftest import full_raw_swagger


def test_resolve_ref_valid():
    category = full_raw_swagger['definitions']['Category']
    reference = {'$ref': '#/definitions/Category'}    
    
    full_swagger = MagicMock()
    def return_resolved_object(ref):
        return (reference, full_raw_swagger['definitions']['Category'])

    full_swagger.resolve = return_resolved_object
    
    assert resolve_ref(reference, full_swagger) == category


def test_resolve_ref_invalid_regex():
    category = full_raw_swagger['definitions']['Category']
    full_swagger = MagicMock()
    reference = {'$ref': '#definitionsCategory'}
    
    assert resolve_ref(reference, full_swagger) == reference


def test_resolve_ref_invalid_ref_type():
    category = full_raw_swagger['definitions']['Category']
    full_swagger = MagicMock()
    reference = {'$ref': []}
    
    assert resolve_ref(reference, full_swagger) == reference


def test_resolve_ref_missing_ref_key():
    category = full_raw_swagger['definitions']['Category']
    full_swagger = MagicMock()
    reference = {'foobar': '#/definitions/Category'}
    
    assert resolve_ref(reference, full_swagger) == reference


def test_resolve_ref_invalid_type():
    category = full_raw_swagger['definitions']['Category']
    full_swagger = MagicMock()
    reference = '$ref'
    
    assert resolve_ref(reference, full_swagger) == reference
