import sqlite3, os
from persist.Germination import Germination


class DbPersistor:
    SRC_DIR = os.path.dirname(__file__)
    db_file = os.path.join(SRC_DIR, "../resources/timorph.db")

    def __init__(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS germination (ID INTEGER PRIMARY KEY AUTOINCREMENT, PARENT TEXT, BASE TEXT, TENSE TEXT, POS TEXT,FEATURE TEXT,SUBJECT TEXT,OBJECT TEXT, GERMINATED TEXT , FREQUENCY INTEGER )")

    def existGermination(self, base, pos, tense, feuture):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cus = cursor.execute("select * from germination where BASE=?  and POS=? and  TENSE=? and FEATURE=?",
                                 (base, pos, tense, feuture))
            fetchall = cus.fetchall()
            # print(fetchall)
        return len(fetchall)

    def getParents(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cus = cursor.execute(
                "SELECT DISTINCT PARENT,POS,COUNT(*) K FROM  germination GROUP BY PARENT,POS ORDER BY K DESC")
            fetchall = cus.fetchall()
        return [{"parent": row[0], "pos": row[1], "count": row[3]} for row in fetchall]

    def getGermination(self, parent):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cus = cursor.execute(
                "SELECT PARENT, BASE , TENSE, POS, FEATURE, SUBJECT, OBJECT, GERMINATED, FREQUENCY FROM  germination WHERE PARENT=?",
                [parent])
            fetchall = cus.fetchall()
        return [Germination(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[7]) for row in fetchall]

    def getGerminations(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cus = cursor.execute(
                "SELECT PARENT, BASE , TENSE, POS, FEATURE, SUBJECT, OBJECT, GERMINATED, FREQUENCY FROM  germination  ")
            fetchall = cus.fetchall()
        return [Germination(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[7]) for row in fetchall]

    def addGermination(self, germinations):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.executemany(
                'INSERT INTO germination ( PARENT, BASE , TENSE,POS, FEATURE, SUBJECT, OBJECT, GERMINATED, FREQUENCY) VALUES (?, ?,?, ?, ?, ?, ?, ?, ? )',
                germinations)
        return cursor.lastrowid


if __name__ == "__main__":
    print("\n".join([x.germinated for x in DbPersistor().getGermination("ሃረመ")]))
    # print(DbPersistor().existGermination('ነገርክንአን',"V","PRESENT","VERBPREFIX"))
    # print("\n".join([x.to_json() for x in DbPersistor().getGerminations()]))
