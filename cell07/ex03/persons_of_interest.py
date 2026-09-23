#!/usr/bin/python3
# your method definition here

def	famous_births(d:dict):
	new_dict = dict(sorted(d.items(), key=lambda item: item[1]["date_of_birth"]))
	for k,v in new_dict.items():
		print(f"{v['name']} is a great scientist born in {int(v['date_of_birth'])}.")

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

# women_scientists = {
# "ada": 1,
# "cecilia": 3,
# "lise": 5,
# "grace": 2
# }

famous_births(women_scientists)