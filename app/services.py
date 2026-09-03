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
        self.categoria_service = CategoriaService()

    def listar(self):
        conexao = self.conexao_bd.obter_conexao()
        try:
            return conexao.cursor().execute(
                """
                SELECT pro.id,
                       pro.descricao,
                       pro.preco_unitario,
                       pro.quantidade_estoque,
                       pro.categoria_id,
                       cat.descricao
                FROM Produto pro
                INNER JOIN Categoria cat ON cat.id = pro.categoria_id
                ORDER BY pro.descricao
                """
            ).fetchall()
        finally:
            conexao.close()

    #def listar_categorias(self):
    #    return self.categoria_service.listar()

    def buscar_por_id(self, id):
        conexao = self.conexao_bd.obter_conexao()
        try:
            return conexao.cursor().execute(
                """
                SELECT pro.id,
                       pro.descricao,
                       pro.preco_unitario,
                       pro.quantidade_estoque,
                       pro.categoria_id,
                       cat.descricao
                FROM Produto pro
                INNER JOIN Categoria cat ON cat.id = pro.categoria_id
                WHERE pro.id = ?
                """,
                (int(id),)
            ).fetchone()
        finally:
            conexao.close()

    def incluir(self, categoria_id, descricao, preco_unitario, quantidade_estoque):
        conexao = self.conexao_bd.obter_conexao()
        try:
            conexao.cursor().execute(
                """
                INSERT INTO Produto (
                    descricao,
                    preco_unitario,
                    quantidade_estoque,
                    categoria_id
                ) VALUES (?, ?, ?, ?)
                """,
                (descricao, preco_unitario, quantidade_estoque, int(categoria_id))
            )
            conexao.commit()
        finally:
            conexao.close()

    def alterar(self, id, descricao, preco_unitario, quantidade_estoque, categoria_id):
        conexao = self.conexao_bd.obter_conexao()
        try:
            conexao.cursor().execute(
                """
                UPDATE Produto
                SET descricao = ?,
                    preco_unitario = ?,
                    quantidade_estoque = ?,
                    categoria_id = ?
                WHERE id = ?
                """,
                (
                    descricao,
                    preco_unitario,
                    quantidade_estoque,
                    int(categoria_id),
                    int(id)
                )
            )
            conexao.commit()
        finally:
            conexao.close()

    def excluir(self, id):
        conexao = self.conexao_bd.obter_conexao()
        try:
            conexao.cursor().execute(
                "DELETE FROM Produto WHERE id = ?",
                (int(id),)
            )
            conexao.commit()
        finally:
            conexao.close()
