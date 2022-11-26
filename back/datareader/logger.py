from functools import wraps

from structlog import get_logger

logger = get_logger("dataloader")


def logging(function_name):
    def log_decorator(function_to_log):
        @wraps(function_to_log)
        def log_decorator_wrapper(*args, **kwargs):
            logger.info("Begin function {function_name}")
            try:
                value = function_to_log(*args, **kwargs)
                logger.info(
                    f"{function_name} returned", args=args, kwargs=kwargs, result=value
                )
            except Exception as e:
                logger.error(
                    f"Exception in {function_name}",
                    args=args,
                    kwargs=kwargs,
                    error=str(e),
                )
                raise
            return value

        return log_decorator_wrapper

    return log_decorator
