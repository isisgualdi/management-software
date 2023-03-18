import os

cars = [["Chevrolet Tracker", 120],
          ["Chevrolet Onix", 90],
          ["Chevrolet Spin", 150],
          ["Hyndai HB20", 85],
          ["Hyundai Tucson", 120],
          ["Fiat Uno", 60],
          ["Fiat Mobi", 70],
          ["Fiat Pulse", 130]]
rented_cars = []

def show_cars_list(cars_list):
  for i, car in enumerate(cars_list):
    print("[{}] {} - ${} /day".format(i, car[0], car[1]))

show_cars_list(cars)

while True:
  os.system("cls")
  print("=========================")
  print("Welcome to the car store!")
  print("=========================")
  print("")
  print("Select an option:")
  print("0 - Show cars / 1 - Rent a car / 2 - Return a car")
  op = int(input())

  os.system("cls")
  if op == 0:
    show_cars_list(cars)

  elif op == 1:
    show_cars_list(cars)
    print("")
    print("Choose the car code:")
    code_car = int(input())
    print("")
    print("For how many days do you want to rent this car?")
    days = int(input())
    os.system("cls")

    print("You chose {} for {} days.".format(cars[code_car][0], days))
    print("")
    print("It will cost ${}. Follow up with payment?".format(days* cars[code_car][1]))
    
    print("0 - YES / 1 - NO")
    conf = int(input())
    if conf == 0:
      print("")
      print("You rentend {} for {} days.".format(cars[code_car][0], days))
      rented_cars.append(cars.pop(code_car))

  elif op == 2:
    if len(rented_cars) == 0:
      print("No cars to return.")
    else:
      print("List of rented cars.")
      show_cars_list(rented_cars)
      print("")
      print("Choose the code of the car you want to return:")
      cod = int(input())
      if conf == 0:
        print("")
        print("You returned {}".format(rented_cars[cod][0]))
        cars.append(rented_cars.pop(cod))

  print("")
  print("==========")
  print("0 - CONTINUE / 1 - EXIT")
  if float(input()) == 1:
    break