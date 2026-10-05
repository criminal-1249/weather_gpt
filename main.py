def add(a, b):
    """Return the sum of a and b.

    Parameters
    ----------
    a : int or float
        First operand.
    b : int or float
        Second operand.

    Returns
    -------
    int or float
        The sum of a and b.
    """
    return a + b


def divide(a, b):
    """Return the result of dividing a by b.

    Parameters
    ----------
    a : int or float
        Numerator.
    b : int or float
        Denominator.

    Returns
    -------
    int or float
        The quotient of a divided by b.

    Raises
    ------
    ZeroDivisionError
        If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


