import re

def normalize_phone(phone_number):
    numbers_list = re.findall('\d', phone_number)
    clean_number = ''.join(numbers_list[-10:])
    # Add code
    country_code = '+38'
    full_number = country_code + clean_number
    return full_number
    

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
#sanitized_numbers = normalize_phone("+380 44 123 4567")
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
