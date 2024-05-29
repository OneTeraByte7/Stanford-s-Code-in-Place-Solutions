"""Question : It is often the case that we don't want to hardcode and store large amounts of data directly in the code of our programs. 
              Instead, it is more common for us to transport data using files and read the data from the files to then operate on it. 
              This also lets us operate on different files which are structured the same using the same exact code! The starter code 
              already loads a list of numbers from file. You may find it interesting to read over. 
"""

def main():
    number_list = load_numbers_from_file("numbers.txt")
    numbers = []
    with open(r'numbers.txt') as file_reader:
        for line in file_reader:
            fields = line.split()
            rowdata = map(float, fields)
            numbers.extend(rowdata)

    print("Average:",sum(numbers)/len(numbers))
    


def load_numbers_from_file(filepath):
    numbers = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                numbers.append(float(cleaned_line))
    
    return numbers


if __name__ == '__main__':
    main()