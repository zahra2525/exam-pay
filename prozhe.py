class income():
    
    def __init__(self, saat, mizan):
        self.saat = saat
        self.mizan = mizan
pul = income(int(input("please enter hours : ")), 15)
if pul.saat > 40 :
    result = (pul.saat - 40) * (15) + 400
    print("pardakht mishavad : " , result )     
else :
    print ("pardakht mishavad: " , pul.saat * pul.mizan)