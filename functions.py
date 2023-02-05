# functions.py

def readableFormat(nonReadableLocation, aisleList, rows):

    # 0, 0, 0, 0 -> KA 01 A01
    aisle = nonReadableLocation[0]
    side  = nonReadableLocation[1]
    row   = nonReadableLocation[2]
    loc   = nonReadableLocation[3]

    # Grabs the locations aisle
    #
    aisle = ''.join([name for name in aisleList[aisle] if not name.isdigit()])

    # Gets the rack number in the aisle
    #
    num   = pos(side, row)

    # Format the position in the rack
    #
    loc   = f"A0{loc+1}"

    return f"{aisle}0{num}{loc}"


def pos(side, row):

    # First rack row
    #
    if not row: row += 1

    # Right side
    #
    if side: return row * 2

    # Left side
    #
    else: return (row + 1) * 2
    


