#!/bin/python

#AAHGH Player Generator

import random


def roll_2d4():
	return random.randint(1,4)+random.randint(1,4)

players = input('Player Count: ')

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

region = ["New England","Appalachia","Dixie","Foundry","Breadbasket","Rocky Mountains","Cascadia","California","Texas","Hawaii"]
p = 0

while p <= int(players):
	name = random.choice(f_name).rstrip()+" "+random.choice(l_name).rstrip()
	region = random.choice(region)
	age = str(20 + random.randint(1,6))

	# Personality
	person_roll = random.randint(1,6)

	if person_roll == 1:
		person = "ruthless"
	elif person_roll == 2:
		person = "determined"
	elif person_roll == 3:
		person = "knowledgable"
	elif person_roll == 4:
		person = "lovable"
	else:
		person = "no personality"

	# Skills

	# Passing
	pa_roll = roll_2d4()
	if pa_roll == 2 or pa_roll == 8:
		pa = 3
	elif pa_roll == 3 or pa_roll == 7:
		pa = 2
	else:
		pa = 1
	if region == "New England" or region == "Texas":
		pa = pa +1
	pa = str(pa)

	# Catching
	ct_roll = roll_2d4()
	if ct_roll == 7 or ct_roll == 8:
		ct = 3
	elif ct_roll == 5 or ct_roll == 6:
		ct = 2
	else:
		ct = 1
	if region == "Appalachia" or region == "Cascadia":
		ct = ct +1
	ct = str(ct)

	# Running
	rn_roll = roll_2d4()
	if rn_roll == 5:
		rn = 3
	elif rn_roll == 4 or rn_roll == 6:
		rn = 2
	else:
		rn = 1
	if region == "Rocky Mountains" or region == "Dixie":
		rn = rn +1
	rn = str(rn)

	# Blocking
	bk_roll = roll_2d4()
	if bk_roll == 2 or bk_roll == 8:
		bk = 3
	elif bk_roll == 5:
		bk = 2
	else:
		bk = 1
	if region == "Breadbasket" or region == "California":
		bk = bk +1
	bk = str(bk)

	# Tackling
	tk_roll = roll_2d4()
	if tk_roll == 2 or tk_roll == 8:
		tk = 3
	elif tk_roll == 5:
		tk = 2
	else:
		tk = 1
	if region == "Foundry" or region == "Hawaii":
		tk = pa +1
	tk = str(tk)

	# Punting
	pn_roll = roll_2d4()
	if pn_roll == 8:
		pn = "3"
	elif pn_roll == 2:
		pn = "2"
	else:
		pn = "1"

	# Endurance
	en_roll = roll_2d4()
	if en_roll == 5:
		en = "3"
	elif en_roll == 2 and en_roll == 8:
		en = "2"
	else:
		en = "1"


	# Focus
	fc_roll = roll_2d4()
	if fc_roll == 5:
		fc = "3"
	elif fc_roll == 2 and fc_roll == 8:
		fc = "2"
	else:
		fc = "1"

	# Output String
	print(name+";"+age+";"+region+";"+person+";"+pa+";"+ct+";"+rn+";"+bk+";"+tk+";"+pn+";"+en+";"+fc)
	p = p + 1

