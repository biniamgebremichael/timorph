import json
class Germination:

    def __init__(self,parentroot,base,shortpath,longpath,pos,feature,subject,object,germinated,frequency):
        self.parent = parentroot
        self.base = base
        self.shortpath =  shortpath
        self.longpath =  longpath
        self.pos = pos
        self.feature = feature
        self.subject = subject
        self.object = object
        self.germinated = germinated
        self.frequency = frequency


    @staticmethod
    def objectify(parentroot,shortpath,longpath, base, pos, feature, map):
        objectified = []
        for x, y in map.items():
            for a, b in y.items():
                if(len(list(y[a]) )>0):
                    objectified.append(Germination(parentroot,base, shortpath,longpath, pos,feature, x, a, y[a][0], y[a][1]))
        return objectified

    @staticmethod
    def rootGermination(root,pos):
        return Germination(root,root,"","",pos,"ROOT","","",root,0)
    def to_json(obj):
        return json.dumps(obj.__dict__)

    def to_tuple(self):
        return (self.parent,self.base,self.shortpath,self.longpath, self.pos, self.feature, self.subject, self.object, self.germinated, self.frequency)