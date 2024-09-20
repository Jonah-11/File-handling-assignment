# file_handling_assignment.py

def create_and_write_file():
    try:
        # Create a new text file and write initial content
        with open("my_file.txt", 'w') as file:
            file.write("Line 1: Trump for president.\n")
            file.write("Line 2: Boeing has the best planes.\n")
            file.write("Line 3: The beast is a cadillac.\n")
        print("File created and written successfully.")
    except Exception as e:
        print(f"An error occurred while creating or writing to the file: {e}")
    finally:
        print("Exiting create_and_write_file function.")

def read_and_display_file():
    try:
        # Read and display the content of the file
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("\nReading file content:")
            print(content)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    finally:
        print("Exiting read_and_display_file function.")

def append_to_file():
    try:
        # Append additional content to the file
        with open("my_file.txt", 'a') as file:
            file.write("Line 4: Kenya airforce one is a fokker 70.\n")
            file.write("Line 5: Airforce has the F-16.\n")
            file.write("Line 6: I am He.\n")
        print("File appended successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")
    finally:
        print("Exiting append_to_file function.")

if __name__ == "__main__":
    create_and_write_file()
    read_and_display_file()
    append_to_file()
    read_and_display_file()  # Read and display again to show the appended content
