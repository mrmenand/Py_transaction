from functools import wraps


def single_ton(cls):
    _instance = {}

    @wraps(cls)
    def single(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return single


@single_ton
class SingleTon:

    def __init__(self, val):
        self.val = val

    # class SingleTon:
#     _instance = {}
#
#     def __new__(cls, *args, **kwargs):
#         if cls not in cls._instance:
#             cls._instance[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
#
#         return cls._instance[cls]
