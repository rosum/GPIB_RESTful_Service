import Gpib
from time import time

class GpibService:

    def __init__(self):

        self.devices = {}



    def register_gpib_device(self, adress):

        try:
            self.devices[adress] = Gpib.Gpib(0, adress)

            return {"status": "registered",
                    "adress": adress}
        except:
            return {"status": "registration_failed",
                    "adress": adress}

    def purge_gpib_device(self, adress):

        del self.devices[adress]

        return {"status": "purged",
                "adress": adress}


    def gpib_write_read(self, adress, query):

        gpib = self.devices[adress]
        gpib.write(query)
        data = gpib.read(100)

        return {"data" : data,
                "time" : time(),
                "adress" : adress}

    def read_gpib(self, adress):

        gpib = self.devices[adress]
        data = gpib.read(100)

        return {"data": data,
                "time" : time(),
                "adress": adress}

    def write_gpib(self, adress, query):

        gpib = self.devices[adress]
        gpib.write(query)

        return {"time" : time(),
                "adress" : adress}
