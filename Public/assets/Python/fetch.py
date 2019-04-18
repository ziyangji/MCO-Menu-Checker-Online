from data_fetch import fetch_all
import json


def to_json(place, lst):
	temp_dict = dict()
	temp_dict[place] = lst
	return json.dumps(temp_dict)


def to_list(name, vals):
	lst = list()
	for k, v in vals.items():
		item = dict()
		item['name'] = k.strip().capitalize()
		item['meal'] = name.upper()
		item['cal'] = v.replace('cal', '')
		lst.append(item)
	return lst


def process_dict(data, place):
	vals = to_list('BREAKFAST', data[0])
	vals.extend(to_list('LUNCH', data[1]))
	vals.extend(to_list('DINNER', data[2]))
	return to_json(place, vals)


def run():
	cms = fetch_all('cms')
	sage = fetch_all('sage')
	barh = fetch_all('barh')

	with open('../data/data_cms.json', 'w', encoding='utf-8') as cms_json:
		cms_json.write(process_dict(cms, 'cms'))

	with open('../data/data_sage.json', 'w', encoding='utf-8') as sage_json:
		sage_json.write(process_dict(sage, 'sage'))

	with open('../data/data_barh.json', 'w', encoding='utf-8') as barh_json:
		barh_json.write(process_dict(barh, 'barh'))


if __name__ == '__main__':
	run()
