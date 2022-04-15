class Auto:
    def __init__ (self, modelis, spalva):
        self.modelis = modelis
        self.spalva = spalva

    def vaziuoti (self):
        print("Važiuoja")

    def plautis (self):
        print ("Plovykloje")

    def stoveti (self):
        print("Stovi")

automobilis = Auto ("Tesla Model Y", "mėlyna")
automobilis.vaziuoti()
automobilis.stoveti()