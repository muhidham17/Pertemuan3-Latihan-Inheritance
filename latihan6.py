from abc import ABCMeta, abstractmethod
import math

class Bangun3D(metaclass=ABCMeta):
  def cetakData(self):
    pass
  def hitungVolume(self):
    pass
  def cetakVolume(self):
    pass
    
class Kotak(Bangun3D):
  def __init__(self, p, l=None, t=None):
    if l == None and t == None:
      self.panjang = self.lebar = self.tinggi = p
    else:
      self.panjang = p
      self.lebar = l
      self.tinggi = t
  
  def cetakData(self):
    print("Panjang\t: ", self.panjang)
    print("Lebar\t: ", self.lebar)
    print("Tinggi\t: ", self.tinggi)
    
  def hitungVolume(self):
    return self.panjang * self.lebar * self.tinggi
    
  def cetakVolume(self):
    print("Volume Kotak \t= ", self.hitungVolume())
    
class Tabung(Bangun3D):
  def __init__(self, r, t):
    self.jarijari = r
    self.tinggi = t
    
  def cetakData(self):
    print("Jari-jari alas\t: ", self.jarijari)
    print("Tinggi tabung \t: ", self.tinggi)
    
  def hitungVolume(self):
    return math.pi * pow(self.jarijari, 2) * self.tinggi
  
  def cetakVolume(self):
    print("Volume tabung \t= ", self.hitungVolume())

def main():
  obj1 = Kotak (6, 5, 4)
  print("BALOK")
  obj1.cetakData()
  obj1.cetakVolume()
  
  obj2 = Kotak (5)
  print("\nKUBUS")
  obj2.cetakData()
  obj2.cetakVolume()
  
  obj3 = Tabung (3, 4)
  print("\nTABUNG")
  obj3.cetakData()
  obj3.cetakVolume()
  
if __name__ == "__main__":
  main()
