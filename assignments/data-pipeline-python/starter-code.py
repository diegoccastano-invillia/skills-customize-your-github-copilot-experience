"""Starter code for the automated data pipeline assignment."""

import csv
import sqlite3
from decimal import Decimal
from pathlib import Path


def load_records(filename):
    """Load and normalize CSV rows."""
    pass


def validate_record(record):
    """Return a list of validation errors for one record."""
    pass


def transform_records(records):
    """Return valid records with a calculated total field."""
    pass


def setup_database(connection):
    """Create the sales table and any required constraints."""
    pass


def save_records(connection, records):
    """Insert records without creating duplicates."""
    pass


def generate_report(connection, filename):
    """Write summary metrics and category totals to a text file."""
    pass


def main():
    input_file = Path("data.csv")
    database_file = Path("sales.db")
    report_file = Path("report.txt")

    records = load_records(input_file)
    valid_records = transform_records(records)

    with sqlite3.connect(database_file) as connection:
        setup_database(connection)
        save_records(connection, valid_records)
        generate_report(connection, report_file)


if __name__ == "__main__":
    main()
