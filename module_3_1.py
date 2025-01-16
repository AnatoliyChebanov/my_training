
calls = 0
def count_calls():
    global calls
calls +=1

def string_info():
    a = 'University'
    b = (len(a), a.upper(), a.lower())
    print (b)
calls += 1

def is_contains():
    contains = ('smoke', ['pensil', 'bacikl'])
    if 'water' in contains:
        print (True)
    else:
        print (False)
calls += 1

string_info()
is_contains()
print (calls)