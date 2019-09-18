class Kotak(object):
  def __init__ (self, p, l, t):
    self.panjang = p 
    self.lebar = l
    self.tinggi = t
  
  def hitungVolume(self):
    return self.panjang * self.lebar * self.tinggi
    
  def cetakData(self):
    print("Panjang\t: ", self.panjang)
    print("Lebar\t: ", self.lebar)
    print("Tinggi\t: ", self.tinggi)
    
  def cetakVolume(self):
    print("Volume\t= ", self.hitungVolume())
    
class KotakWarna(Kotak):
  def __init__ (self, p, l, t, w):
    self.panjang = p 
    self.lebar = l
    self.tinggi = t
    self.warna = w
  
  def cetakData(self):
    print("Panjang\t: ", self.panjang)
    print("Lebar\t: ", self.lebar)
    print("Tinggi\t: ", self.tinggi)
    print("Warna\t: ", self.warna)
    
def main():
  kotakwarna1 = KotakWarna (6, 5, 4, "Merah")
  kotakwarna1.cetakData()
  kotakwarna1.cetakVolume()
  
if __name__ == "__main__":
  main()
