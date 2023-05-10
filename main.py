class Calculator:

    def adding(self, q, w):
        print('Сложение')
        print('Sum')

        return q + w

    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print('Division на ноль запрещено ')
            return 'На ноль делить нельзя '
        except ValueError:
            print('Не верные данные')
            print('Не верные Data')

        except TypeError as e:
            return e
