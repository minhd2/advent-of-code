
def password_check(filename):

    valid_password_counter = 0

    with open(filename, 'r') as file:
        for lines in file:
            columns = lines.split()
            number_index = columns[0].split('-')
            letter = columns[1].rstrip(':')
            password = columns[2]
            first_index = int(number_index[0]) - 1 
            second_index = int(number_index[1]) - 1 

            if password[first_index] == letter and password[second_index] == letter: 
                continue
            elif password[first_index] == letter or password[second_index] == letter:
                valid_password_counter += 1 

        return valid_password_counter



print(password_check('data.txt'))