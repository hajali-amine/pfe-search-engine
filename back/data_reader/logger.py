from functools import wraps
from logging import Logger

def logging(function_name):
    def log_decorator(function_to_log):
        @wraps(function_to_log)
        def log_decorator_wrapper(*args, **kwargs):
            Logger.info(msg="Begin function")
            try:
                value = function_to_log(*args, **kwargs)
                Logger.info(msg=f"{function_name} returned", args=args, kwargs=kwargs, result=value)
            except Exception as e:
                Logger.error(msg=f"Exception in {function_name}", msg=str(e))
                raise
            return value
        return log_decorator_wrapper
    return log_decorator
