class Atm () :
    def __init__ (self,cardNum,pin,bal) :
        self.cardNum=cardNum
        self.pin=pin
        self.bal=1000
    
    def balanceWD (self,num) :
        self.bal=self.bal+num
        print('Balance has been changed by', num)
    
    def checkBal (self,bal) :
        print(self.bal)
    
user_0=Atm(0,'n20q9wufsdvniqiwa345qtw',1000000000000)
