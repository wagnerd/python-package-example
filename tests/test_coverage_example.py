"""
Unittests for coverage_example
"""

from module1.coverage_example import method_one

def test_method_one() -> None:
    """
    Cover method_one
    """
    assert method_one(1,2) == 3
