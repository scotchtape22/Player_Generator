#!/bin/python

# Deadball Player Creation for 1909

import random

fielders = input('Player Count: ')
pitcher = input('Pitcher Count: ')

fn_data = open("../Name_Data/firstnames.txt","r")
f_name = fn_data.readlines()
fn_data.close()
for l in f_name:
	l = l.rstrip()

ln_data = open("../Name_Data/lastnames.txt","r")
l_name = ln_data.readlines()
ln_data.close()
for l in l_name:
	l = l.rstrip()

tn_data = open("../Name_Data/townnames.txt","r")
t_name = tn_data.readlines()
tn_data.close()
for t in t_name:
	t = t.rstrip()

p = 0

while p <= int(fielders):
	my_name = random.choice(f_name).rstrip()+" "+random.choice(l_name).rstrip()
	town = random.choice(t_name).rstrip()
	age = 17 + random.randint(1,6)

	bt = random.randint(0,9)+random.randint(0,9)+13
	wt = random.randint(1,6)+random.randint(1,6)+bt
	pd = "-25"

	hand_roll = random.randint(0,9)
	
	position = random.choice(["Infield","Outfield"])

	hand = random.choice(["Switch","Right","Right","Right","Right","Right","Right","Left","Left","Left"])


	perk_roll = random.randint(1,6) + random.randint(1,6)

	if perk_roll == 2:
		perk = "S+,D+"
	elif perk_roll == 3:
		perk = "S+"
	elif perk_roll == 4:
		perk = "D+"
	elif perk_roll == 12:
		perk = "P++"
	elif perk_roll == 10:
		perk = "P+"
	elif perk_roll == 11:
		perk = "C+"
	else:
		perk = "NA"


	print(my_name+";"+str(age)+";"+town+";"+hand+";"+position+";"+str(bt)+";"+str(wt)+";"+pd+";"+perk)
	p = p + 1

p = 0

while p <= int(pitcher):
	my_name = random.choice(f_name).rstrip()+" "+random.choice(l_name).rstrip()
	town = random.choice(t_name).rstrip()
	age = 17 + random.randint(1,6)

	bt = random.randint(0,9)+10
	wt = random.randint(1,6)+bt

	position = "Pitcher"
				      
	pd = random.choice(["d20","d12","d8","d6","d6","d4","0","-d4"])

	hand = random.choice(["Left","Right","Right","Right","Right","Right","Right","Left","Left","Left"])


	perk_roll = random.randint(1,6) + random.randint(1,6)

	if perk_roll == 2:
		perk = "GB+,"
	elif perk_roll == 3:
		perk = "K+,"
	elif perk_roll > 3 and perk_roll < 11:
		perk = ""
	elif perk_roll == 11:
		perk = "ST+,"
	else:
		perk = "CN+,"

	perk = perk+"P-"


	print(my_name+";"+str(age)+";"+town+";"+hand+";"+position+";"+str(bt)+";"+str(wt)+";"+pd+";"+perk)
	p = p + 1
