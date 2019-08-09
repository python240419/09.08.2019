class BankAccout:
    def __init__(self, id,
                 fname, lname,
                 balance = 0):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.balance = balance
    def __str__(self):
        return f'BankAccount '\
    f'{self.id} {self.fname} {self.lname}'\
    f' {self.balance}'
    def __eq__(self, other):
        return self.balance == other.balance
    def __gt__(self, other):
        return self.balance > other.balance
    def __add__(self, other):
        return self.balance + other.balance

acc1 = BankAccout(1, 'Jim',
                  'Cohen', 4000)
acc2 = BankAccout(2, 'Suzi',
                  'Mark', 4005)
print(acc1)
print(acc2)
print (f'equal ? {acc1 == acc2}')
print (f'Bigger? {acc1 > acc2}')
print (f'sum: {acc1 + acc2}')
