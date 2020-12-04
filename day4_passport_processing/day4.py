import re

def valid_passport(filename):

	minimum_requirements = 7
	passport_check = dict()
	valid = 0 

	with open(filename, 'r') as file:

		for line in file:
			if line == "\n":
				if len(passport_check) < 7:
					passport_check.clear()
					continue
				elif len(passport_check) == 7 and passport_check.get('cid'):
					passport_check.clear()
					continue
				else:
					if extra_requirements(passport_check):
						valid += 1

					passport_check.clear()
			else:
				pairs = line.split()
				for item in pairs:
					key, value = item.split(':')
					passport_check[key] = value
		if len(passport_check) < 7:
			passport_check.clear()
		elif len(passport_check) == 7 and passport_check.get('cid'):
			passport_check.clear()
		else:
			if extra_requirements(passport_check):
				valid += 1 
				passport_check.clear()
		return valid


def extra_requirements(passport_dict):
	min_byr, max_byr = 1920, 2002
	min_iyr, max_iyr = 2010, 2020
	min_eyr, max_eyr = 2020, 2030
	min_cm, max_cm = 150, 193
	min_in, max_in = 59, 76
	hcl_pattern = re.compile('#([0-9]|[a-f]){6}')
	eye_pattern = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
	passport_pattern = re.compile('\d{9}(?!\S)')
	default_check = False


	for key, value in passport_dict.items():
		if key == 'byr':
			if int(value) >= min_byr and int(value) <= max_byr and len(value) == 4:
				default_check = True
			else:
				return False
		elif key == 'iyr':
			if int(value) >= min_iyr and int(value) <= max_iyr and len(value) == 4:
				default_check = True
			else:
				return False
		elif key == 'eyr':
			if int(value) >= min_eyr and int(value) <= max_eyr  and len(value) == 4:
				default_check = True
			else:
				return False
		elif key == 'hgt':
			if value[-2:] == 'cm':
				if int(value[:-2]) >= min_cm and int(value[:-2]) <= max_cm:
					default_check = True
				else:
					return False
			elif value[-2:] == 'in':
				if int(value[:-2]) >= min_in and int(value[:-2]) <= max_in:
					default_check = True
				else:
					return False
			else:
				return False
		elif key =='hcl':
			if re.match(hcl_pattern, value):
				default_check = True
			else:
				return False
		elif key == 'ecl':
			if value in eye_pattern:
				default_check = True
			else:
				return False
		elif key == 'pid':
			if re.match(passport_pattern, value):
				default_check = True
			else:
				return False

	return default_check



#148

print(valid_passport('data.txt'))
print(valid_passport('valid_pass.txt'))
print(valid_passport('invalid_pass.txt'))