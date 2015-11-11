__author__ = '30137120'


class Cell(object):
    def __init__(self, reference, row, column):
        self.reference = reference
        self.row = "Row" + row
        self.column = "Column" + column
        self.square = ""
        self.value = ""
        self.possiblevalues = []

    def setpossible(self, value):
        self.possiblevalues = list(value)

    def removepossible(self,value):
        if value in self.possiblevalues: self.possiblevalues.remove(value)
