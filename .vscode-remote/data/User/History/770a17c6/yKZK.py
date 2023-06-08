from bank import value

def test_value():
    assert value("здравствуйте") == 0
    assert value("здесь") == 20
    assert value("привет") == 100
