import json


def to_dict(names, cals):
    if len(names) != len(cals):
        raise RuntimeError(f'{len(names)}, {len(cals)}')

    menu = dict()
    for i in range(len(names)):
        menu[names[i]] = cals[i]
    return menu

