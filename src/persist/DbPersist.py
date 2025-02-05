import sqlite3, os
from persist.Germination import Germination
from functools import lru_cache

class DbPersistor:
    SRC_DIR = os.path.dirname(__file__)
    db_file = os.path.join(SRC_DIR, "../resources/timorph.db")

    def __init__(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS germination (ID INTEGER PRIMARY KEY AUTOINCREMENT, PARENT TEXT, BASE TEXT, SHORTPATH TEXT, LONGPATH TEXT, POS TEXT,FEATURE TEXT,SUBJECT TEXT,OBJECT TEXT, GERMINATED TEXT , FREQUENCY INTEGER ,  UPDATETIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

    @lru_cache(maxsize=200)
    def existGermination(self, base, pos,  feature):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cus = cursor.execute("select count(*) from germination where BASE=?  and POS=?   and FEATURE=? LIMIT 0,1",
                                 (base, pos, feature))
            fetchall = cus.fetchall()
            # print(fetchall)
        return fetchall[0][0]

    def getParents(self,pos,limit):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            query = f"SELECT DISTINCT PARENT,POS,COUNT(DISTINCT GERMINATED) K FROM  germination   WHERE POS=? AND FREQUENCY>0 GROUP BY PARENT,POS ORDER BY K DESC LIMIT {limit},50"
            cus = cursor.execute(query,[pos])
            fetchall = cus.fetchall()
        return [{"parent": row[0], "pos": row[1], "count": row[2]} for row in fetchall]

    def getGermination(self, pos,parent):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cus = cursor.execute(
                "SELECT PARENT, BASE , SHORTPATH,LONGPATH, POS, FEATURE, SUBJECT, OBJECT, GERMINATED, FREQUENCY FROM  germination WHERE  FREQUENCY>=0 and PARENT=? and POS=?",
                [parent,pos])
            fetchall = cus.fetchall()
        return [Germination(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]) for row in fetchall]

    def getGerminations(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cus = cursor.execute(
                "SELECT PARENT, BASE , SHORTPATH,LONGPATH, POS, FEATURE, SUBJECT, OBJECT, GERMINATED, FREQUENCY FROM  germination  ")
            fetchall = cus.fetchall()
        return [Germination(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]) for row in fetchall]

    def addGermination(self, germinations):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.executemany(
                'INSERT INTO germination ( PARENT, BASE , SHORTPATH,LONGPATH,POS, FEATURE, SUBJECT, OBJECT, GERMINATED, FREQUENCY) VALUES (?, ?,?,?, ?, ?, ?, ?, ?, ? )',
                germinations)
        return cursor.lastrowid


if __name__ == "__main__":
    print("\n".join([x.germinated for x in DbPersistor().getGermination("ሃረመ")]))
    # print(DbPersistor().existGermination('ነገርክንአን',"V","PRESENT","VERBPREFIX"))
    # print("\n".join([x.to_json() for x in DbPersistor().getGerminations()]))
