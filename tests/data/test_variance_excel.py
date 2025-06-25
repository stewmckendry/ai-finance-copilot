"""Unit tests for variance spreadsheet parser."""

import pathlib
import sys

import pandas as pd

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))

from app.data.variance_excel import parse_variance


def test_parse_variance_xlsx(tmp_path: pathlib.Path) -> None:
    """Excel file is parsed into a list of row dictionaries."""
    df = pd.DataFrame(
        {
            "department": ["Finance", "Finance"],
            "program": ["ProgramA", "ProgramB"],
            "account": ["Acct1", "Acct2"],
            "budget": [1000, 2000],
            "actual": [800, 2100],
            "variance": [200, -100],
        }
    )
    sample_path = tmp_path / "sample.xlsx"
    df.to_excel(sample_path, index=False)

    rows = parse_variance.fn(str(sample_path))

    assert len(rows) == 2
    assert rows[0]["department"] == "Finance"
    assert rows[0]["budget"] == 1000
    assert rows[1]["variance"] == -100
