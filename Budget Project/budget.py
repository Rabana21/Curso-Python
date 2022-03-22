class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = list()

  def deposit(self, amount, dscrpt = ''):
    dic = dict()
    dic['amount'] = amount
    dic['description'] = dscrpt
    self.ledger.append(dic)

  def withdraw(self, amount, dscrpt = ''):
    founds = True
    if self.check_funds(amount):
      dic = dict()
      dic['amount'] = - amount
      dic['description'] = dscrpt
      self.ledger.append(dic)
    else:
      founds = False

    return founds

  def get_balance(self):
    allamount = 0
    for transaction in self.ledger:
      allamount += transaction['amount'] 
    return allamount

  def transfer(self, amount, budget):
    dscrpt = 'Transfer to ' + budget.name 
    operation = self.withdraw(amount, dscrpt)
    if operation:
      dscrpt = 'Transfer from ' + self.name
      budget.deposit(amount, dscrpt)

    return operation

  def check_funds(self, amount):
    balance = self.get_balance()
    greater = False
    if amount <= balance:
      greater = True

    return greater

  def spent(self):
    spnts = 0
    for dict in self.ledger:
      spnt = dict['amount']
      if spnt < 0:
        spnts += spnt
    return spnts 
    
  def __str__(self):
    prnt = ''
    prnt += self.name.center(30,'*') + '\n'
    for trns in self.ledger:
      prnt += trns['description'][:23].ljust(23) + '{:.2f}'.format(trns['amount']).rjust(7) + '\n'
    prnt += 'Total: '+ str(self.get_balance()) 
    return prnt

def total_spent(categories):
  tspent = 0
  for category in categories:
    tspent += category.spent()
    

  return tspent

def truncate_ten(number):
  return round(number / 10) * 10

def max_len(categories):
  max_num = -1
  for category in categories:
    if len(category.name) > max_num:
      max_num = len(category.name)
  return max_num
def create_spend_chart(categories):
  title = 'Percentage spent by category\n'
  line = ''
  sub_line = ''
  tspent = total_spent(categories)
  dic = dict()
  num_categories = len(categories) * 3
  sub_line = '    ' + ''.rjust(num_categories, '-') + '\n'
  
  for category in categories:
    spent = category.spent()
    prcnt = spent / tspent * 100
    dic[category.name] =  truncate_ten(round(prcnt)) 

  for index in range(100, 0, -10):
    line += str(index).rjust(3) + '|'  
    for category in categories:
      prct = dic[category.name]
      if prct >= index:
        line += 'o'.center(3)
      else:
        line += ' '.center(3)
    line += '\n'

  for index in range(max_len(categories)):
    sub_line += '\n    ' 
    for category in categories:
      name = category.name
      if len(name) > index:
        sub_line += name[index].center(3)
      else:
        sub_line += ' '.center(3)
  
  return title + line + sub_line.rjust(4+num_categories)

  
    
  