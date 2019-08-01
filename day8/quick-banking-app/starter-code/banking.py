class BankAccount():
    def __init__(self,label,balance):
        self.label = label
        self.balance = balance
    
    def __str__(self):
        return self.label + ": " + str(self.balance)
    20
    def withdraw(self,widthdraw):
        if widthdraw<0:
            print "you cannot widthdraw negative amounts"
        elif widthdraw>self.balance:
            print "You cannot widthdraw more than what you have in your account"
        else: 
            self.balance =self.balance-widthdraw
            print "you have widthdrawed " + str(widthdraw) +" from your account"
    



    def deposit(self,deposit):
        if deposit <0:
            print "cannot deposit negative value"
        else:
            self.balance=self.balance+deposit

    def rename(self,name):
        if name == '':
            print "please enter a label name"
        else:
            self.label=name



    