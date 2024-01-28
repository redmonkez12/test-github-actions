from money import Dollar


def test_multiplication_2():
    fiver = Dollar(5)
    tenner = fiver.times(2)
    assert tenner.amount == 10


def test_multiplication_4():
    fiver = Dollar(5)
    tenner = fiver.times(4)
    assert tenner.amount == 20
