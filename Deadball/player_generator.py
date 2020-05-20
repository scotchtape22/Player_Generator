#!/bin/python

# Deadball Player Creation

import random

fielders = input('Player Count: ')
pitcher = input('Pitcher Count: ')

fn_data = open("firstnames.txt","r")
f_name = fn_data.readlines()
fn_data.close()
for l in f_name:
	l = l.rstrip()

ln_data = open("lastnames.txt","r")
l_name = ln_data.readlines()
ln_data.close()
for l in l_name:
	l = l.rstrip()

tn_data = open("townnames.txt","r")
t_name = tn_data.readlines()
tn_data.close()
for t in t_name:
	t = t.rstrip()

p = 0

while p <= fielders:
	pf_name = random.choice(f_name)
	pl_name = random.choice(l_name)
	town = random.choice(t_name)
	age = 20 + random.int(1,6)

	bt = random.int(0,9)+random.int(0,9)+15
	wt = random.int(1,6)+random.int(1,6)+bt
	era = "NA"

	hand_roll = random.int(0,9)
	
	position_pref = random.choice(["Infield","Outfield"]

	if hand_roll == 0:
		hand = "switch"
	else if hand_roll > 0 and hand_roll < 7
		hand = "right"
	else:
		hand = "left "

	perk_roll = random.int(1,6) + random.int(1,6)

	if perk_roll == 2:
		perk = "S+,D+"
	else if perk_roll == 3:
		perk = "S+"
	else if perk_roll == 4:
		perk = "S+"
	else if perk_roll < 4 and perk_roll > 10:
		perk = ""
	else if perk_roll == 10:
		perk = "P+"
	else if perk_roll == 11:
		perk = "C+"
	else:
		perk = "P++"


	print(pf_name+";"+pl_name+";"+town+";"+hand+";"+position_pref+";"+bt+";"+wt+";"+era+";"+perk)
	p = p + 1

p = 0

while p <= pitcher:
	pf_name = random.choice(f_name)
	pl_name = random.choice(l_name)
	town = random.choice(t_name)
	age = 20 + random.int(1,6)

	bt = random.int(0,9)+5
	wt = random.int(1,6)+bt

	position_pref = random.choice(["Starter","Reliever"]
				      
	era_roll = random.int(1,8)
	if era_roll == 1:
		era = "d12"
	else if era_roll == 2 or era_roll == 3:
		era = "d8"
	else if era_roll == 4 or era_roll == 5 or era_roll == 6:
		era = "d4"
	else:
		era = "-d4"

	hand_roll = random.int(0,9)
	if hand_roll == 0:
		hand = "left"
	else if hand_roll > 0 and hand_roll < 7
		hand = "right"
	else:
		hand = "left "

	perk_roll = random.int(1,6) + random.int(1,6)

	if perk_roll == 2:
		perk = "GB+"
	else if perk_roll == 3:
		perk = "K+"
	else if perk_roll < 3 and perk_roll > 11:
		perk = ""
	else if perk_roll == 11:
		perk = "ST+"
	else:
		perk = "CN+"

	perk = perk+",P-"


	print(pf_name+";"+pl_name+";"+town+";"+hand+";"+position_pref+";"+bt+";"+wt+";"+era+";"+perk)
	p = p + 1
