from televisores.tv import TV

class Control:

    def __init__(self):
        self.tv= None

    def turnOn(self):
        self.tv.turnOn()

    def turnOff(self):
        self.tv.turnOff()

    def canalUp(self):
        self.tv.canalUp()
    
    def canalDown(self):
        self.tv.canalDown()

    def volumenUp(self):
        self.tv.volumenUp()

    def volumenDown(self):
        self.tv.volumenDown()

    def setCanal(self, canal):
        self.tv.setCanal(canal)

    def setVolumen(self, volumen):
        self.tv.setVolumen(volumen)

    def enlazar(self, tev):
        self.tv= tev
        self.tv.setControl(self)

    def getTv(self):
        return self.tv

    def setTv(self, tel):
        self.tv= tel