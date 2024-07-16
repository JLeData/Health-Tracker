# Base functions
    # [x] Creatable CSV file for data tracking
    # [x] Weight tracking
    # [x] Chart implmentation
 
# Future Implementations
    # Calorie tracking
    # BMI calc
    # water intake tracker?
    # dashboard?

# notes
    # consider using \n to create space for less clutter
    # potential undo and delete functions to avoid digging in csv file
    # other considerations for weight gain/loss like sleep

# Import statements
import sys
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import time
import matplotlib.dates as mdates
import numpy as np

# Enter to continue function to aleviate text clutter
def press_enter():
    input("\nPress Enter to continue...")

# Create loading effect
def loading_effect(duration=3):
    print("\nLoading", end="")
    for _ in range(duration):
        time.sleep(1)
        print(".", end="")
        sys.stdout.flush()
    print("")

# Option select 1
def user_option():
    print("Welcome to the Health Tracker!\n")
    print("1: New user")
    print("2: Returning user")  

    user_status = input("> ")

    while user_status not in ['1', '2']:
        print("\nThat is not a valid input.")
        press_enter()

        print("\nPlease select the options available: ")
        print("1: New user")
        print("2: Returning user")

        user_status = input("> ")

    return user_status

# Disclaimer message
def disclaimer():
    disclaimer_message = (
    "This health tracker is a personal project for practicing programming and promoting a healthier lifestyle.\n" 
    "Feel free to use it, but please note I am not a professional. \n"
    "For professional health advice, consult a healthcare provider.\n" 
    "The accuracy of estimates depends on the data provided by the user,\n" 
    "and I am not liable for any outcomes from using this tool.\n"
    )

    print(disclaimer_message)

# Check for file existence
def file_exists(file_name):
    # Specify the directory path to the desktop on Windows
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    folder_name = 'Your Health Data'
    file_path = os.path.join(desktop_path, folder_name, file_name + ".csv")
    
    # Check if the file exists
    return os.path.isfile(file_path)


# Function to create a new CSV file
def create_csv():
    # Error messages for file existence and blank input
    error_message_exists = "\nError: The file already exists. Please enter a different file name. "
    error_message_blank = "\nError: The file name cannot be blank. Please enter a file name. "
    
    print("\nLet's create your profile. Please enter the name for your file (no .csv extension required): ")

    while True:
        try:
            file_name = input("> ").strip().lower()

            # Check for file existence using the file_exists function
            if file_exists(file_name):
                print(error_message_exists)
            # Check for blank input    
            elif file_name == "":
                print(error_message_blank)
            else:
                # Specify the directory path to the desktop on Windows
                desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
                folder_name = 'Your Health Data'
                folder_path = os.path.join(desktop_path, folder_name)

                # Create the folder if it doesn't exist
                os.makedirs(folder_path, exist_ok=True)

                # Specify the file path inside the folder
                file_path = os.path.join(folder_path, file_name + ".csv")
            
                # Create the CSV file with headers
                headers = ["Date", "time", "Weight", "Target Weight"]
                try:
                    with open(file_path, mode='w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(headers)
                    loading_effect(3)
                    print(f"\n{file_path} has been created with headers: {headers}")
                    return file_name, file_path  # Return file name and path for further use

                except Exception as e:
                    print(f"\nAn error occurred while creating the CSV file: {str(e)}")
                    return None

        except KeyboardInterrupt:
            print("\n\nOperation aborted by user.")
            return None


# Get user's current weight
def initial_weight_entry():
    print("\nLet's get started!\n"
          "Please enter your current weight in lbs: ")

    while True:
        try:
            current_weight = float(input("> "))
            if 50 <= current_weight <= 1000:
                while True:
                    print(f"\nConfirming current weight: {current_weight} lbs")
                    confirmation = input("Is this correct? (y/n): ").strip().lower()

                    while confirmation not in ['y','n']:
                        print("\nInvalid option. Please enter 'y' for yes or 'n' for no.")
                        confirmation = input("> ")

                    if confirmation == 'y':
                        print("\nGreat! Saving your current weight.") 
                        press_enter()
                        return current_weight
                    elif confirmation == 'n':
                        print("\nPlease re-enter your current weight.")
                        break  # Break the confirmation loop to re-enter the weight
                    else:
                        print("\nInvalid option. Please enter 'y' for yes or 'n' for no.")
            else:
                print(f"\nThe value you entered ({current_weight} lbs) seems off. Please try again.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")

# Get user's goal weight
def initial_target_weight():
    print("\nPlease enter your target weight in lbs: ")

    while True:
        try:
            target_weight = float(input("> "))
            while True:
                print(f"\nConfirming target weight: {target_weight} lbs")
                confirmation = input("Is this correct? (y/n): ").strip().lower()

                while confirmation not in ['y','n']:
                    print("\nInvalid option. Please enter 'y' for yes or 'n' for no.")
                    confirmation = input("> ")

                if confirmation == 'y':
                    print("\nAwesome! Saving your target weight.") 
                    press_enter()
                    return target_weight
                elif confirmation == 'n':
                    print("\nPlease re-enter your target weight.")
                    break  # Break the confirmation loop to re-enter the weight
                else:
                    print("\nInvalid option. Please enter 'y' for yes or 'n' for no.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number")
    return target_weight

# Calculate weight difference
def weight_gain_or_loss(current_weight, target_weight):
    print("\nYou have given these values:\n"
          f"Current weight: {current_weight} lbs\n"
          f"Target weight: {target_weight} lbs")
    
    # Adding calcuating time delay for effect
    print("\nCalculating difference\n",end="")
    loading_effect(3)

    if current_weight > target_weight:
        weight_difference = abs(current_weight - target_weight) 
        goal_message = f"\nYour goal is to lose {weight_difference} lbs. You got this!"
    elif current_weight < target_weight:
        weight_difference = abs(current_weight - target_weight)
        goal_message = f"\nYour goal is to gain {weight_difference} lbs. Look's like its time to bulk up!"
    else:
        goal_message = "\nYour goal is to maintain your weight. Keep up the great work!"

    print(goal_message)
    return weight_difference

# Add current and target weight data to file
def initial_weight_update(file_name, file_path, current_weight, target_weight):
    try:
        # Open CSV in append mode
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)

            # Get current date and time
            now = datetime.now()
            date = now.strftime("%m/%d/%Y")
            time = now.strftime("%H-%M-%S")

            # Insert current weight and target weight
            writer.writerow([date, time, current_weight, target_weight])

    except Exception as e:
        print(f"\nAn error occurred while updating the CSV file: {str(e)}")


# Function to open existing file and read its data
def open_file():
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    folder_name = 'Your Health Data'
    
    print("\nWelcome back! Please enter your file name: ")
    file_name = input("> ")
    file_path = os.path.join(desktop_path, folder_name, file_name + ".csv")
    
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
            if len(data) > 1:
                target_weight = data[1][3]  # Read the target weight from the first data row
            else:
                target_weight = None
        return file_name, file_path, target_weight, data  # Retrieve file_name, file_path, target_weight, and data
    except Exception as e:
        print(f"\nThe file name {file_name} is invalid or cannot be opened: {str(e)}")
        return None, None, None, None

# New function to read data from the file
def update_data(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
        return data
    except Exception as e:
        print(f"\nAn error occurred while reading the CSV file: {str(e)}")
        return None
    
# Weight entry
def weight_entry(file_path, target_weight):
    print("\nPlease enter your new weight in lbs.")

    while True:
        try:
            updated_weight = float(input("> "))
            if 50 <= updated_weight <= 1000:
                while True:
                    print(f"\nConfirm new weight: {updated_weight} lbs")
                    confirmation = input("If this correct? (y/n): ").strip().lower()

                    while confirmation not in ['y','n']:
                        print("\nInvalid option. Please enter 'y' for yes or 'n' for no.")
                        confirmation = input("> ").strip().lower()

                        # Open csv to add entriees in append mode
                    if confirmation == 'y':
                        try:    
                            with open(file_path, mode='a', newline='') as file:
                                writer = csv.writer(file)

                                # Get current date and time
                                now = datetime.now()
                                date = now.strftime("%m/%d/%Y")
                                time = now.strftime("%H-%M-%S")

                                # Insert new weight entry
                                writer.writerow([date, time, updated_weight, target_weight])
                                print("\nNew weight entry saved successfully.")
                                press_enter()
                                return updated_weight

                        except Exception as e:
                            print(f"\nAn error occurred while updating the CSV file: {str(e)}")
                            return None

                    elif confirmation == 'n':
                        print("\nPlease re-enter your new weight.")
                        break  # Break the confirmation loop to re-enter the weight
                    else:
                        print("\nInvalid option. Please enter 'y' for yes or 'n' for no.")
            else:
                print(f"\nThe value you entered ({updated_weight} lbs) seems off. Please try again.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")

# Print out last 5 data slots
def print_data(data):
    try:
        if data:
            # Retrieve headers and last 5 data
            headers = data[0] 
            data_rows = data[1:]
            last_five = data_rows[-5:]

            # Select date and weight (ignore target weight and time)
            date_index = headers.index("Date")
            weight_index = headers.index("Weight")

            # Determine column widths
            date_width = max(len(headers[date_index]), max(len(row[date_index]) for row in last_five))
            weight_width = max(len(headers[weight_index]), max(len(row[weight_index]) for row in last_five))

            # Print selected headers with appropriate spacing
            loading_effect(3)
            print(f"\n{headers[date_index]:<{date_width}}   {headers[weight_index]:<{weight_width}}")

            # Print last 5 rows with only "Date" and "Weight" columns
            for row in last_five:
                print(f"{row[date_index]:<{date_width}}   {row[weight_index]:<{weight_width}} lbs")
        
            press_enter()
        else:
            print("\nNo data available.")
    except Exception as e:
        print(f"\nAn error occured while reading the CSV file: {str(e)}")

# Line graph for weight tracking
def plot_weight_graph(file_path):
    try:
        # Load data from CSV into a DataFrame
        df = pd.read_csv(file_path)

        # Convert the 'Date' column to datetime format
        df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

        # Extract dates, weights, and target weight
        dates = df['Date']
        weights = df['Weight']
        target_weight = df['Target Weight'].iloc[-1]  # Get the last target weight as an example
        
        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(dates, weights, marker='o', linestyle='-', color='b', label='Weight')

        # Plot the target weight as a red dashed line
        plt.axhline(y=target_weight, color='r', linestyle='--', label=f'Target Weight ({target_weight})')

        # Formatting the dates on x-axis
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))

        # Set x-axis ticks to include all dates in the data
        plt.xticks(dates, rotation=45)

        # Set y-axis label
        plt.ylabel('Weight (lbs)')

        # Formatting
        plt.xlabel('Date')
        plt.title('Weight Progress')
        plt.legend()

        # Display the plot
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"\nAn error occurred while plotting the graph: {str(e)}")

# First menu
def submenu_1_display():
    print("\nHealth Tracker Menu\n")
    print("1: Enter new weight entry")
    print("2: View weight history")
    print("3: View line graph")
    print("4: Exit")

# First menu functionality
def submenu_1(file_path, target_weight, data):
    while True:
        submenu_1_display()
        choice = input("> ")
        
        if choice == "1":
            updated_weight = weight_entry(file_path, target_weight) # Weight entry function
            if updated_weight is not None:
                data = update_data(file_path)  # Refresh data after new entry
        elif choice == "2":
            print_data(data) # print data
        elif choice == "3":
            plot_weight_graph(file_path) # show line graph
        elif choice == "4":
            print("\nThank you for using the program!")
            press_enter()
            sys.exit()
        else:
            print("\nInvalid choice. Please try again.")

# Main function to call all functions orderly
def main():
    # Pre-variable values
    file_name = None

    disclaimer() # Disclaimer message

    while True:
        user_status = user_option() # User selection

        if user_status == "1":
            file_name, file_path = create_csv() # Retrieve file_name from csv creation
            current_weight = initial_weight_entry() # Retrieve current weight
            target_weight = initial_target_weight() # Retrieve target weight
            weight_difference = weight_gain_or_loss(current_weight, target_weight) # Show weight goal difference
            initial_weight_update(file_name,file_path,current_weight,target_weight) # Update initial weight input
            data = update_data(file_path) # retrieve data from file for option 1
            press_enter()
            submenu_1(file_path, target_weight, data) # Option menu
        elif user_status == "2":
            file_name, file_path, target_weight, data = open_file() # Open file and retrieve data
            loading_effect(3)

            if file_name and data:
                submenu_1(file_path, target_weight, data)  # Enter submenu with target weight
            else:
                sys.exit()
main()
