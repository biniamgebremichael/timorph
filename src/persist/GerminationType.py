class GerminationType:

    def __init__(self, rows,maps):
            self.id,self.name,self.tense,self.subtense = rows
            self.map = maps[self.name]