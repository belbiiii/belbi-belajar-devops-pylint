"""Module for adding two numbers cleanly."""


def add_numbers(num_a, num_b):
    """Calculate and return the sum of two numbers.

    Args:
        num_a (int or float): The first number.
        num_b (int or float): The second number.

    Returns:
        int or float: Sum of num_a and num_b.
    """
    result = num_a + num_b
    print(result)
    return result


if __name__ == "__main__":
    add_numbers(1, 2)