from re import match
from six import iteritems
from jsonschema.validators import RefResolver


def resolve_ref(reference, full_swagger):
    """ Convert a JSON Schema reference string into the referenced object

    If `reference` is not in the form {'$ref: :obj:`str`}, return `reference`
    
    Args:
       reference (str): JSON schema $ref value
       full_swagger (:obj:`jsonschema.validators.RefResolver`): the full Swagger schema

    Returns:
        dict: the referenced object

    Examples:

    """

    try:
        ref_value = reference['$ref']
    except (KeyError, TypeError):
        return reference

    if not (isinstance(ref_value, str) and match(r'#(\/[a-zA-Z0-9].+).+', ref_value)):
        return reference

    return full_swagger.resolve(ref_value)[1]
