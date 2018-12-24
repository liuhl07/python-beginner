cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New Work'
cities['OR'] = 'Portland'


def find_city(themap,state):
    if state in themap:
        return themap[state]
    else:
        return 'Not Found.'
        
        
cities['_find'] = find_city

while True:        
    print "State?(Enter to quit)",   ##逗号将换行改为空格
    state = raw_input("> ")          #raw_input直接读取控制台输入，将任何类型输入作为字符串，
                                     #input格式希望读取合法python表达式，输入字符串时需用引号，输入123type为int
    if not state: break
    
    city_found = cities['_find'](cities, state)
    print(city_found)        
