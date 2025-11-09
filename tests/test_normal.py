from main import main
from unittest.mock import patch, MagicMock

@patch("builtins.print")
@patch("builtins.input", return_value="1e-5")
def test_normal(
    mock_input: MagicMock,
    mock_print: MagicMock
) -> None:
    main()

    called_args = [str(c) for c in mock_print.call_args_list]

    assert any(
        "A = 0.29429820134360696" in arg
        for arg in called_args
    ), "Ожидалось, что будет вычислено значение суммы с погрешностью 1e-5"
