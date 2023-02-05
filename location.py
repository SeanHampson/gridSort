# location.py

class Location:
    def __init__(self, aisle, side, row, loc, customerCode, quantity):

        # 0-7 for 8 aisles KA, KB, KC, KD, KE, VC, WC, KK
        #
        self.aisle = aisle

        # 0-1 for 2 sides right or left
        #
        self.side = side  

        # EQ 0 - (totalLocations / 3) * 0.5
        #
        self.row  = row 

        # 0-2 for locations A01, A02, A03
        # 
        self.loc  = loc   # 0-2 for locations A01, A02, A03
        
        # Owner of this location
        #
        self.customerCode = customerCode

        # Amount of packs in the customers order
        #
        self.quantity = quantity

    def needShelf(self):

        # Does this location require a shelf?
        #
        if self.quantity >= 25: 
            return True
        return False

    def nextLocation(self):

        # Goes forward by 1 location in the current aisle
        #
        if self.loc == 2:
            return f"{self.aisle} {self.side} {self.row+1} 0"
        else:
            return f"{self.aisle} {self.side} {self.row} {self.loc+1}"

    def prevLocation(self):
        
        # Goes back by 1 location in the current aisle
        #
        if self.loc == 0:
            return f"{self.aisle+1} {self.side} {self.row-1} 2"
        else:
            return f"{self.aisle} {self.side} {self.row} {self.loc-1}"

    def __str__(self):

        # Returns the location on the grid
        #
        return f"{self.aisle} {self.side} {self.row} {self.loc}"
    
    def __eq__(self, other): 
        
        # Check if 2 locations have matching customer codes
        #
        if isinstance(other, Location):
            return self.customerCode == other.customerCode
        return False

    def __ne__(self, other):

        # Check if 2 locations don't have matching customer codes
        #
        if isinstance(other, Location):
            return self.customerCode != other.customerCode
        return False
    
    def __repr__(self):

        # Location is represented by its owner
        #
        return f"{self.customerCode}"