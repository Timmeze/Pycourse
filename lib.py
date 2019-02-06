def fuel_consaption(fuel_resudie, consumption_100km):
    """
    >>> fuel_consaption(125, 10)
    1249

    """
    result = round(((fuel_resudie / consumption_100km * 100) - 1))
    return result


def wallpaper_calc(lengh, widgh, heigh, wall_paper):
    """
    >>> wallpaper_calc(5, 6, 2.5, 1.04)
    9

    """
    result = round((((lengh + widgh) * 2 // wall_paper + 1) / (10 // (heigh + 0.1))) + 2)
    return result
