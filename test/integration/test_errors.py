from swagger_diff.errors import update_errors, _errors


def test_errors():
    update_errors('hello/world/foo/bar', 'Some error message')
    update_errors('hello/world/foo/baz', 'Another error message')
    assert {'hello': {'world': {'foo': {'bar': 'Some error message', 'baz': 'Another error message'}}}} == _errors
