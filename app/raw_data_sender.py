import logging
from datetime import datetime
from typing import List, Tuple 

import mysql.connector

from mysql_queries import QUERY_INSERT_RAW_DATA 


class RawDataSender:
    def __init__(self, user: str, password: str, host: str, database: str, port: str):
        logging.info(f'raw_data_sender.py: Initializing a MySQL connection to host: {host}, to database: {database}, using credentials: {user}/{password}.')
        self._cnx = mysql.connector.connect(user=user, password=password, host=host, database=database, port=port)
        self._cursor = self._cnx.cursor()
        self._queued_data: List[Tuple[int, int, str]]  = []
        self.user = user

    def __del__(self):
        logging.info('raw_data_sender.py: Closing MySQL connection.')
        self._cursor.close()
        self._cnx.close()

    def queue(self, can_id: int, data: bytearray):
        timestamp: str = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        value: int = int.from_bytes(data, byteorder='big', signed=False)
        logging.info(f'raw_data_sender.py: Queing raw CAN data to be sent: id:{can_id}, value:{value}, timestamp:{timestamp}\n') 
        self._queued_data.append((can_id, value, timestamp, self.user))

    def send(self):
        if not self._queued_data:
            logging.info('raw_data_sender.py: No queued data found. Skipping sending.')
            return

        logging.info('raw_data_sender.py: Sending all queued raw CAN data.')
        self._cursor.executemany(QUERY_INSERT_RAW_DATA, self._queued_data)

        self._cnx.commit()
        self._queued_data.clear()

