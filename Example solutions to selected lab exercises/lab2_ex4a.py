def total_price(n_copies):
    """
    Calculates the total price in dollars of n_copies of a $24.95 book with a 40% discount.
    Includes the shipping cost of $3 for the first copy and $0.75 for each additional copy.
    Assume n_copies is a non-negative integer.
    If n_copies = 0, return 0.
    """
    assert type(n_copies) is int, "total_price: n_copies must be integer."
    assert n_copies >= 0, "total_price: n_copies must be non-negative."
    if n_copies == 0:
        return 0
    price    = 24.95
    discount = 0.40 #40%
    shipping_first = 3.0
    shipping_nexts = 0.75
    shipping = shipping_first + (n_copies-1) * shipping_nexts
    return (n_copies * price * (1-discount)) + shipping
