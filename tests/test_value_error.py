from main import main
from unittest.mock import patch, MagicMock

@patch("builtins.print")
@patch("builtins.input", return_value="2, 5")
def test_normal(
    mock_input: MagicMock,
    mock_print: MagicMock
) -> None:
    msg = "n < k? - Да"
    main()

    assert any(
        msg in str(arg)
        for arg in mock_print.call_args_list
    )
