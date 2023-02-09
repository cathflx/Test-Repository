#Python Program Tax Calculator based on the Income Tax Tables Under TRAIN

def income(): #function for annual income
  annual_income = monthly_income * 12 #determines the annual income based on the monthly income input
  return annual_income #calls the variable annual_income

def monthly_income_tax(): #function for monthly income tax
  monthly_tax = annual_tax / 12 #divides the annual tax by 12 to determine monthly tax
  return monthly_tax #calls the variable annual_income
  
def first_income_tax(): #function for first condition of tax rate
  income_tax = 0 #no rate involved
  return income_tax #calls the income_tax

def second_income_tax(): #function for second condition of tax rate
  second_income_tax = annual_income - second_tax_rate
  return second_income_tax

def third_income_tax():
  third_income_tax = annual_income - third_tax_rate
  return third_income_tax

def fourth_income_tax():
  fourth_income_tax = annual_income - fourth_tax_rate
  return fourth_income_tax

def fifth_income_tax():
  fifth_income_tax = annual_income - fifth_tax_rate
  return fifth_income_tax

def sixth_income_tax():
  sixth_income_tax = annual_income - sixth_tax_rate
  return sixth_income_tax
  
monthly_income = float(input("What is your monthly income? "))

annual_income = income ()

first_tax_rate = 0
second_tax_rate = (annual_income - 250000) * 0.15
third_tax_rate = ((annual_income - 400000) * 0.2) + 22500
fourth_tax_rate = ((annual_income - 800000) * 0.25) + 102500
fifth_tax_rate = ((annual_income - 2000000) * 0.30) + 402500
sixth_tax_rate = ((annual_income - 8000000) * 0.35) + 2202500

print ("Your annual income is:",annual_income)

if annual_income <= 250000:
  annual_tax = first_income_tax ()
  print ()
  print ("Your income tax is", annual_tax)

elif annual_income > 250000 and annual_income <= 400000:
  annual_tax  = second_income_tax ()
  monthly_rate = monthly_income_tax ()
  print ()
  print ("Your annual income tax is", annual_tax )
  print ("Your monthly income tax is", monthly_rate)

elif annual_income > 400000 and annual_income <= 800000:
  annual_tax  = third_income_tax ()
  monthly_rate = monthly_income_tax ()
  print ()
  print ("Your income tax is", annual_tax )
  print ("Your monthly income tax is", monthly_rate)

elif annual_income > 800000 and annual_income <= 2000000:
  annual_tax  = fourth_income_tax ()
  monthly_rate = monthly_income_tax ()
  print ()
  print ("Your income tax is", annual_tax )
  print ("Your monthly income tax is", monthly_rate)

elif annual_income > 2000000 and annual_income <= 8000000:
  annual_tax  = fifth_income_tax ()
  monthly_rate = monthly_income_tax ()
  print ()
  print ("Your income tax is", annual_tax )
  print ("Your monthly income tax is", monthly_rate)

elif annual_income > 8000000:
  annual_tax  = sixth_income_tax ()
  monthly_rate = monthly_income_tax ()
  print ()
  print ("Your income tax is", annual_tax )
  print ("Your monthly income tax is", monthly_rate)