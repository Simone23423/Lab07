from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM biblioteca"
        cursor.execute(query)
        for row in cursor:
            result.append(Biblioteca(row["id"], row["nome"], row["indirizzo"]))
        cursor.close()
        cnx.close()
        return result
