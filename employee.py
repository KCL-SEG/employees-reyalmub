"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, salary, hrs = 0, commission = False, commissionType = "", contractNumber = 0, comPerConstract = 0, bonus = 0):
        self.name = name
        self.contract = contract
        self.salary = salary
        self.hrs = 0
        self.commission = False
        self.commissionType = ""
        self.contractNumber = 0
        self.comPerConstract = 0
        self.bonus = 0
    def get_pay(self):
        if self.contract.equals("hourly"):
            self.salary = self.hrs * self.salary
        if self.commissionType.equals("contract"):
            self.salary += (self.contractNumber * self.comPerConstract)
        if self.commissionType.equals("bonus"):
            self.salary += self.bonus
        return self.salary

    def __str__(self):
        description = f'{self.name} works on a {self.contract} of {self.salary} '
        if self.contract.equals("contract"):
            description += f'hours at {str(self.hrs)}/hour. '
        if self.commission:
            if self.commission.equals("contract"):
                description += f'receives a commission for {str(self.contractNumber)} contract(s) at {str(self.comPerConstract)}/contract. '
            else: 
                description += f'receives a {self.commissionType} commission of {str(self.bonus)}.'
        description += f'Their total pay is {str(self.get_pay())}'
        return description 


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',"monthly",4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',"contract",100,25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',"monthly salary",3000,commission=True, commissionType="contract",contractNumber= 4, comPerConstract=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',"contract",150,25,True,"contract",3,220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',"monthly salary",2000,commission=True, commissionType="bonus",bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
# ariel = Employee('Ariel')
