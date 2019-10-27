import requests

properties = [{"name": "janka hardness", "unit": "N"},
			  {"name": "density", "unit": "kg/m"},
			  {"name": "modulus of rupture", "unit:": "MPa"},
			  {"name": "elastic modulus", "unit":"GPa"},
			  {"name": "crushing strength", "unit":"MPa"}]



def extract_property(data, property):
	#Inputs: Data is a string; the entirety of the HTML. Property is a dictionary with name and a unit
	#Outputs: A dictionary consisting of {name, property}, with property being a numerical value
	#Date: October 26, 2019
	#index-of-property is data.index(property[name])
	property_pos = data.index(property[name])
	unit_pos = property_pos + data[property_pos:].index(property[unit])
	return {property[name] : float(data[property_pos:unit_pos].strip().split(" ")[-1][1:].replace(",", ""))}

def get_properties(data, name):
	#Input: Data
	#Output: A dictionary of the entire wood
	output = {"name": name}
	