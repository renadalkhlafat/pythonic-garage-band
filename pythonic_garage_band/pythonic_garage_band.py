from abc import abstractmethod

class Musician:
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def __str__(self):
        pass
    @abstractmethod
    def __repr__(self):
        pass
    @abstractmethod
    def get_instrument(self):
        pass
    @abstractmethod
    def play_solo(self):
        pass

class Band(Musician):
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)
    def play_solos(self):
        solos_member = []
        for member in self.members:
            solos_member.append(member.play_solo())
        return solos_member
    @abstractmethod
    def __str__(self):
        return f" band {self.name}"
    @abstractmethod
    def __repr__(self):
       return f"{self.name}"
    @classmethod
    def to_list(cls):
        return cls.instances

        


class Guitarist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    def get_instrument(self):
        return 'guitar'
    def play_solo(self):
        return 'face melting guitar solo'

class Drummer(Musician):

    def __str__(self):
        return f"My name is {self.name} and I play drums"
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    def get_instrument(self):
        return 'drums'
    def play_solo(self):
        return 'rattle boom crash'

class Bassist(Musician):

    def __str__(self):
        return f"My name is {self.name} and I play bass"
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    def get_instrument(self):
        return 'bass'
    def play_solo(self):
        return 'bom bom buh bom'

if __name__ == "__main__":
    Joan = Guitarist('Joan Jett')
    Sheila = Drummer('Sheila E.')
    Meshell = Bassist('Meshell Ndegeocello')

    print(Joan)
    print(Sheila)
    print(Meshell)