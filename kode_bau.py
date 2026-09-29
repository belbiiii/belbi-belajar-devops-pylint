"""Module for demonstrating code refactoring and Pylint compliance."""

X_VALUE = 10


def calculate_sum(val_a, val_b, val_c=None, val_d=1, list_e=None, val_f=3):
    """Calculate sum of parameters if valid.

    Args:
        val_a (bool): Primary flag condition.
        val_b (bool): Secondary flag condition.
        val_c (optional): Null check condition.
        val_d (int): Integer modifier.
        list_e (list): List containing base values.
        val_f (int): Additional integer value.

    Returns:
        int or None: Calculated sum if conditions are met, else None.
    """
    if list_e is None:
        list_e = [2]

    if val_a and not val_b and val_c is None:
        res = list_e[0] + val_f + val_d + X_VALUE
        return res

    return None


if __name__ == "__main__":
    calculate_sum(True, False, None, 1, [2], 3)