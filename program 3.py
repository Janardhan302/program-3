word=input("Enter a word:")
number={'0','1','2','3','4','5','6','7','8','9'}
d={}
for x in word:
    if x in number:
        d[x]=d.get(x,0)+1
for k,v in sorted(d.items()):
    print(k,"occured",v,"times")
             
