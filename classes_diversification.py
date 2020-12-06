def injecting(**kwargs):
    """
    Class diversification
    :param kwargs: Parameters for class diversification
    :return: Class after injection
    """

    def inner(cls):
        for k, v in kwargs.items():
            setattr(cls, k, v)
        return cls

    return inner
