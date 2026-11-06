from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_generi(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result
        cursor = cnx.cursor()
        query = "SELECT DISTINCT genere FROM libro"
        cursor.execute(query)
        for (genere,) in cursor:
            if genere:
                result.append(genere)
        cursor.close()
        cnx.close()
        return result

    def get_libri_filtrati(self, biblioteca: str, genere: str):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result
        cursor = cnx.cursor(dictionary=True)

        query = """
            SELECT l.* 
            FROM libro l, biblioteca b 
            WHERE l.id_biblioteca = b.id 
              AND (%s IS NULL OR b.nome = %s) 
              AND (%s IS NULL OR l.genere = %s)
        """
        cursor.execute(query, (biblioteca, biblioteca, genere, genere))
        for row in cursor:
            result.append(Libro(
                row["id"],
                row["titolo"],
                row["autore"],
                row["genere"],
                row["anno_pubblicazione"],
                row["id_biblioteca"]
            ))
        cursor.close()
        cnx.close()
        return result
