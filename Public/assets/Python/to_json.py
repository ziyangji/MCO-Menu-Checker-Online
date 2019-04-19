import json

# expect "names" to be a list
# expect "cals" to be a list
# expect names have the same length as cals
# If names and cals's length are different, raise exception
#
# Return a dictionary contains {names1, cals1}, {names2, cals2}....
#

def to_dict(names, cals):
    if len(names) != len(cals):
        raise RuntimeError(f'{len(names)}, {len(cals)}')

    menu = dict()
    for i in range(len(names)):
        menu[names[i]] = cals[i]
    return menu


if __name__ == '__main__':
    
    #empty
    names = []
    cals = []
    menu = to_dict(names, cals)
    print(menu)
    
    
    '''
    #should raise runtime exception
    names = ["1"]
    cals = []
    menu = to_dict(names, cals)
    '''
    
    #regular case with one input
    names = ["1"]
    cals = ["1"]
    menu = to_dict(names, cals)
    print(menu)    
    
    #regular case with small number of inputs
    names = ["a", "b", "c", "d", "e"]
    cals = ["1", "2", "3", "4", "5"]
    menu = to_dict(names, cals)
    print(menu)   


