def main():
  
  pizza_count = get_pizza_count()
  delivery_needed = get_delivery_choice()
  tuesday_discount = get_tuesday_discount()
  app_used = get_app_usage()

  pizza_cost = calculate_pizza_cost(pizza_count, tuesday_discount)

  delivery_cost = calculate_delivery_cost(delivery_needed, pizza_count)


  total_price = pizza_cost + delivery_cost


  total_price = apply_app_discount(total_price, app_used)

  display_final_price(total_price)


def get_pizza_count():
  while True:
    try:
      count = int(input("How many pizzas ordered? "))
      if count > 0:
        return count
      else:
        print("Please enter a positive integer!")
    except ValueError:
      print("Please enter a number!")

def get_delivery_choice():
  while True:
    choice = input("Is delivery required? (Y/N) ").upper()
    if choice in ["Y", "N"]:
      return choice == "Y"
    else:
      print("Please answer 'Y' or 'N'.")

def get_tuesday_discount():
  while True:
    choice = input("Is it Tuesday? (Y/N) ").upper()
    if choice in ["Y", "N"]:
      return choice == "Y"
    else:
      print("Please answer 'Y' or 'N'.")

def get_app_usage():
  while True:
    choice = input("Did the customer use the app? (Y/N) ").upper()
    if choice in ["Y", "N"]:
      return choice == "Y"
    else:
      print("Please answer 'Y' or 'N'.")

def calculate_pizza_cost(pizza_count, tuesday_discount):
  individual_pizza_cost = 12
  pizza_subtotal = pizza_count * individual_pizza_cost
  if tuesday_discount:
    pizza_subtotal = pizza_subtotal * 0.5
  return pizza_subtotal

def calculate_delivery_cost(delivery_needed, pizza_count):
  delivery_charge = 2.50
  if not delivery_needed or pizza_count >= 5:
    return 0
  else:
    return delivery_charge

def apply_app_discount(total_price, app_used):
  if app_used:
    return total_price * 0.75
  else:
    return total_price

def display_final_price(total_price):
  print("Total Price: £{:.2f}".format(total_price))

main()
