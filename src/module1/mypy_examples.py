"""
This module contains some examples for mypy.
"""


def greeting(name: str) -> str:
    """
    Example for mypy
    """
    return 'Hello ' + name

greeting(3)         # Argument 1 to "greeting" has incompatible type "int"; expected "str"
greeting(b'Alice')  # Argument 1 to "greeting" has incompatible type "bytes"; expected "str"
