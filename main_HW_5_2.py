import re

# Генератор, що відбирає числа з аргументу
def generator_numbers(text: str):
    yield re.findall(r' \d+\.\d+ ', text)

# Обчислення суми
def sum_profit(text: str, generator_numbers):
    total = generator_numbers(text)
    for k in total:
        total_s = sum(map(float, k))
    return total_s

# Передання аргументів та запуск функції
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
