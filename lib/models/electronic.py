class Electronic:
    def _init_(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price
        self.features = []

    def _repr_(self):
        return f"<Electronic(name={self.name}, brand={self.brand}, price={self.price})>"