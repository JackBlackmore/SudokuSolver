__author__ = '30137120'


def importsudoku(filename, Cells):
    f = open(filename,'r')
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
    print "solve"
    updated = False
    if solverowdefinites(Grid) == True: updated = True
    if solvecolumndefinites(Grid) == True: updated = True
    if solvesquaredefinites(Grid) == True: updated = True
    if solvecelldefinites(Grid) == True: updated = True
    if updated == True: solvedefinites(Grid)


def solverowdefinites(Grid):
    updated = False
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
                        updated = True
    if updated == True:
        updatepossibles(Grid)
    return updated

def solvecolumndefinites(Grid):
    updated = False
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
                        updated = True
    if updated == True:
        updatepossibles(Grid)
    return updated

def solvesquaredefinites(Grid):
    updated = False
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
                        updated = True
    if updated == True:
        updatepossibles(Grid)
    return updated

def solvecelldefinites(Grid):
    updated = False
    for cell in Grid['Cells'].itervalues():
        if cell.value == "" and len(cell.possiblevalues) == 1:
            cell.value = cell.possiblevalues[0]
            cell.possiblevalues = []
            updated = True

    if updated == True:
        updatepossibles(Grid)
    return updated


def checkresults(Grid):
    solved = True
    failedstring = ""
    for Row in Grid['Rows'].iteritems():
        requiredvalues = list(str(v) for v in xrange(1,10))
        for cell in Row[1]:
            if cell.value in requiredvalues: requiredvalues.remove(cell.value)

        if len(requiredvalues) != 0:
            solved = False
            failedstring += str(Row[0]) + " failed\n"

    for Column in Grid['Columns'].iteritems():
        requiredvalues = list(str(v) for v in xrange(1,10))
        for cell in Column[1]:
            if cell.value in requiredvalues: requiredvalues.remove(cell.value)

        if len(requiredvalues) != 0:
            solved = False
            failedstring += str(Column[0]) + " failed\n"

    for Square in Grid['Squares'].iteritems():
        requiredvalues = list(str(v) for v in xrange(1,10))
        for cell in Square[1]:
            if cell.value in requiredvalues: requiredvalues.remove(cell.value)

        if len(requiredvalues) != 0:
            solved = False
            failedstring += str(Square[0]) + " failed\n"

    if solved == False:
        Grid["SolvedStatus"] = failedstring
    else:
        Grid["SolvedStatus"] = "Success"


def exportsudoku(Grid):
    f = open("sudoku_output.txt","w")

    for row in range(1,10):
        rowstring = ""
        for col in range(1,10):
#            rowstring += str(Cells["R" + str(row) + "C" + str(col)].value) + "|"
           if str(Grid["Cells"]["R" + str(row) + "C" + str(col)].value) != "":
               rowstring += str(Grid['Cells']["R" + str(row) + "C" + str(col)].value) + "|"
           else:
               possiblestring = "("
               for v in Grid["Cells"]["R" + str(row) + "C" + str(col)].possiblevalues:
                   possiblestring += str(v) + "/"
               possiblestring = possiblestring[:-1] + ")"
               rowstring += possiblestring + "|"

        rowstring = rowstring[:-1] + "\n"
        f.write(rowstring)

    f.write("Status: " + Grid["SolvedStatus"])