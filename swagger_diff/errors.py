
_errors = {}


def update_errors(canonical_key, message):
    """ Update the global errors dict with a new error

    Args:
       canonical_key (str): canonical key path in the errors dict
       message (str): error message

    Returns:
        None

    Examples:
        >>> from swagger_diff import errors
        >>> print(errors)
        {}
        >>> update_errors('/hello/world/foo/bar', 'Some error message')
        None
        >>> print(errors)
        {'hello': {'world': {'foo': {'bar': 'Some error message'}}}}

    """

    global _errors
    keys = canonical_key.lstrip('/').split('/')
    new_errors = _errors

    for key in keys[:-1]:
        new_errors = new_errors.setdefault(key, {})

    new_errors[keys[-1]] = message
