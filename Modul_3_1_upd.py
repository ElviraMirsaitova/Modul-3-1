calls = 0
def count_calls():
    global calls
    calls = calls + 1
    return calls
def string_info(name):
    tuple = (len(str(name)), (str(name).upper()), (str(name).lower()))
    count_calls()
    return(tuple)
def in_contains(string, list_to_search):
    a = str(string.lower())
    result = False
    for i in list_to_search:
        if i.lower() in a:
            result = True
            break
        else:
            result = False
    count_calls()
    return result

print(string_info("Suslik"))
print(string_info("krokodil"))
print(string_info("afrika"))
print(in_contains("suSlik", ["derevo", "SusliK", "kust"]))
print(in_contains("suslik", ['tree', 'flower', 'sun']))
print(calls)






