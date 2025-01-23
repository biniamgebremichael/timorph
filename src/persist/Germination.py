import json
class Germination:

    def __init__(self,base,tensebase,pos,feature,subject,object,germinated,frequency):
        self.base = base
        self.basetense = tensebase
        self.pos = pos
        self.feature = feature
        self.subject = subject
        self.object = object
        self.germinated = germinated
        self.frequency = frequency


    @staticmethod
    def objectify(base, basetense,pos, feature, map):
        objectified = []
        for x, y in map.items():
            for a, b in y.items():
                if(len(list(y[a]) )>0):
                    objectified.append(Germination(base, basetense, pos,feature, x, a, y[a][0], y[a][1]))
        return objectified

    def to_json(obj):
        return json.dumps(obj.__dict__)

    def to_tuple(self):
        return (self.base, self.basetense, self.pos, self.feature, self.subject, self.object, self.germinated, self.frequency)