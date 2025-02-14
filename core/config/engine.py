import functools
import os
import warnings
import json
import ctypes
from typing import Optional, Any, Callable
from dotenv import load_dotenv
from functools import lru_cache
class ConfigEngine:
    _config_init_file_ = os.path.abspath("local/__init__.json")
    _config_path_ = os.path.abspath("local/")
    _config_env_file_ = os.path.abspath("local/.env")
    _config_file_name_ = '\config.json'
    _env_file_name_ = '\.env'

    def __init__(self, config_file = None):

        self.config_file = self._config_path_ + self._config_file_name_ if config_file == None else config_file
        if os.path.exists(self.config_file):
            print("Файл конфигурации найден!")
        else:
            raise Exception(f"Конфигурационный файл {self.config_file} отсутствует!")
        self.data = self._get_all_params_()

        self.fast_structure = self._get_all_keys_(self.data)

    def _get_all_params_(self) -> dict:
        with open(self.config_file) as file:
            data = json.load(file)
        return data
    def _get_all_keys_(self, data: dict, mother:Optional[str] = None) -> dict[str, id]:
        key_dict = {}
        for key, value in data.items():
            key_hash = key if mother == None else (mother + key)
            key_dict[key_hash] = id(value)
            if isinstance(value, dict):
                buf = mother
                mother = key + "_" if mother == None else mother + key + "_"
                key_dict.update(self._get_all_keys_(value, mother))
                mother = buf
        return key_dict

    def get_value_by_params(self, *args) -> Optional[Any]:
        user_params = args
        config_keys = self.fast_structure.keys()
        values = []
        for param in user_params:
            key_list = list(map(lambda key: key if param in key else None,config_keys))
            if not any(key_list):
                warnings.warn("Параметр не найден в конфигурационном файле!", UserWarning)
                continue

            key_list = [key for key in key_list if key != None]
            key_hash = key_list[0]
            values.append(ctypes.cast(self.fast_structure[key_hash], ctypes.py_object).value)
        return values

    @classmethod
    @lru_cache(maxsize=128)
    def use_env_params(cls, func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            load_dotenv(cls._config_env_file_)
            return func(*args, **kwargs)
        return wrapper


