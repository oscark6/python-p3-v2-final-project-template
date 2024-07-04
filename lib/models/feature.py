class Feature:
    def _init_(self, name):
        self.name = name

    def _repr_(self):
        return f"<Feature(name={self.name})>"