import time

def calc_time(birthday: str) -> float:
    """
    Calculate the time between birthday and now

    Args:
        birthday: str
    Returns:
        str, the corresponding time
    """
    convert = time.strptime(birthday, "%Y-%m-%d")

    t = time.time() - time.mktime(convert)
    return t/31536000
