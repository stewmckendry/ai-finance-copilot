# Purpose: Validate fetch_budget_data returns expected records
# Test command: pytest tests/data/test_azure_sql.py
"""Tests for fetch_budget_data using SQLite."""

import os
from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.storage import models, db
from app.data.azure_sql import fetch_budget_data


def setup_sqlite():
    engine = create_engine("sqlite:///:memory:")
    models.Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    session.add_all([
        models.Budget(id=1, department="Finance", account="1001", amount_planned=1000, fiscal_year="2024"),
    ])
    session.add_all([
        models.Actual(id=1, department="Finance", account="1001", amount_actual=900, fiscal_period="2024-Q1"),
    ])
    session.add_all([
        models.Transaction(id=1, account="1001", date=date(2024, 1, 15), amount=450, description="Office supplies"),
    ])
    session.commit()
    session.close()
    return engine, SessionLocal


def test_fetch_budget_data(monkeypatch):
    engine, SessionLocal = setup_sqlite()

    def fake_get_engine(url=None):
        assert url == "resource://config/azure_sql"
        return engine

    monkeypatch.setattr(db, "get_engine", fake_get_engine)
    monkeypatch.setattr(db, "get_session", lambda eng=engine: SessionLocal())

    data = fetch_budget_data("2024-Q1")

    assert data["budgets"][0]["amount_planned"] == 1000
    assert data["actuals"][0]["amount_actual"] == 900
    assert data["transactions"][0]["description"] == "Office supplies"
