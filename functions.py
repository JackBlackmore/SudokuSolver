__author__ = '30137120'


def importsuduko(Cells):
    f = open('suduko.txt','r')
    for row in xrange(1,10):
        line = f.readline().split('|')
        for col in xrange(1,10):
            if line[col-1] != '':
                Cells["R" + str(row) + "C" + str(col)].value = str(line[col-1]).replace("\n","")
                Cells["R" + str(row) + "C" + str(col)].solved = True

def updatepossibles(Grid):
    updaterowpossibles(Grid)
    removecolumnimpossibles(Grid)
    removesquareimpossibles(Grid)
    print "wait"

def updaterowpossibles(Grid):
    for Row in Grid["Rows"].itervalues():
        possiblevalues = list(str(e) for e in range(1,10))

        # Remove impossible row values
        for cell in Row:
            if cell.value in possiblevalues: possiblevalues.remove(cell.value)

        # Assign possible values to cells
        for cell in Row:
            if cell.value == "": cell.setpossible(possiblevalues)

def removecolumnimpossibles(Grid):
    for Column in Grid["Columns"].iteritems():
        impossiblevalues = []

        # Create list of impossible values by column
        for cell in Column[1]:
            if cell.value != "": impossiblevalues.append(cell.value)

        # Remove impossible values from possible values
        for cell in Column[1]:
            if cell.value == "":
                for v in impossiblevalues:
                    if v in cell.possiblevalues: cell.removepossible(v)

def removesquareimpossibles(Grid):
    print "wait"