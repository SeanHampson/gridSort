# setup.py

# Number of aisles and their names for program to keep track of
#
def setup():

    # Layout file used for aisle names in order required e.g KA-KB-KC-KD-KE etc
    #
    with open("layout.txt", "r") as file:

        # List of aisle names given by layout.txt
        #
        aisleList  = [ais.strip('\n') for ais in file.readlines() if ais.strip()]
        
    return aisleList

