from main import Calculator


class SplitForCalc(Calculator):

    def __init__(self, s):
        self.s = s


    const = 'Hi'

    def make_calc(self):
        s = self.s.split()
        if s[1] == '+':
            print(self.const)
            return self.adding(int(s[0]), int(s[2]))
        elif s[1] == '/':
            return self.division(int(s[0]), int(s[2]))
        else:
            print('This is not correct')
            return 'Это арифметичесткое выражение'


c = Calculator(int(s[0]), int(s[2]))

