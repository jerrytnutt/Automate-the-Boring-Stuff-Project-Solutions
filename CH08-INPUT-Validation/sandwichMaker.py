# Write a program that asks users for their sandwich preferences. 
# Come up with prices these options and display a total cost.

import pyinputplus as pyip

def order_sandwich():
  price_dict = {'chicken':6.99,'turkey':5.99,'ham':5.79,'tofu':8.99,'cheddar':0.25, 'Swiss':0.50,'mozzarella':0.25,'no':0}
  number_of_sandwiches = pyip.inputInt('How many sandwiches would you like today? ', min=1)
  sandwich_list = []
  total_price = 0

  for i in range(number_of_sandwiches):
    print('What would you like for your bread and protein?\n')
    bread_type = pyip.inputMenu(['wheat', 'white','sourdough'])
    protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham','tofu'])

    cheese_input = pyip.inputYesNo('Would you like any cheese?\n')
    if cheese_input == 'yes':
      cheese_type = pyip.inputMenu(['cheddar', 'Swiss','mozzarella'])
    else:
      cheese_type = 'no'

    mayo_input = pyip.inputYesNo('Would You Like any Mayo? ')
    mustard_input = pyip.inputYesNo('Would You Like any Mustard?')
    lettece_input = pyip.inputYesNo('Would You Like any Lettece? ')
    tomato_input = pyip.inputYesNo('Would You Like any Toamato? ')

    input_list = [mayo_input,mustard_input,lettece_input,tomato_input ]
    addition_names = ['mayo','mustard','lettece','tomato']
    included_extras = []

    for i in range(4):
      if input_list[i] == 'yes':
        included_extras.append(addition_names[i])

    
    # Append newly created sandwich to sandwich list
    sandwich_list.append([protein_type,bread_type,cheese_type,included_extras])

  for sandwiches in sandwich_list:
    # Set price based on meat and cheese
    total_price += (price_dict[sandwiches[0]] + price_dict[sandwiches[2]])
    if len(sandwiches[-1]) == 0:
      included_extras = 'no toppings'
    else:
      included_extras = ", ".join(sandwiches[-1])
    print('You orderd a {} sandwich with {} bread and {} cheese, with {}.'.format(sandwiches[0],sandwiches[1],sandwiches[2],included_extras))
  print('Your total comes to ${}'.format(round(total_price,3)))

order_sandwich()