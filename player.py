class player:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def get_nom(self):
        return self.nom

    def get_vie(self):
        return self.vie

    def degats(self, damage):
        self.vie = self.vie - damage
        return self.vie
