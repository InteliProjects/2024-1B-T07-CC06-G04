"""
CSV Service for Processing CSV Files

This module provides a service for processing CSV files and returning their content as a list of dictionaries.

Modules:
    - List, Dict: Typing modules for type hinting.
    - csv: Standard Python library for CSV file operations.

Classes:
    - CSVService:
        Provides static methods for processing CSV files.

Functions:
    - process_csv(file_path: str) -> List[Dict[str, str]]:
        Processes a CSV file and returns its content as a list of dictionaries.
"""

from typing import List, Dict
import csv

class CSVService:
    @staticmethod
    async def process_csv(file_path: str) -> List[Dict[str, str]]:
        """
        Processes a CSV file and returns its content as a list of dictionaries.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            List[Dict[str, str]]: A list of dictionaries where each dictionary represents a row in the CSV file.
        """
        with open(file_path, "r", encoding="utf-8") as f:
            csv_reader = csv.DictReader(f, delimiter=';')
            return [row for row in csv_reader]