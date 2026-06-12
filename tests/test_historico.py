from unittest.mock import patch
from src.logic.historico import salvar_dia


def test_salvar_dia_supabase():

    with patch("src.logic.historico.get_supabase") as mock_supabase:

        salvar_dia(1500, 2000)

        mock_supabase.return_value.table.assert_called_once_with(
            "historico"
        )

        mock_supabase.return_value.table.return_value.insert.assert_called_once()

        mock_supabase.return_value.table.return_value.insert.return_value.execute.assert_called_once()