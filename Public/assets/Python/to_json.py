
def to_json(names, cals):
    if len(names) != len(cals):
        raise RuntimeError;
    menu = dict()
    for i in range(len(names)):
        menu[names[i]] = cals[i]
    return menu
    
