from .database import ConexaoDB


class CategoriaService:
    def __init__(self):
        self.conexao_bd = ConexaoDB()

    def listar(self):
        conexao = self.conexao_bd.obter_conexao()
        try:
            return conexao.cursor().execute(
                "SELECT id, descricao FROM Categoria ORDER BY descricao"
            ).fetchall()
        finally:
            conexao.close()

    def buscar_por_id(self, id):
        conexao = self.conexao_bd.obter_conexao()
        try:
            return conexao.cursor().execute(
                "SELECT id, descricao FROM Categoria WHERE id = ?",
                (int(id),)
            ).fetchone()
        finally:
            conexao.close()

    def incluir(self, descricao):
        conexao = self.conexao_bd.obter_conexao()
        try:
            conexao.cursor().execute(
                "INSERT INTO Categoria (descricao) VALUES (?)",
                (descricao,)
            )
            conexao.commit()
        finally:
            conexao.close()

    def alterar(self, id, descricao):
        conexao = self.conexao_bd.obter_conexao()
        try:
            conexao.cursor().execute(
                "UPDATE Categoria SET descricao = ? WHERE id = ?",
                (descricao, int(id))
            )
            conexao.commit()
        finally:
            conexao.close()

    def excluir(self, id):
        conexao = self.conexao_bd.obter_conexao()
        try:
            conexao.cursor().execute(
                "DELETE FROM Categoria WHERE id = ?",
                (int(id),)
            )
            conexao.commit()
        finally:
            conexao.close()


class ProdutoService:
    def __init__(self):
        self.conexao_bd = ConexaoDB()

    # métodos CRUD
