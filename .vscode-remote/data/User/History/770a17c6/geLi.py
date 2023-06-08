from bank import value

def main():
    test_return_zero()
    test_return_20()

def test_return_zero():
    assert value("здравствуйте") == 0
    assert value("здесь") == 20
    assert value("привет") == 100

def test_return_20():
    assert value('Hi') == 20
    assert value('hey') == 20
def test_return_100():
    assert value("Whats up?") == 100
    assert
if __name__ == "__main__":
    main()