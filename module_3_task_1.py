calls = 0
def count_calls():
    global calls
    calls+=1
def string_info():
    a = input()
    tuple_a = (len(a), a.upper(), a.lower())
    print(tuple_a)
    count_calls()
    return(tuple_a)
def is_contains():
    string = input().strip()
    list_to_search = input().strip().split(',')
    list_to_search = [item.strip().lower() for item in list_to_search]
    string = string.lower()
    count_calls()
    return string in list_to_search


string_info()
resultat = is_contains()
print(resultat)
print(calls)