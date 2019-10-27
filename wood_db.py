import requests
import sys

properties = [{"name": "Janka", "unit": "N"},
			  {"name": "Average Dried Weight", "unit": "kg/m"},
			  {"name": "Modulus of Rupture", "unit": "MPa"},
			  {"name": "Elastic Modulus", "unit": "GPa"},
			  {"name": "Crushing Strength", "unit": "MPa"}]


def extract_property(data, property):
	#Inputs: Data is a string; the entirety of the HTML. Property is a dictionary with name and a unit
	#Outputs: The value of the property
	#Date: October 26, 2019
	#index-of-property is data.index(property[name])
	property_pos = data.index(property["name"])
	unit_pos = property_pos + data[property_pos:].index(property["unit"])
	return float(data[property_pos:unit_pos].strip().split(" ")[-1][1:].replace(",", ""))

def get_properties(data, name):
	#Input: Data
	#Output: A dictionary of the entire wood
	output = {"name": name}
	for i in properties:
		output[i["name"]] = extract_property(data, i)
	return output


def link_to_wood_dict(link):
	#Input: A link, a string
	#Output: A dictionary of the wood and save to file
	return get_properties(requests.get(link).text, link.split("/")[-2])

def save_to_file(wood):
	#Input: None
	#Output: None
	#opens a file called wooddb.csv, writes each wood to it
	#Check for existence
	wood_file = open('wooddb.csv', mode='r') 
	if wood_file.read().find(wood["name"]) != -1:
		print(wood["name"] + " already exists in the database!")
		return None
	wood_file.close()			

	with open('wooddb.csv', mode='a') as wood_file:
		for i in wood.keys():
			wood_file.write(str(wood[i]) + ",")
		wood_file.write("\n")
	print("Successfully added " + wood["name"] + " to the database!")

def list_woods():
	#Input: None
	#Output: A list of the woods in the database
	wood_list = []
	with open('wooddb.csv', mode = 'a') as wood_file:
		for line in enumerate(wood_file):
			wood_list.append(line[1].split(","))
	return wood_list

def compare_woods(wood_list):
	#Input: A list of woods to compare
	#Output: None
	db_woods = list_woods()
	output = []
	for i in wood_list:
		if i in db_woods

	return None

def main():
	#Run forever
	while True:
		print("Your options are as follows:")
		print("1. Add a wood to the database")
		print("2. Compare woods")
		print("3. Exit")
		choice = input("> ")
		if (choice == "1"):
			print("Please enter the link at the prompt below")
			link = input("> ")
			try:
				save_to_file(link_to_wood_dict(link))
			except Exception:
				print("An exception occured, so you probably entered an invalid link. Please try again.\n")
		elif (choice == "3"):
			print("Goodbye!")
			sys.exit()
		else:
			None

