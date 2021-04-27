class arme:
    def __init__(self, nom, degats, utilisation):
        self.nom = nom
        self.degats = degats
        self.utilisation = utilisation

    def get_nom(self):
        return self.nom

    def get_degats(self):
        return self.degats

    def get_utilisation(self):
        return self.utilisation

    def utilise(self, use):
        self.utilisation = self.utilisation - use
        return self.utilisation
