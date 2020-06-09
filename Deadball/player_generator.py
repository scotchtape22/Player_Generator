#!/bin/python

# Deadball Player Creation

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

	bt = random.randint(0,9)+random.randint(0,9)+15
	wt = random.randint(1,6)+random.randint(1,6)+bt
	era = "-25"

	hand_roll = random.randint(0,9)
	
	position_pref = random.choice(["Infield","Outfield"])

	if hand_roll == 0:
		hand = "switch"
	elif hand_roll > 0 and hand_roll < 7:
		hand = "right"
	else:
		hand = "left"

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


	print(my_name+";"+str(age)+";"+town+";"+hand+";"+position_pref+";"+str(bt)+";"+str(wt)+";"+era+";"+perk)
	p = p + 1

p = 0

while p <= int(pitcher):
	my_name = random.choice(f_name).rstrip()+" "+random.choice(l_name).rstrip()
	town = random.choice(t_name).rstrip()
	age = 17 + random.randint(1,6)

	bt = random.randint(0,9)+5
	wt = random.randint(1,6)+bt

	position_pref = random.choice(["Starter","Reliever"])
				      
	era_roll = random.randint(1,8)
	if era_roll == 1:
		era = "d12"
	elif era_roll == 2 or era_roll == 3:
		era = "d8"
	elif era_roll == 4 or era_roll == 5 or era_roll == 6:
		era = "d4"
	else:
		era = "-d4"

	hand_roll = random.randint(0,9)
	if hand_roll == 0:
		hand = "left"
	elif hand_roll > 0 and hand_roll < 7:
		hand = "right"
	else:
		hand = "left"

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


	print(my_name+";"+str(age)+";"+town+";"+hand+";"+position_pref+";"+str(bt)+";"+str(wt)+";"+era+";"+perk)
	p = p + 1
