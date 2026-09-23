#!/usr/bin/python3
def find_the_redheads(d:dict):
# 	# return ([name for name, color in d.items() if color == "red"])
	return list(dict(filter(lambda x: x[1] == 'red', d.items())).keys())

# your method definition here
dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))