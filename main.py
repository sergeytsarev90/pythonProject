class Calculator:

    def adding(self, a, b):
        return a + b

    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'На ноль делить нельзя '
        except ValueError:
            print('Не корректные данные')
        except TypeError as e:
            return e
