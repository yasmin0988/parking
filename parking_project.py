from parking.parking_funcs import *

while True:
    
    option = show_menu_()
    match option:
        case "1":
            new_car = add_car()
            car_list.append(new_car)
            print(f"Car has been added sucessfully.\n{new_car}")

        case "2":
            founded = find_by_plate()
            if founded:
                def print_car(car):
                    print(car)
                list(map(print_car, founded))
                
            #     print("Found car(s): ")
            #     for car in founded:
            #         print(car)
            
            else:
                print("No cars were found.")

        case "3":
            show_car_list()

        case "0":
            break

        case _:
            print("Option is not valid.")
