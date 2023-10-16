# TP-Objet-Connecte

Python code for a calculator, the version 1 depicts the raw use of calculators that does basic operations, the second version have an added feature of memory functionality. we can store a result in memory and recall it for further calculations. Additionally, we've included a clear method to reset the result to zero.

VERSION_1.0
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


VERSION_2.0
class Calculator:
    def __init__(self):
        self.result = 0
        self.memory = 0

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

    def clear(self):
        self.result = 0

    def store_to_memory(self):
        self.memory = self.result

    def recall_from_memory(self):
        self.result = self.memory

    def get_result(self):
        return self.result


if __name__ == "__main__":
    calculator = Calculator()
    calculator.add(5)
    calculator.multiply(3)
    calculator.subtract(2)
    calculator.divide(4)

    calculator.store_to_memory()
    calculator.clear()
    calculator.recall_from_memory()

    print("Result:", calculator.get_result())
