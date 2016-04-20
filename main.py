from cell import Cell
from functions import *


__author__ = '30137120'

Cells = {}
Rows = {}
Columns = {}
Squares = {}
Grid = {}

# Create Cell objects and populate Cells and Rows dictionaries
for row in xrange(1, 10):
    Row = []
    for col in xrange(1, 10):
        Cells["R" + str(row) + "C" + str(col)] = Cell("R" + str(row) + "C" + str(col), str(row), str(col))
        Row.append(Cells["R" + str(row) + "C" + str(col)])

    Rows["Row" + str(row)] = Row

# Populate Columns dictionary
for col in xrange(1, 10):
    Column = []
    for row in xrange(1, 10):
        Column.append(Cells["R" + str(row) + "C" + str(col)])
    Columns["Column" + str(col)] = Column

# Populate Squares dictionary
squarecount = 1

for RowSet in ([1, 2, 3], [4, 5, 6], [7, 8, 9]):
    for ColSet in ([1, 2, 3], [4, 5, 6], [7, 8, 9]):
        square = []
        for row in RowSet:
            for col in ColSet:
                square.append(Cells["R" + str(row) + "C" + str(col)])
                Cells["R" + str(row) + "C" + str(col)].square = "Square" + str(squarecount)
        Squares["Square" + str(squarecount)] = square
        squarecount += 1

Grid["Cells"] = Cells
Grid["Rows"] = Rows
Grid["Columns"] = Columns
Grid["Squares"] = Squares


# Import sudoku.txt file to fill our Cells dictionary
importsudoku("sudoku_extreme.txt",Cells)

# Populate potential values
updatepossibles(Grid)

# Solve definites
solvedefinites(Grid)

# Check Results
checkresults(Grid)

if Grid['SolvedStatus'] == "Success":
    exportsudoku(Grid)
else:
    # Simulation Time
    simulatesolution(Grid, 1, "")


