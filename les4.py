
class Computer:
     def __init__(self,ram, cpu,ssd,cores,mother_board):
        self.ram=ram
        self.cpu=cpu
        self.ssd=ssd
        self.cores=cores
        self.mother_board=mother_board


     def info(self):
         print(f'Ram: {self.ram} GB')
         print(f'CPU: {self.cpu} GB')
         print(f'SSD: {self.ssd} GHz')
         print(f'Cores: {self.cores}')
         print(f'Mother Board: {self.mother_board}')

asusPC = Computer(16,4.4,256,4,'Asus ZTX 125')
asusPC.info()

class GameComputer(Computer):
    def __init__(self,gpu,ram,cpu,ssd,cores,mother_board):
        super().__init__(ram,cpu,ssd,cores,mother_board)
        self.gpu= gpu

    def info(self):
        super().info()
        print(f'GPU: {self.gpu} GB')

print('\nGame Computer:')
class Display:
    inc=5.6
    brand='Samsung'
    def info(self):
        print(f'Display: {self.brand} {self.inc}')

class Smartphone(Computer,Display):
    def info(self):
        print(f'Display: {self.brand} {self.inc}')
        print(f'CPU: {self.cpu} GHz {self.ram} GB')
LenovoLegion=GameComputer("Nvidia 1660", 32,512,4.4,8,'Gbyte')
LenovoLegion.info()