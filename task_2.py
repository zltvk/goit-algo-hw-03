import random

def get_numbers_ticket(min, max, quantity=1):
    try:
        #Validating parameters
        if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
            return []
        #Generation
        result = sorted(random.sample(range(min, max+1),quantity))
        return result
    except:
        return []
    
a = get_numbers_ticket(1, 100, 3)
print(a)

