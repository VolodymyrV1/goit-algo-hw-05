# Створюємо декоратор, що буде обробляти помилки
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            return "Your need enter number!"
    return inner 

# Створюємо основну функцію aching_fibonacci
def caching_fibonacci():
    # Створюємо пустий словник
    cache = {}
    # Добавляємо декоратор
    @input_error 
    # Створює функцію, яка буде обраховувати та додавати в словник та перевіряти наявність
    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n] 

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
print(fib('dsd')) # Перевірка декоратора. Виведе Your need enter number!

    