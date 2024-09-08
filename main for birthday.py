# Programmer and userID = Niyam Acharya nka42
# Program date = 11/30/2023
# Description = Reads a file containing a list of birthdays in the format "month/day/year".
#               Utilizes the Birthday class to create Birthday objects from the input file data.
#               Creates a hash table using Birthday objects as keys and displays the count of elements in each hash location.
#               Prompts the user to input the data file name until a valid file is provided.
#               Handles file errors and invalid input formats appropriately.

from birthday import Birthday

def read_birthday_file(file_name):
    birthdays = []
    try:
        with open(file_name) as file:
            for line in file:
                parts = line.strip().split('/')
                if len(parts) == 3:
                    month, day, year = map(int, parts)
                    birthdays.append(Birthday(month, day, year))
                else:
                    print(f"Error in line: {line.strip()} - Invalid format")
    except FileNotFoundError:
        print(f"Error: {file_name} does not exist. Try again.")
    return birthdays

def create_hash_table(birthday_list):
    hash_table = [[] for _ in range(12)]
    for i, bday in enumerate(birthday_list, start=1):
        idx = hash(bday)
        hash_table[idx].append((bday, i))
    return hash_table

def output_hash_table(hash_table):
    print()
    for i, slot in enumerate(hash_table):
        print(f"Hash location {i} has {len(slot)} elements in it.")

def main():
    while True:
        file_name = input("Enter name of the data file: ")
        birthdays = read_birthday_file(file_name)
        if birthdays:
            hash_table = create_hash_table(birthdays)
            output_hash_table(hash_table)
            break

if __name__ == "__main__":
    main()
