class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, times):
        return Dollar(times * self.amount)


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def times(self, multiplier):
        return Money(self.amount * multiplier. self.currency)