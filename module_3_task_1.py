calls = 0
def count_calls():
    global calls
    calls+=1

def string_info(a):
    tuple_a = (len(a), a.upper(), a.lower())
    print(tuple_a)
    count_calls()
    return(tuple_a)

def is_contains(string, list_to_search):
    list_to_search = [item.strip().lower() for item in list_to_search]
    string = string.lower()
    count_calls()
    return string in list_to_search


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
