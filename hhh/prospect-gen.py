#!/bin/python
import random

fielders = input('Skater Count: ')
pitcher = input('Goalie Count: ')

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

while p <= int(skater):
  my_name = random.choice(f_name).rstrip()+" "+random.choice(l_name).rstrip()
  town = random.choice(t_name).rstrip()
  age = 17 + random.randint(1,6)
  
  pck = random.choice(["3","3","3","4","4","4","4","4","4","4","4","4","4","4","4","5","5","5","5","5","5","5","5","5","5","5","5","5","5","5","6","6","6","6","6","6","6","6","6","6","6","6","7"])
  skt = random.choice(["3","3","3","4","4","4","4","4","4","4","4","4","4","4","4","5","5","5","5","5","5","5","5","5","5","5","5","5","5","5","6","6","6","6","6","6","6","6","6","6","6","6","7"])
  chk = random.choice(["3","3","3","4","4","4","4","4","4","4","4","4","4","4","4","5","5","5","5","5","5","5","5","5","5","5","5","5","5","5","6","6","6","6","6","6","6","6","6","6","6","6","7"])

  port = random.choice(["1","2","2","3","3","3"
