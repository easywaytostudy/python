
class Condition(object):
    where = []

    def __init__(self, column, test, value):
        self.where.append({'col':column, 'test':test, 'value': value})
