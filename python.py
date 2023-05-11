class Milli_On():
    def _init_(self):
        pass
class Komunal_xidmetler(Milli_On):
    def _init_(self,abune_kodu="12345678"):
        self.kod=abune_kodu
class Azerqaz(Komunal_xidmetler):
    def _init_(self,abune_kodu="12345678",balans=50):
        self.abune_kodu=abune_kodu
        self.balans=balans
    def secim(self,abune_kodu="12345678",balans=50):
        self.balans=balans
        print("[1]-ehali\n[2]-qeyri-ehali\n[3]-istixana")
        secim=int(input("birini secin :"))
        if secim==1:
            self.kod=input("abune kodunu yazin :")
            if len(self.kod)!=8:
                print("abune kodunuz sevdir yeniden yoxlayin!")
            else:
                    if self.kod==abune_kodu:
                        medaxil=int(input("yuklemek istediyiniz belegi yazin :"))
                        print("BALANS :",self.balans+medaxil)
                    else:
                        print("abune kodunuz yalnisdir")

        if secim==2:
            
            self.kod=input("abune kodunu yazin :")
            if len(self.kod)!=8:
                print("abune kodunuz sevdir yeniden yoxlayin!")
            else:
                    if self.kod==abune_kodu:
                        medaxil=int(input("yuklemek istediyiniz belegi yazin :"))
                        print("BALANS :",self.balans+medaxil)
                    else:
                        print("abune kodunuz yalnisdir")
        if secim==3:
            self.kod=input("abune kodunu yazin :")
            if len(self.kod)!=8:
                print("abune kodunuz sevdir yeniden yoxlayin!")
            else:
                if self.kod==abune_kodu:
                    medaxil=int(input("yuklemek istediyiniz belegi yazin :"))
                    print("BALANS :",self.balans+medaxil)
                else:
                    print("abune kodunuz yalnisdir")
                            
class Azerisiq(Komunal_xidmetler):
    def _init_(self,abune_kodu="123456789",balans=50):
        self.balans=balans
        self.abkod=abune_kodu
        pass
    def giris(self,abune_kodu="123456789",balans=50):
        self.balans=balans
        self.kod=input("abune kodunuzu yazin :")
        if len(self.kod)==9 :
            if self.kod==abune_kodu:
                self.medaxil=int(input("yuklemek istediyiniz meblegi yazin :"))
                print("BALANS :",self.balans+self.medaxil)
            
        else:
            print("abune kodunuz 9 reqemden ibaret olmalidir")
            
            
class Azersu(Komunal_xidmetler):
    def _init_(self,balans=50,abune_kodu="123456789"):
        pass
    def secim(self,abune_kodu="123456789",balans=50):
        print("[1]-ehali\n[2]-Qeyri-ehali")
        self.balans=balans
        secim=int(input("birini secin :"))
        if secim==1:
                self.kod=input("abune kodunuzu yazin :")
                if len(self.kod)==9 :
                    if self.kod==abune_kodu:
                        self.medaxil=int(input("yuklemek istediyiniz meblegi yazin :"))
                        print("BALANS :",self.balans+self.medaxil)
                else:
                    print("abune kodunuz 9 reqemden ibaret olmalidir")
        elif secim==2:
                self.kod=input("abune kodunuzu yazin :")
                if len(self.kod)==10 :
                    if self.kod==self.abkod:
                        self.medaxil=int(input("yuklemek istediyiniz meblegi yazin :"))
                        print("BALANS :",self.balans+self.medaxil)
                else:
                    print("abune kodunuz 10 reqemden ibaret olmalidir")
#------------------------------------------------------------------------------------------------------
class Bank_xidmetleri(Milli_On):
    def _init_(self):
        pass
    
class Uni_bank(Bank_xidmetleri):
    def _init_(self,borc=500,balans=1000):
        self.borc=borc
        self.balans=balans
        
    def secim(self,kart_kodu="4169 7851 5958 8495",balans=1000,borc=500):
        self.borc=borc
        self.balans=balans
        print("[1]-balans artimi\n[2]kredit odenisi")
        self.secim=int(input("birini secin :"))
        if self.secim==1:
                self.kart_kodu=input("kart normresini daxil edin :")
                if self.kart_kodu==kart_kodu:
                    print("ISTIFADECI : Ali Alizade ")
                    self.medaxil=int(input("ne qeder mebleg daxil etmek isteyirsiniz :"))
                    print("BALANS :",self.balans+self.medaxil)
                else:
                    print("bele bir istifadeci yoxdur")
        elif self.secim==2:
                self.kart_kodu=input("kart normresini daxil edin :")
                if self.kart_kodu==kart_kodu:
                    print("ISTIFADECI : Ali Alizade ")
                    self.medaxil=int(input("borcunuzdan ne qeder odemek isteyirsiniz :"))
                    print("QALAN BORCUNUZ :",self.borc-self.medaxil)
                    
class Pasha_bank(Bank_xidmetleri):
    def _init_(self,borc=500,balans=1000):
        self.borc=borc
        self.balans=balans
    def secim(self,kart_kodu="4169 7851 5958 8495",balans=1000,borc=500):
        self.borc=borc
        self.balans=balans
        print("[1]-balans artimi\n[2]kredit odenisi")
        self.secim=int(input("birini secin :"))
        if self.secim==1:
                self.kart_kodu=input("kart normresini daxil edin :")
                if self.kart_kodu==kart_kodu:
                    print("ISTIFADECI : Ali Alizade ")
                    self.medaxil=int(input("ne qeder mebleg daxil etmek isteyirsiniz :"))
                    print("BALANS :",self.balans+self.medaxil)
                else:
                    print("bele bir istifadeci yoxdur")
        elif self.secim==2:
                self.kart_kodu=input("kart normresini daxil edin :")
                if self.kart_kodu==kart_kodu:
                    print("ISTIFADECI : Ali Alizade ")
                    self.medaxil=int(input("borcunuzdan ne qeder odemek isteyirsiniz :"))
                    print("QALAN BORCUNUZ :",self.borc-self.medaxil)
class Kapital_bank(Bank_xidmetleri):
    def _init_(self,borc=500,balans=1000):
        self.borc=borc
        self.balans=balans
    def secim(self,kart_kodu="4169 7851 5958 8495",balans=1000,borc=500):
        self.borc=borc
        self.balans=balans
        print("[1]-balans artimi\n[2]kredit odenisi")
        self.secim=int(input("birini secin :"))
        if self.secim==1:
                self.kart_kodu=input("kart normresini daxil edin :")
                if self.kart_kodu==kart_kodu:
                    print("ISTIFADECI : Ali Alizade ")
                    self.medaxil=int(input("ne qeder mebleg daxil etmek isteyirsiniz :"))
                    print("BALANS :",self.balans+self.medaxil)
                else:
                    print("bele bir istifadeci yoxdur")
        elif self.secim==2:
                self.kart_kodu=input("kart normresini daxil edin :")
                if self.kart_kodu==kart_kodu:
                    print("ISTIFADECI : Ali Alizade ")
                    self.medaxil=int(input("borcunuzdan ne qeder odemek isteyirsiniz :"))
                    print("QALAN BORCUNUZ :",self.borc-self.medaxil)
#----------------------------------------------------------------------------------------------------
class Mobil_operatorlar(Milli_On):
    def _init_(self):
        pass
class Azercell(Mobil_operatorlar):
    def prefiks_yoxlama(self,prefiks1="050",prefiks2="050",prefiks3="50",prefiks4="51"):
        self.prefiks1=prefiks1
        self.prefiks2=prefiks2
        self.prefiks3=prefiks3
        self.prefiks4=prefiks4
        prefiks=input("prefiksi yazin :")
        if prefiks==self.prefiks1 or prefiks==self.prefiks2 or prefiks==self.prefiks3 or prefiks==self.prefiks4:
                self.norme=int(input("normenizi daxil edin "))
                print(f"{prefiks}-{self.norme}")
                self.medaxil=int(input("ne qeder yuklemek isteyirsiniz :"))
                print("emeliyyat ugurla tamamlandi")
        else:
            print("sehv  operatora gelmisiniz")
     
class Bakcell(Mobil_operatorlar):
    def _init_(self,prefiks1="055",prefiks2="55"):
        self.prefiks1=prefiks1
        self.prefiks2=prefiks2  
    def prefiks_yoxlama(self,prefiks1="055",prefiks2="55"):
        self.prefiks1=prefiks1
        self.prefiks2=prefiks2 
        prefiks=input("prefiksi yazin :")
        if prefiks==self.prefiks1 or prefiks==self.prefiks2 :
                self.norme=int(input("normenizi daxil edin "))
                print(f"{prefiks}-{self.norme}")
                self.medaxil=int(input("ne qeder yuklemek isteyirsiniz :"))
                print("emeliyyat ugurla tamamlandi")
        else:
            print("sehv  operatora gelmisiniz")
class Nar(Mobil_operatorlar):
    def prefiks_yoxlama(self,prefiks1="070",prefiks2="077",prefiks3="77",prefiks4="70"):
        self.prefiks1=prefiks1
        self.prefiks2=prefiks2
        self.prefiks3=prefiks3
        self.prefiks4=prefiks4
        prefiks=input("prefiksi yazin :")
        if prefiks==self.prefiks1 or prefiks==self.prefiks2 or prefiks==self.prefiks3 or prefiks==self.prefiks4:
                self.norme=int(input("normenizi daxil edin "))
                print(f"{prefiks}-{self.norme}")
                self.medaxil=int(input("ne qeder yuklemek isteyirsiniz :"))
                print("emeliyyat ugurla tamamlandi")
        else:
            print("sehv  operatora gelmisiniz")
#---------------------------------------------------------------------------------------------------------------
print("""
[1]-Komunal xidmetler
[2]-Bank xidmetleri
[3]-Mobil operatorlar
""")
secim=int(input("birini secin :"))
if secim==1:
    print(""""
[1]-Azerqaz
[2]-Azerisiq
[3]-Azersu
""")    
    secim1=int(input("birini secin :"))
    if secim1==1:
        istifadeci=Azerqaz()
        istifadeci.secim()
        
    if secim1==2:
        istifadeci=Azerisiq()
        istifadeci.giris()
    if secim1==3:
        istifadeci=Azersu()
        istifadeci.secim()
        
if secim==2:
    print("""
[1]-Uni bank
[2]-Pasha bank
[3]-Kapital bank
""")
    secim2=int(input("birini secin :"))
    if secim2==1:
        istifadeci=Uni_bank()
        istifadeci.secim()
    if secim2==2:
        istifadeci=Pasha_bank()
        istifadeci.secim()
    if secim2==3:
        istifadeci=Kapital_bank()
        istifadeci.secim()
if secim==3:
    print("""
[1]-Azercell
[2]-Bakcell
[3]-Nar
""")
    secim3=int(input("birini secin :"))
    if secim3==1:
        istifadeci=Azercell()
        istifadeci.prefiks_yoxlama()
    if secim3==2:
        istifadeci=Bakcell()
        istifadeci.prefiks_yoxlama()
    if secim3==3:
        istifadeci=Nar()
        istifadeci.prefiks_yoxlama()