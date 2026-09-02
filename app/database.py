import sqlite3


class ConexaoDB:
    def __init__(self, caminho_banco='db_solid.sqlite3'):
        self.caminho_banco = caminho_banco

    def obter_conexao(self):
        conexao = sqlite3.connect(self.caminho_banco)
        conexao.execute("PRAGMA foreign_keys = ON;")
        return conexao