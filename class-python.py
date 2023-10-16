class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num

    def subtract(self, num):
        self.result -= num

    def multiply(self, num):
        self.result *= num

    def divide(self, num):
        if num != 0:
            self.result /= num
        else:
            return "Cannot divide by zero."

    def get_result(self):
        return self.result


if __name__ == "__main__":
    calculator = Calculator()
    calculator.add(5)
    calculator.multiply(3)
    calculator.subtract(2)
    calculator.divide(4)

    print("Result:", calculator.get_result())
