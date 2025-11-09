from collections.abc import Generator

def generate_sum_values(eps: float) -> Generator[tuple[int, float]]:
    """Генерирование значений суммы

    Генерирует значения суммы до момента, пока |a_i| не станет
    меньше погрешности eps.

    Args:
        eps: погрешность.

    Returns:
        индекс и значение суммы при нём.
    """
    value = 0

    k = 0
    while True:
        a_k = (-1)**k * ( 1 - ( (2**k) / (2**k + 1)  ) )

        value += a_k

        yield k, value
        k += 1

        if abs(a_k) < eps:
            break

def main() -> None:
    eps = float(input("Ввод >>> "))

    if eps > 1:
        raise ValueError("Погрешность больше единицы не имеет смысла")
    elif eps <= 0:
        raise ValueError("Погрешность меньше или равно нуля не имеет смысла")

    for i, value in generate_sum_values(eps):
        print(f"{i:3}. {value}")

if __name__ == "__main__":
    main()
