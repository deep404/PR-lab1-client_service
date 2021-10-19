import logging
import coloredlogs
from flask import Flask
import threading
import time
from actors.Client import Client

CLIENTS_NR = 3

APP_HOST = '0.0.0.0'
CS_PORT = 8000

app = Flask('Client-Service')

logging.basicConfig(filename='client_service.log', level=logging.DEBUG, format='%(asctime)s: %(threadName)s: %(message)s', datefmt="%m/%d/%Y %I:%M:%S %p")
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')


def clients():
    for i in range(CLIENTS_NR):
        client = Client(i)
        threading.Thread(target=client.generate_order, daemon=True, name=f'Client-{i}').start()
        time.sleep(2)


def main():
    open("client_service.log", "w").close()

    threading.Thread(target=lambda: app.run(host=APP_HOST, port=CS_PORT, debug=False, use_reloader=False, threaded=True), name=f'FLASK-MAIN', daemon=True).start()
    clients()

    while True:
        pass


if __name__ == '__main__':
    main()