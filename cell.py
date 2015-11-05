__author__ = '30137120'


class Cell(object):
    def __init__(self, reference):
        self.reference = reference
        self.value = ""
        self.possiblevalues = []

    def setpossible(self, value):
        self.possiblevalues = list(value)

    def removepossible(self,value):
        if value in self.possiblevalues: self.possiblevalues.remove(value)
