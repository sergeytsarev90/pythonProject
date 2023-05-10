class Calculator:

    def adding(self, q, w):
        print('Сложение')
        return q + w

    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print('Деление на ноль запрещено ')
            return 'На ноль делить нельзя '
        except ValueError:
            print('Не верные данные')
        except TypeError as e:
            return e
