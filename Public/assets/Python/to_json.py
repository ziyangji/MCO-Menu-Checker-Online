import json


def to_json(names, cals):
    if len(names) != len(cals):
        raise RuntimeError(f'{len(names)}, {len(cals)}')

    menu = dict()
    for i in range(len(names)):
        menu[names[i]] = cals[i]
    return json.dumps(menu)


if __name__ == '__main__':
	with open('test_json.json', 'w', encoding="utf-8") as js:
		js.write(to_json())
