from collections.abc import Generator

def generate_sum_values(n: int) -> Generator[tuple[int, float]]:
    """Генерирование значений суммы

    Args:
        n: верхний предел суммы.

    Returns:
        индекс и значение суммы при нём.
    """
    value = 0
    for k in range(n):
        a_k = (-1)**k * ( 1 - ( (2**k) / (2**k + 1)  ) )
        value += a_k

        yield k, value

def main() -> None:
    if (n := int(input("Ввод >>> "))) <= 0:
        raise ValueError(
            "Количество членов суммы не может быть меньше или равно нулю"
        )

    print(f"n = {n}")

    for i, value in generate_sum_values(n):
        print(f"{i}. {value:.4}")


if __name__ == "__main__":
    main()
