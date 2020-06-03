def do_decorate(func):
    def func_wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return func_wrapper