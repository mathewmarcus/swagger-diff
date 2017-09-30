from re import match
from six import iteritems
from jsonschema.validators import RefResolver


def nest(flat_schema):
    full_swagager = RefResolver.from_schema(flat_schema)
    return _nest_helper(flat_schema, {}, full_swagger)


def _nest_helper(flat_schema, nested_schema, full_swagger):
    for key, value in iteritems(flat_schema):
        if isinstance(value, dict):
            nested_schema[key] = resolve_ref(value, full_swagger)
            self._nest_helper(flat_schema[key], nested_schema[key], full_swagger)
        elif isinstance(value, list) and all(isinstance(item, dict) for item in value):
            nested_schema[key] = (resolve_ref(param, full_swagger) for param in value)
            for index, item in enumerate(nested_schema[key]):
                self._nest_helper(flat_schema[key][index], nested_schema[key][index], full_swagger)
        else:
            nested_schema[key] = value

    return nested_schema


def _resolve_ref(reference, full_swagger):
    """ Convert a JSON Schema reference string into the referenced object

    If `reference` is not in the form {'$ref: :obj:`str`}, return `reference`
    
    Args:
       reference (str): JSON schema $ref value
       full_swagger (:obj:`jsonschema.validators.RefResolver`): the full Swagger schema

    Returns:
        dict: the referenced object

    Raises:
        Exception: reference string is invalid

    Examples:

    """

    try:
        ref_value = reference['$ref']
    except KeyError:
        return reference

    print(ref_value)
    if not (isinstance(ref_value, str) and match(r'#(\/[a-zA-Z0-9].+).+', ref_value)):
        return reference

    return full_swagger.resolve_fragment(ref_value.lstrip('#'))
