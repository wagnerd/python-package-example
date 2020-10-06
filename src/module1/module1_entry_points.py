"""
module1.module1_entry_points.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains the entry-point functions for the module1 module.
The entry-points can be referenced inside the setup.cfg and will be created during
package installation.
"""

from sys import argv


def main() -> None:
    """Main package entry point.

    Delegates to other functions based on user input.
    """

    try:
        user_cmd = argv[1]
        if user_cmd == 'entry1':
            entry_one()
        else:
            RuntimeError('please supply a command for py_pkg - e.g. install.')
    except IndexError:
        RuntimeError('please supply a command for py_pkg - e.g. install.')


def entry_one() -> None:
    """
    Simple example for entry-point method
    """
    print("This is entry-point entry_one")
   # return # Remove comment for Pylint error example
