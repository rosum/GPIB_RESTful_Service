class Gpib:

    def __init__(self, adress, foo):
        self.adress = adress
        self.foo = foo


    def read(self, sample_size):
        return "KETHLEY 2015 THD"

    def write(self, query):
        return True