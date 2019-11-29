class GpibRegister:

    def __init__(self):

        self.devices = {}



    def register_gpib_device(self, adress):
        self.devices['adress'] = "Gpib Dummy " + str(adress)

        return self.devices['adress']

    def get_gpib_by_adress(self, adress):

        return self.devices['adress']

