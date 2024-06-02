#!/usr/bin/env python3
"""
A module that contains a function that returns the log message obfuscated
"""
import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Args:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character is separating all
                    fields in the log line
    Returns:
        The log message obfuscated
    """
    for field in fields:
        field_regex = rf'{field}=.+?{separator}'
        replacement = f'{field}={redaction}{separator}'
        message = re.sub(field_regex, replacement, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Constructor method"""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ Formater method that returns the log message obfuscated"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
