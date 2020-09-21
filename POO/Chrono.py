class Chrono:
  def __init__(self, h, m, s):
    self.heures = h
    self.minutes = m
    self.secondes = s

  def affiche(self) :
    print("il est {0} heures, {1} minutes et {2} secondes".format(self.heures, self.minutes, self.secondes))

  def avance(self, s) :
    self.secondes += s
    self.minutes += self.secondes // 60
    self.secondes = self.secondes % 60

    self.heures += self.minutes // 60
    self.minutes = self.minutes % 60



t = Chrono(10,59,58)
t.affiche()
t.avance(16)
t.affiche()