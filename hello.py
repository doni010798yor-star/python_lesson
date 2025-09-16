number=inp("Sonlardan iborat list yozmig")
number=number.replace(" ", ", ",")
number=number.split(",")
number=[int(i) for i in number if i.strip()!=""]
total=0
for i in number:
if i %2==0:
total+=i
print("LIst ichdegi sonlarning yig'indisi", total)
