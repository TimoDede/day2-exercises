class Mammals:
    def __init__(self):
        """
        Constructor for this class
        """
        # Create a list of animals which are mammals
        self.members = ["Tiger", "Elefant", "Wildcat"]

    def printMembers(self):
        print("Printing members of the Mammals class ")
        for member in self.members:
            print('\t%s ' % member)