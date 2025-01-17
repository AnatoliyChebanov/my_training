
calls = 0
def count_calls():
    global calls

def string_info(a):
    print (len(a), a.upper(), a.lower())

def is_contains(string, list_to_search):
    if 'water' in string:
        print (True)
    else:
        print (False)

string_info(University)
calls += 1
string_info('Эверест')
calls += 1
is_contains('smoky', ['pensil', 'bacikl'])
calls += 1
is_contains('water', ['dream', 'book'])
calls += 1
print (calls)
