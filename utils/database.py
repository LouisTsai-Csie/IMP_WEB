import sqlite3
import datetime
import cherrypy
import threading
import time
import json

class RESTService(object):
    def __init__(self, service):
        self._service = service

    @cherrypy.expose
    def index(self):
        return "database plugin."

    @cherrypy.expose
    def fetch_all(self):
        return self._service._fetch_all()

    @cherrypy.expose
    def peek_all(self):
        return self._service.peek_all()

class DatabaseService:
    def __init__(self):
        self._data_queue = []
        server_thread   = threading.Thread(target=self._server_job)
        database_thread = threading.Thread(target=self._database_job)

        server_thread.start()
        database_thread.start()

    def _server_job(self):
        cherrypy.config.update({'server.socket_port':8081})
        cherrypy.quickstart(RESTService(self))

    def _database_job(self):
        while True:
            self._process_data_queue()
            time.sleep(1)
    def _process_data_queue(self):
        while len(self._data_queue) > 0:
            with sqlite3.connect("DB0.db") as con:
                self._write(con, self._data_queue.pop(0))

    def _write(self, data, database_id):
        db = f'DB{database_id}.db'
        with sqlite3.connect(db) as con:
            cur = con.cursor()
            count = cur.execute('INSERT OR IGNORE INTO data(id, GOT, GPT) VALUES (?, ?, ?) ON CONFLICT(id) DO UPDATE SET GOT = (?), GPT = (?)', (data["id"], data["GOT"], data["GPT"], data["GOT"], data["GPT"])) 
            con.commit()

    def _fetch_all(self, preserve_data = False):
        with sqlite3.connect("DB5.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM data")

            rows = cur.fetchall()

            if not preserve_data:
                cur.execute("""DELETE FROM data""")

            return json.dumps(row)
        return ""

    def _peek_all(self):
        return self._fetch_all(True)

    def add_sample(self, data):
        self._data_queue.append((data, datetime.datetime.now))      