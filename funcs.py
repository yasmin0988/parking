import re
def show_menu_():
    print("1)Add car")
    print("2)Find by plate")
    print("3)Show car list")
    print("0)Exit")
    global option
    option = input("Enter option: ")
    print("-" * 50)
    return option 

car_list = []

def add_car():
    while True:
        name = input("Enter car's name: ")
        if re.match(r"^[a-zA-Z\s]{3,30}$", name):  
            break
        else:
            print("Name is not valid.")

    while True:
        model = input("Enter car's model: ")
        if re.match(r"^[a-zA-Z\s\d]{3,30}$", model):  
            break
        else:
            print("Model is not valid.")

    while True:
        plate = input("Enter car's plate: ")
        if re.match(r"^[\d][\d][a-zA-Z][\d][\d][\d]_iran[\d][\d]$", plate):  
            break
        else:
            print("Plate is not valid.")

    while True:
        color = input("Enter car's color: ")
        if color.lower() in ["white", "black", "red", "blue"]:  
            break
        else:
            print("Color is not valid.")
    car = {
        "name": name,
        "model": model,
        "plate": plate,
        "color": color  
    }
    return car

def find_by_plate():
    while True:
        find_plate = input("Enter car's plate: ")
        if re.match(r"^[\d][\d][a-zA-Z][\d][\d][\d]_iran[\d][\d]$", find_plate):  
            break
        else:
            print("Plate is not valid.")

    founded = []

    for item in car_list:
        if find_plate == item["plate"]:
            founded.append(item) 
        
    return founded

def show_car_list():
    if car_list == []:
        print("No cars in the list.")
    
    print("Car List:")
    print("-" * 50)

    counter = 0
    for car in car_list:
        counter += 1
        print(f"Car{counter}")
        print(f"  Name: {car['name']}")
        print(f"  Model: {car['model']}")
        print(f"  Plate: {car['plate']}")
        print(f"  Color: {car['color']}")
        print("-" * 50)
