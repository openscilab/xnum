# -*- coding: utf-8 -*-
"""Conflict-check script."""
from xnum.params import NUMERAL_MAPS


def detect_conflicts() -> bool:
    """
    Detect conflicts.

    :return: result as boolean
    """
    seen = {}
    for system, digits in NUMERAL_MAPS.items():
        for index, char in enumerate(digits):
            if char in seen:
                other_system, other_index = seen[char]
                print("  Conflict detected:")
                print("    Character: '{char}'".format(char=char))
                print("    System 1:  {other_system} -> {other_index}".format(other_system=other_system, other_index=other_index))
                print("    System 2:  {system} -> {index}".format(system=system, index=index))
                return False
            seen[char] = (system, index)
    print("No conflicts detected among numeral systems.")
    return True

if __name__ == "__main__":
    success = detect_conflicts()
    exit(0 if success else 1)
