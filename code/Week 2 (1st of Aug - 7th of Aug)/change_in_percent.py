
def change_in_percent(old, new):
    """
    Calculates change from old to new value, as a
    percentage of the old.
    Assumes that old and new are both numbers and
    that old is not 0.
    """
    diff = new - old
    return (diff / old) * 100

enrolled_2020 = 489
enrolled_2021 = 556

print("The increase is", change_in_percent(enrolled_2020, enrolled_2021), "%")
