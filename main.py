Bank_Balance = 200
print(
    'To win this, you have to have more than 20 Dollars at the end of the Game.'
)
print('')
print('You Have 200 Dollars in your bank account')
print('')
print('Now you Have to choose something for Breakfast')
print('')
B = input('5 Star Pancakes are 30 dollars or 5 Dollar Starbucks\n')

if B == '5 Star Pancakes':
    Bank_Balance = Bank_Balance - 30
    print('You now Have 170 Dollars in your Bank Account')
if B == 'Starbucks':
    Bank_Balance = Bank_Balance - 5
    print('You now Have 195 Dollars in your Bank Account')

print('')
print('Next, You Can go Shopping')
S = input('You can go to Gucci For 50 Dollars or H&M for 25 Dollars\n')
if S == 'Gucci':
    Bank_Balance = Bank_Balance - 50
    print('You Now have', Bank_Balance, 'Dollars in your bank Account')
if S == 'H&M':
    Bank_Balance = Bank_Balance - 25
    print('You now have', Bank_Balance, 'Dollars in you Bank Account')
print('')
print('Next You Can go to a Movie')
M = input('Deluxe Tickets are 30 Dollars and Normal tickets are 15\n')
if M == 'Deluxe':
    Bank_Balance = Bank_Balance - 30
    print('You Now have', Bank_Balance, 'Dollars in your Account')
if M == 'Normal':
    Bank_Balance = Bank_Balance - 15
    print('You Now have', Bank_Balance, 'Dollars in your Account')
print('')
print('Next, Its time for lunch')
L = input(
    'You can Choose a 5 Dollar Salad or A Burger Meal Worth 30 Dollars\n')
if L == 'Salad':
    Bank_Balance = Bank_Balance - 5
    print('You have', Bank_Balance, 'Dollars left in your Account')
if L == 'Burger Meal':
    Bank_Balance = Bank_Balance - 30
    print(Bank_Balance, 'Dollars is left in your account')
print('')
print('Next, you will be going to an Amusement Park')
A = input(
    'All Ride Deluxe Tickets are 40 Dollars or Normal Tickets are 20 Dollars\n'
)
if A == 'Deluxe':
    Bank_Balance = Bank_Balance - 40
    print(Bank_Balance, 'Dollars is left in your Account')
if A == 'Normal':
    Bank_Balance = Bank_Balance - 20
    print(Bank_Balance, 'Dollars is left in your Account')
print('')
print('Lastly, Its time for Dinner!')
D = input('Choose one Option: Chipotle is $10 or McDonalds which is $5')
if D == 'Chiptole':
    Bank_Balance = Bank_Balance - 10
    print('You have', Bank_Balance, 'Dollars in your account')
if D == 'McDonalds':
    Bank_Balance = Bank_Balance - 5
    print('You have', Bank_Balance, 'Dollars in your account')
if Bank_Balance >= 25:
    print("Good Job! You spent your money well!")
if Bank_Balance < 25:
    print("You might want to Spend smartly next time")
