import sqlite3


class ConexaoDB:
    def __init__(self, caminho_sql='db_solid.sqlite3'):
        self.caminho_sql = caminho_sql

    def obter_conexao(self):
        conexao = sqlite3.connect(self.caminho_sql)
        conexao.execute("PRAGMA foreign_keys = ON;")
        return conexao