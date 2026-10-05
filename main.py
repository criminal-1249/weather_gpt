def add(a, b):
    """
    Return the sum of a and b.

    Parameters
    ----------
    a : numeric
    b : numeric

    Returns
    -------
    numeric
        The result of a + b.
    """
    return a + b


def divide(a, b):
    """
    Return the result of dividing a by b.

    Parameters
    ----------
    a : numeric
    b : numeric

    Returns
    -------
    numeric
        The result of a / b.

    Raises
    ------
    ValueError
        If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
