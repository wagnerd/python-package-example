"""
Some tests for package mechanisms

For the metadata import(s) we have to disable mypy checks, because else it will fail here.

"""
try:
    from importlib import metadata # type: ignore
except ImportError:
    # Running on pre-3.8 Python; use importlib-metadata package
    import importlib_metadata as metadata # type: ignore


def test_get_package_version() -> None:
    """
    Simple test to show how to get the package version inside code.
    https://packaging.python.org/guides/single-sourcing-package-version/
    """
    assert metadata.version('python-package-example') == '0.1.0' # type: ignore
