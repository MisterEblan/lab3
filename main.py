def calculate_sum_with_precision(eps: float) -> tuple[int, float]:
    """Вычисление значения суммы с определённой точностью

    Считает значения суммы до момента, пока |a_i| не станет
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

        if abs(a_k) < eps:
            return k, value

        k += 1

def main() -> None:
    eps = float(input("Ввод >>> "))

    if eps > 1:
        raise ValueError("Погрешность больше единицы не имеет смысла")
    elif eps <= 0:
        raise ValueError("Погрешность меньше или равно нуля не имеет смысла")

    print(f"eps = {eps}")

    i, value = calculate_sum_with_precision(eps)

    print(f"A = {value}")
    print(f"i = {i}")

if __name__ == "__main__":
    main()
