import math
import sys


def is_perfect_square(x: int) -> bool:
    if x < 0:
        return False
    root = math.isqrt(x)
    return root * root == x


def is_fibonacci(n: int) -> bool:
    if n < 0:
        return False
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


def fibonacci(n: int) -> int:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Индекс n должен быть целым числом.")
    if n < 0:
        raise ValueError("Индекс n не может быть отрицательным.")

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    # Можно передать число аргументом в терминале: python fibonacci.py 10
    raw = sys.argv[1] if len(sys.argv) > 1 else input("Введите целое число >= 0: ").strip()
    try:
        num = int(raw)
        if num < 0:
            print("Ошибка: число должно быть >= 0.")
            sys.exit(1)
        print(f"F({num}) = {fibonacci(num)}")
        print(f"Входит в ряд Фибоначчи: {'Да' if is_fibonacci(num) else 'Нет'}")
    except ValueError:
        print("Ошибка: введите корректное целое число.")
        sys.exit(1)

