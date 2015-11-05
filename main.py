from cell import Cell
from functions import *

__author__ = '30137120'

Cells = {}
Rows = {}
Columns = {}
Squares = {}
BigRows = {}  # rows [1,2,3] [4,5,6] and [7,8,9]
BigColumns = {}
Grid = {}

# Create Cell objects and populate Cells and Rows dictionaries
for row in xrange(1, 10):
    Row = []
    for col in xrange(1, 10):
        Cells["R" + str(row) + "C" + str(col)] = Cell("R" + str(row) + "C" + str(col))
        Row.append(Cells["R" + str(row) + "C" + str(col)])

    Rows["Row" + str(row)] = Row

# Populate Columns dictionary
for col in xrange(1, 10):
    Column = []
    for row in xrange(1, 10):
        Column.append(Cells["R" + str(row) + "C" + str(col)])
    Columns["Column" + str(col)] = Column

# Populate BigCells dictionary
squarecount = 1

for RowSet in ([1, 2, 3], [4, 5, 6], [7, 8, 9]):
    for ColSet in ([1, 2, 3], [4, 5, 6], [7, 8, 9]):
        square = []
        for row in RowSet:
            for col in ColSet:
                square.append(Cells["R" + str(row) + "C" + str(col)])
        Squares["Square" + str(squarecount)] = square
        squarecount += 1

# Populate BigRows dictionary
count = 1
for RowSet in ([1, 2, 3], [4, 5, 6], [7, 8, 9]):
    BigRow = []
    for row in RowSet:
        BigRow.append(Rows["Row" + str(row)])
    BigRows["BigRow" + str(count)] = BigRow
    count += 1

# Populate BigColumns dictionary
count = 1
for ColSet in ([1, 2, 3], [4, 5, 6], [7, 8, 9]):
    BigColumn = []
    for col in ColSet:
        BigColumn.append(Columns["Column" + str(col)])
    BigColumns["BigColumn" + str(count)] = BigColumn
    count += 1

Grid["Cells"] = Cells
Grid["Rows"] = Rows
Grid["Columns"] = Columns
Grid["Squares"] = Squares
Grid["BigRows"] = BigRows
Grid["BigColumns"] = BigColumns

# Import suduko.txt file to fill our Cells dictionary
importsuduko(Cells)

# Populate potential values
updatepossibles(Grid)

print "wait"