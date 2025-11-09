import pytest
from main import main
from unittest.mock import patch, MagicMock

@patch("builtins.print")
@patch("builtins.input", return_value="0")
def test_normal(
    mock_input: MagicMock,
    mock_print: MagicMock
) -> None:
    msg = "Количество членов суммы не может быть меньше или равно нулю"
    with pytest.raises(ValueError, match=msg):
        main()

    mock_input.return_value = "-2"
    with pytest.raises(ValueError, match=msg):
        main()
