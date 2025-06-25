"""Tests for reconcile_budget variance computation."""

import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))

from app.analysis.variance import reconcile_budget


def test_reconcile_budget() -> None:
    sample_path = pathlib.Path(__file__).resolve().parents[2] / "samples" / "mock_variance_input.json"
    with open(sample_path) as f:
        data = json.load(f)

    result = reconcile_budget(data)

    by_account = {v["account"]: v for v in result["variance"]}

    assert by_account["A"]["variance_amount"] == -1000
    assert by_account["A"]["variance_pct"] == -10.0
    assert by_account["A"]["flag"] == "under"

    assert by_account["B"]["variance_amount"] == 2000
    assert by_account["B"]["variance_pct"] == 10.0
    assert by_account["B"]["flag"] == "over"

    assert by_account["C"]["variance_amount"] == 0
    assert by_account["C"]["flag"] == "ok"

    assert by_account["D"]["variance_amount"] == 5000
    assert by_account["D"]["flag"] == "over"
