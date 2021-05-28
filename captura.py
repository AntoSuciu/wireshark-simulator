from scapy.all import *
from scapy.layers.inet import TCP, UDP, IP, Ether
import matplotlib.pyplot as plt
from pachet import *
import os
import functools



class Captura():
    _captura = None

    @staticmethod
    def getCaptura(self):
        if Captura._captura == None:
            Captura(self)
        return Captura._captura

    def __init__(self):
        pass

    def functie_apelata(func):
        @functools.wraps(func)
        def wrapper(*args):
            wrapper.has_been_called = True
            return func(*args)

        wrapper.has_been_called = False
        return wrapper

    @functie_apelata
    def captura_pachete(self):
        self.pachete = sniff(count=10)
        for pachet in self.pachete:
            print(pachet.show())
        print("\n")


    def grafic_pachete(self):
        pachete_retea = [len(self.pachete[TCP]), len(self.pachete[UDP])]
        eticheta = ['TCP', 'UDP']
        plt.pie(pachete_retea, labels=eticheta, startangle=90,
                shadow=True, autopct='%.2f%%')
        plt.title('TCP/UDP ratio')
        plt.show()

    def salvare_json(self):
        pachete_json = []
        for i in range(0,len(self.pachete)):
            if self.pachete[i].haslayer(IP) and self.pachete[i].haslayer(TCP):
                pachete_json.append(Pachet(self.pachete[i][Ether].dst,
                                           self.pachete[i][Ether].src,
                                           self.pachete[i][IP].dst,
                                           self.pachete[i][IP].src,
                                           self.pachete[i][IP].version,
                                           self.pachete[i][IP].proto,
                                           self.pachete[i][TCP].sport,
                                           self.pachete[i][TCP].dport,
                                           #self.pachete[i][UDP].sport,
                                           #self.pachete[i][UDP].dport,
                                           " ",
                                           " "
                                                                                      ))
            elif self.pachete[i].haslayer(UDP) and self.pachete[i].haslayer(IP):
                    pachete_json.append(Pachet(self.pachete[i][Ether].dst,
                                               self.pachete[i][Ether].src,
                                               self.pachete[i][IP].dst,
                                               self.pachete[i][IP].src,
                                               self.pachete[i][IP].version,
                                               self.pachete[i][IP].proto,
                                               #self.pachete[i][TCP].sport,
                                               #self.pachete[i][TCP].dport,
                                               " ",
                                               " ",
                                               self.pachete[i][UDP].sport,
                                               self.pachete[i][UDP].dport
                                               ))

        for j in range(0,len(pachete_json)):
            print(pachete_json[j].__str__())

        nume_fisier = "informatii_pachete.json"
        cale_completa = os.getcwd()+"\\"+nume_fisier

        with open(cale_completa,'w', encoding="UTF-8") as f:
            for i in range(0,len(pachete_json)):
                json.dump(pachete_json[i].__str__().split("\n"), f, indent = 4)

