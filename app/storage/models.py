"""ORM models for budget data.

Purpose: Define SQLAlchemy models for budgets, actuals and transactions tables.
Deployment: Import by tools needing database access.
Test: pytest tests/data/test_azure_sql.py
"""

from sqlalchemy import Column, Integer, String, Numeric, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Budget(Base):
    __tablename__ = 'budgets'
    id = Column(Integer, primary_key=True)
    department = Column(String, nullable=False)
    account = Column(String, nullable=False)
    amount_planned = Column(Numeric, nullable=False)
    fiscal_year = Column(String, nullable=False)

class Actual(Base):
    __tablename__ = 'actuals'
    id = Column(Integer, primary_key=True)
    department = Column(String, nullable=False)
    account = Column(String, nullable=False)
    amount_actual = Column(Numeric, nullable=False)
    fiscal_period = Column(String, nullable=False)

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    account = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    amount = Column(Numeric, nullable=False)
    description = Column(String, nullable=False)
