import pytest
from main import main
from unittest.mock import patch, MagicMock

@patch("builtins.print")
@patch("builtins.input", return_value="19")
def test_normal(
    mock_input: MagicMock,
    mock_print: MagicMock
) -> None:
    msg = "Погрешность больше единицы не имеет смысла"
    with pytest.raises(ValueError, match=msg):
        main()

    mock_input.return_value = "0"
    msg = "Погрешность меньше или равно нуля не имеет смысла"
    with pytest.raises(ValueError, match=msg):
        main()

    mock_input.return_value = "-3"
    with pytest.raises(ValueError, match=msg):
        main()
