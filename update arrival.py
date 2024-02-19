def update_arrival(h, m, d):
    """
    >>> update_arrival(10, 45, 20)
    (11, 5)
    >>> update_arrival(12, 30, 60)
    (13, 30)
    >>> update_arrival(22, 0, 120)
    (0, 0)
    >>> update_arrival(23, 57, 5 + 24*60)
    (0, 2)
    """
    return ((h * 60 + m + d) // 60) % 24, (h * 60 + m + d) % 60