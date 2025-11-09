from collections.abc import Generator

# Escape-последовательности для цвета текста в терминале
GREEN = "\033[32m"
RED   = "\033[31m"
RESET = "\033[0m"

def generate_sum_values(
    n: int,
    k: int
) -> Generator[tuple[int, float]]:
    """Генерирование значений суммы до предела n

    Генерирует значения суммы с верхнем пределом n,
    пропуская каждый k-й член

    Args:
        n: верхний предел суммы.
        k: члены кратные этому числу по индексу
            будут пропускаться.

    Returns:
        индекс и значение суммы при нём.
    """
    value = 0

    for l in range(n):
        a_l = (-1)**l * ( 1 - ( (2**l) / (2**l + 1)  ) )

        value += a_l

        if l % k == 0:
            continue

        yield l, value

def main() -> None:

    n, k = map(
        int,
        input("Введите n и k через запятую >>> ").strip().split(",")
    )

    print(f"n = {n}\nk = {k}")

    check_msg = "n < k? - "
    if n < k:
        print(RED + check_msg + "Да" + RESET)
        return
    else:
        print(GREEN + check_msg + "Нет" + RESET)

    for i, value in generate_sum_values(
        n=n,
        k=k
    ):
        print(f"\t{i:3}. {value}")

if __name__ == "__main__":
    main()
