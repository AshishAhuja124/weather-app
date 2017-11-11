import random
f = open("a.json","r")
f = f.read()
f = f.replace("[","")
f = f.replace("]","")

f = f.split("}\n{")

f[0] = f[0].replace("{","")

f[-1] = f[-1].replace("}","")


n = int(raw_input("enter n : "))

s = [i for i in range(0,14)]
random.shuffle(s)

t = []

slen = len(s)
x = slen%n
y = slen/n

for i in range(y):
  t+=[s[i*n:i*n+n]]
t+=[s[y*n:]]


g = open("output2.json","w")
for o in t:
  g.write("[\n")
  for i in o:
    g.write("{")
    g.write(f[i])
    g.write("}\n")
  g.write("\n]\n")

