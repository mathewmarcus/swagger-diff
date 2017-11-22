from swagger_diff.errors import update_errors, _errors


def test_errors():
    update_errors('hello/world/foo/bar', 'Some error message')
    assert {'hello': {'world': {'foo': {'bar': 'Some error message'}}}} == _errors
