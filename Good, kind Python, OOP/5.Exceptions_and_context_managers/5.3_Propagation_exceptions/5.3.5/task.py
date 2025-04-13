class Test:
    def __init__(self, descr):
        if not 10 <= len(descr) <= 10000:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        self.descr = descr

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)
        if not isinstance(ans_digit, (int, float)) or not isinstance(max_error_digit, (int, float)) or max_error_digit < 0:
            raise ValueError('недопустимые значения аргументов теста')
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def run(self):
        ans = float(input())
        return (self.ans_digit - self.max_error_digit) <= ans <= (self.ans_digit + self.max_error_digit)


descr, ans = map(str.strip, input().split('|'))
ans = float(ans)

try:
    test = TestAnsDigit(descr, ans)
    try:
        result = test.run()
        print(result)
    except Exception as e:
        print(e)
except ValueError as e:
    print(e)
