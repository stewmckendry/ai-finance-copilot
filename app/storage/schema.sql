-- SQL schema for budget data tables
-- Deployment: executed on test SQLite database
-- Test: pytest tests/data/test_azure_sql.py

CREATE TABLE budgets (
    id INTEGER PRIMARY KEY,
    department TEXT NOT NULL,
    account TEXT NOT NULL,
    amount_planned NUMERIC NOT NULL,
    fiscal_year TEXT NOT NULL
);

CREATE TABLE actuals (
    id INTEGER PRIMARY KEY,
    department TEXT NOT NULL,
    account TEXT NOT NULL,
    amount_actual NUMERIC NOT NULL,
    fiscal_period TEXT NOT NULL
);

CREATE TABLE transactions (
    id INTEGER PRIMARY KEY,
    account TEXT NOT NULL,
    date DATE NOT NULL,
    amount NUMERIC NOT NULL,
    description TEXT NOT NULL
);
