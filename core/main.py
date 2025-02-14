import click
import uvicorn
from config.engine import ConfigEngine
from api.app import start_app

@click.command()
@click.argument("startserver")
@click.option("-h", "--host", help="Указать хост инстанса John")
@click.option("-p", "--port", help="Указать порт инстанса John")
@click.option("-v", "--verbose", is_flag=True, help="Добавить логи отладки инстанса")
def start(startserver, host, port, verbose):
    config = ConfigEngine()
    server = config.get_value_by_params("server_instance")[0]
    if host == None:
        print('Хост введен не был! Используется хост конфигурации')
        host = server["host"]
    else:
        if host != server["host"]:
            print(f'Хост {host} отличается от порта конфигурации {server["host"]}! ')
    if port == None:
        print('Порт введен не был! Используется порт конфигурации')
        port = server["port"]
    else:
        if port != server["port"]:
            print(f'Порт {port} отличается от порта конфигурации {server["port"]}! ')
    if verbose == True:
        print("Включен отладочный режим!")
    start_app(host, port, verbose)
    return host, port, verbose

if __name__ == "__main__":
    host, port, verbose = start()
    print(host, port, verbose)



