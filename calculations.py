def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Computes and prints statistical measures
    (mean, median, quartile, std, var)
    for the given data based on keyword arguments
    specifying the desired operations.
    """
    op = {
        'mean': ft_mean,
        'median': ft_median,
        'quartile': ft_quartile,
        'std': ft_std,
        'var': ft_var,
    }

    try:
        for _, value in kwargs.items():
            if value in op.keys():
                if len(args) > 0:
                    print(value, ':', op[value](args))
                else:
                    print('ERROR')

    except BaseException as e:
        print(type(e).__name__, ':', e)


def ft_mean(args):
    """
    Calculates and returns the mean (average) of the given data.
    """
    return sum(args) / len(args)


def ft_median(args):
    """
    Calculates and returns the median of the given data.
    """
    sorted_args = sorted(args)
    n = len(sorted_args)

    if n % 2 == 1:
        median = sorted_args[n // 2]
    else:
        mid1 = sorted_args[n // 2 - 1]
        mid2 = sorted_args[n // 2]
        median = (mid1 + mid2) / 2
    return median


def ft_quartile(args):
    """
    Calculates and returns the first and third quartiles of the given data.
    """
    list_n = list(args)
    list_n.sort()
    median = ft_median(list_n)

    one = ft_median(filter(lambda x: x <= median, list_n))
    two = ft_median(filter(lambda x: x >= median, list_n))

    return [one, two]


def ft_std(args):
    """
    Calculates and returns the standard deviation of the given data.
    """
    var = ft_var(args)
    return var ** 0.5


def ft_var(args):
    """
    Calculates and returns the variance of the given data.
    """
    mean = ft_mean(args)
    return sum((x - mean) ** 2 for x in args) / len(args)
