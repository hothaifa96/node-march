class BankAccount:
    def __init__(self, owner, id, balance, credit_score=5):
        self.owner = owner
        self.id = id
        self.balance = balance
        self.credit_score = credit_score

    def withdraw(self, amount):
        pass

    def deposite(self, amount):
        pass


class PrivateBankAccount(BankAccount):
    def __init__(self,owner, id, balance, credit_score, teller):
        super().__init__(owner, id, balance, credit_score)
        self.teller = teller

    def withdraw(self, amount):
        self.balance -= amount+5
    def deposite(self, amount):
        self.balance += amount-5

    def __str__(self):
        return f'{self.owner} has {self.balance}'

    def __eq__(self, other):
        return self.id == other.id
    def __ge__(self, other):
        return self.balance >= other.balance
    def __len__(self):
        return 55
    def __add__(self, other):
        return PrivateBankAccount(f'{self.owner} {other.owner}',111,self.balance + other.balance,11,'fga')


acc1 = PrivateBankAccount('gitam','2197',195000,9,'avraham')
acc2 = PrivateBankAccount('kim','2197',-900,2,'shahr')

# print(acc1)
# print(acc2)
# acc1.deposite(790)
# acc2.withdraw(250)
# print(acc1)
# print(acc2)

print(acc2 >= acc1)
print(len(acc2))
print(acc1+acc2)