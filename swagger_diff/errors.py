
_errors = {}


def update_errors(canonical_key, message):
    global _errors
    keys = canonical_key.split('/')
    for key in keys[:-1]:
        _errors = _errors.setdefault(key, {})
    _errors[keys[-1]] = message
