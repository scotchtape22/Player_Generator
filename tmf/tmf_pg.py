#!/bin/python

# 10 Minute Football Player Creation

import random

p_count = input('Player Count: ')

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

# Stat Arrays
# Balanced (Block, Run, Tackle, Catch)
bal_array = ["1","2","2","2","2","2","3","3","3","3","3","3","3","3","3","4","4","4","4","4","4","4","4","4","4","4","5","5","5","5","5","5","5","5","5","6"]
# Specialist
spe_array = ["1","1","1","1","1","1","2","2","2","2","2","2","2","2","2","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","6","6","6","7","7","8"]
# Life
lif_array = ["1","2","2","3","3","3","4","4","4","4","5","5","5","5","5","5","5","5","5","5","5","6","6","6","6","6","7","7","7","7","8","8","8","9","9","10"]

while p <= int(p_count):
	# Regular Info
	my_name = random.choice(f_name).rstrip()+" "+random.choice(l_name).rstrip()
	town = random.choice(t_name).rstrip()
	age = 17 + random.randint(1,6)


	blk = random.choice(bal_array)
	run = random.choice(bal_array)
	tkl = random.choice(bal_array)
	cth = random.choice(bal_array)

	pas = random.choice(spe_array)
	kic = random.choice(spe_array)

	pot = random.choice(lif_array)
	sta = random.choice(lif_array)

	print(my_name+":"+blk+":"+run+":"+tkl+":"+cth+":"+pas+":"+kic+":"+pot+":"+sta+":"+town+":"+str(age))

	# Iterate
	p = p + 1
