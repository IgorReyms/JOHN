from logtype import LogType
from typing import Any
class Log:
    def __init__(self, standart: bool = False):
        self._head = None
        self._body = None
        self._tail = None
        self.tabulator = '   '
    def set_type(self, logt: str):
        self._head = logt + ":" + self.tabulator

    def set_func_name(self, func: str):
        self._body = '' if self._body == None else self._body
        print(func)
        if func.split('.')[1] != "__init__":
            self._body += 'Функция: ' + func + self.tabulator
        else:
            self._body += f'Модуль {func.split('.')[0]} инициализрован!' + self.tabulator
    def set_func_args(self, *args, **kwargs):
        self._body = '' if self._body == None else self._body
        self._body += 'args: ' + str(args) + self.tabulator + 'kwargs:' + str(kwargs) + self.tabulator

    def set_tail(self, tail: str):
        self._tail = '' if self._tail == None else self._tail
        self._tail += tail

    def __str__(self):
        if self._head == None or self._body == None:
            raise Exception
        else:
            return self._head + self._body + (self._tail if self._tail != None else '') + '\n'

