import os.path
from typing import Callable, Optional
import functools
import asyncio
from log import Log
from logtype import LogType
import warnings
import logging
import traceback
class Logger:
    _log_file_ = os.path.abspath('../temp/log.txt')

    def __init__(self, log_warning: bool = False):
        if os.path.exists(self._log_file_):
            with open(self._log_file_, mode="a", encoding="utf-8") as file:
                file.write('')
            logging.basicConfig(level=logging.INFO, filename="_log_file_", filemode="w")
        if log_warning:
            warnings.showwarning = Logger.logging_warnings
    @classmethod
    def write_custom_log(cls, log):
        with open(cls._log_file_, mode="a", encoding="utf-8") as file:
            file.write(log.__str__())
    @classmethod
    def write_log(cls, log: Log):
        with open(cls._log_file_, mode="a", encoding="utf-8") as file:
            file.write(log.__str__())
    @classmethod
    def logging_full(cls, func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log = Log()
            log.set_type(LogType.INFO)
            log.set_func_name(func.__qualname__)
            log.set_func_args(*args[1:], **kwargs)
            cls.write_log(log)
            return func(*args, **kwargs)
        return wrapper

    @classmethod
    def logging_time(cls, func: Callable):
        pass

    @classmethod
    def logging_warnings(cls, message, category, filename, lineno, file=None, line=None):
        stack = traceback.extract_stack()
        log = Log()
        log.set_type(LogType.WARNING)

        log._head += 'Функция: ' + stack[-3][-2] + ' '
        log._body = category.__name__ + ' ' + str(filename)+ ' ' + str(lineno) + '\n'
        cls.write_log(log)


    @classmethod
    def logging_errors(cls, func: Callable):
        pass


    def __warning_with_traceback(self):
        pass
class fucker:
    @Logger.logging_full
    def __init__(self):
        self.lol(1, b=1)

    @Logger.logging_full
    def lol(self, a, b):
        print('oki')
        warnings.warn("ичто")
        return None


logger = logging.getLogger(__name__)
logger.info(f"Ошибка в функции")
logger.warning(f"Ошибка в функции")
logger.error(f"Ошибка в функции")
o = Logger(log_warning=True)
a = fucker()