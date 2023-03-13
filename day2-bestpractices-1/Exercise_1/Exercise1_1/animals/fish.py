class Fish():
    def __init__(self):
        """
        Constructor to this class
        """
        self.members = ["Salmon", "Tuna", "Cod"]

    def printMembers(self):
        print('Printing members of the Fish class')
        for member in self.members:
            print("\t%s " %member)