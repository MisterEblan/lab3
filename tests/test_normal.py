from main import main
from unittest.mock import patch, MagicMock

@patch("builtins.print")
@patch("builtins.input", return_value="10, 2")
def test_normal(
    mock_input: MagicMock,
    mock_print: MagicMock
) -> None:
    main()

    called_args = [str(c) for c in mock_print.call_args_list]

    assert any(
        "9. 0.29365046490927516" in arg
        for arg in called_args
    ), "Ожидалось, что будет вычислено значение суммы"
