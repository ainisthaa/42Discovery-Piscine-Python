#!/usr/bin/python3
# your method definition here

def array_of_names(d:dict): 
	return (list(f.capitalize() + ' ' + l.capitalize() for f,l in d.items()))

persons = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier"
}
print(array_of_names(persons))