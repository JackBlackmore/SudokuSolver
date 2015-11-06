__author__ = '30137120'
# Git Test

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
    for Column in Grid["Columns"].itervalues():
        impossiblevalues = []

        # Create list of impossible values by column
        for cell in Column:
            if cell.value != "": impossiblevalues.append(cell.value)

        # Remove impossible values from possible values
        for cell in Column:
            if cell.value == "":
                for v in impossiblevalues:
                    if v in cell.possiblevalues: cell.removepossible(v)

def removesquareimpossibles(Grid):
    for Square in Grid["Squares"].itervalues():
        impossiblevalues = []

        # Create list of impossible values by square
        for cell in Square:
            if cell.value != "": impossiblevalues.append(cell.value)

        # Remove impossible values from possible values
        for cell in Square:
            if cell.value == "":
                for v in impossiblevalues:
                    if v in cell.possiblevalues: cell.removepossible(v)

def solvedefinites(Grid):
    rerun = False
    if solverowdefinites(Grid) == True: rerun = True
    if solvecolumndefinites(Grid) == True: rerun = True
    if solvesquaredefinites(Grid) == True: rerun = True

    if rerun == True:
        updatepossibles(Grid)
        solvedefinites(Grid)

def solverowdefinites(Grid):
    rerun = False
    for Row in Grid["Rows"].itervalues():
        # Initialise valuecounty dictionary
        valuecount = {}
        for v in xrange(1,10): valuecount[str(v)] = 0

        # Populate valuecount
        for cell in Row:
            if cell.value == "":
                for v in cell.possiblevalues: valuecount[str(v)] += 1

        #
        for cell in Row:
            if cell.value == "":
                for v in cell.possiblevalues:
                    if valuecount[str(v)] == 1:
                        cell.value = str(v)
                        cell.possiblevalues = []
                        rerun = True
    return rerun

def solvecolumndefinites(Grid):
    rerun = False
    for Column in Grid["Columns"].itervalues():
        # Initialise valuecounty dictionary
        valuecount = {}
        for v in xrange(1,10): valuecount[str(v)] = 0

        # Populate valuecount
        for cell in Column:
            if cell.value == "":
                for v in cell.possiblevalues: valuecount[str(v)] += 1

        #
        for cell in Column:
            if cell.value == "":
                for v in cell.possiblevalues:
                    if valuecount[str(v)] == 1:
                        cell.value = str(v)
                        cell.possiblevalues = []
                        rerun = True
    return rerun

def solvesquaredefinites(Grid):
    rerun = False
    for Square in Grid["Squares"].itervalues():
        # Initialise valuecount dictionary
        valuecount = {}
        for v in xrange(1,10): valuecount[str(v)] = 0

        # Populate valuecount
        for cell in Square:
            if cell.value == "":
                for v in cell.possiblevalues: valuecount[str(v)] += 1

        #
        for cell in Square:
            if cell.value == "":
                for v in cell.possiblevalues:
                    if valuecount[str(v)] == 1:
                        cell.value = str(v)
                        cell.possiblevalues = []
                        rerun = True
    return rerun

def exportsuduko(Cells):
    f = open("suduko_output.txt","w")

    for row in range(1,10):
        rowstring = ""
        for col in range(1,10):
            rowstring += str(Cells["R" + str(row) + "C" + str(col)].value) + "|"

        rowstring = rowstring[:-1] + "\n"

        f.write(rowstring)