

def product_of_sums(filename, sum_number):
    differences_dict = dict() #difference:original

    with open(filename, 'r') as file:
        for line in file:
            number = int(line)
            if number in differences_dict.keys():
                return number * differences_dict[number]
            else:
                difference = sum_number - number
                differences_dict[difference] = number

        return None




print(product_of_sums('data.txt', 2020))