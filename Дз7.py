def safe_calculator(func):
    def wrapper(expression):
        try:
            for char in expression:
                if char not in "0123456789+-*/(). ":
                    return "Помилка: заборонені символи у виразі"
            result = func(expression)
            return f"Результат: {result}"
        except ZeroDivisionError:
            return "Помилка: ділення на нуль"
        except Exception:
            return "Помилка: неправильний вираз"
    return wrapper
@safe_calculator
def calculate(expression):
    return eval(expression)
print(calculate("2 + 3 * 4"))




