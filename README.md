# Parking Manager 

A simple Python command-line application to manage a list of cars. You can add new cars, find them by their license plate, and view the full list.

## Features

- **Add a New Car**: Input details like name, model, license plate, and color with validation.
- **Find Car by Plate**: Search for a specific car using its Iranian license plate number.
- **Show All Cars**: Display the complete list of added cars.

## How to Use

1.  **Clone the repository** to your local machine.
    ```bash
    https://github.com/yasmin0988/parking.git
    ```
2.  **Navigate to the project directory**.
    ```bash
    cd parking
    ```
3.  **Run the main script** to start the program.
    ```bash
    python main.py
    ```

### Using the Application

When you run the program, you will see a menu with these options:

1)Add car
2)Find by plate
3)Show car list
0)Exit

-   Choose `1` to add a new car. You will be prompted to enter the car's details.
-   Choose `2` to find a car by its Iranian license plate (e.g., `12A345_iran67`).
-   Choose `3` to display the entire list of cars.
-   Choose `0` to exit the program.

## License Plate Format

This program validates and expects Iranian license plates in the following format:
**`12A345_iran67`** (Two digits, one letter, three digits, followed by "_iran" and two final digits).

## Technologies Used

-   **Python**
-   Regular Expressions (`re` module) for input validation
