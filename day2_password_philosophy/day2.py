

def password_requirements(filename):

    valid_password_counter = 0

    with open(filename, 'r') as file:
        for lines in file:
            columns = lines.split()
            number_range = columns[0].split('-')
            letter = columns[1].rstrip(':')
            password = columns[2]
            minimum = int(number_range[0])
            maximum = int(number_range[1])

            if password.count(letter) >= minimum and password.count(letter) <= maximum:
                valid_password_counter += 1 

        return valid_password_counter


print(password_requirements('data.txt'))