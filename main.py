class Atm () :
    def __init__ (self,cardNum,pin,bal) :
        self.cardNum=cardNum
        self.pin=pin
        self.bal=bal
    
    def balanceWD (self,num) :
        self.bal=self.bal+num
        print('Balance has been changed by', num)
    
    def checkBal (self) :
        print(self.bal)
    
user_0=Atm(0,'n20q9wufsdvniqiwa345qtw',1000000000000)
user_0.balanceWD(500)
user_0.checkBal()
