def sum_numbers(*args):
    """
    Calculate the sum of 2, 3, or 4 numbers.
    
    Args:
        *args: Variable length argument list containing numbers to sum.
              Must contain 2, 3, or 4 numbers.
    
    Returns:
        The sum of the input numbers.
        
    Raises:
        ValueError: If fewer than 2 or more than 4 arguments are provided.
    """
    if len(args) < 2 or len(args) > 4:
        raise ValueError("Function requires 2, 3, or 4 numbers")
    
    return sum(args)
