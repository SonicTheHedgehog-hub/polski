import json,glob,sys
packs=[];seen={};bad=0
for f in sorted(glob.glob("vocab/*.tsv")):
    cur=None
    for n,line in enumerate(open(f,encoding="utf-8"),1):
        line=line.rstrip("\n")
        if not line.strip(): continue
        c=line.split("\t")
        if c[0]=="#pack":
            cur={"id":c[1],"level":c[2],"title":c[3],"words":[]};packs.append(cur);continue
        c=(c+[""]*7)[:7] if 4<=len(c)<=7 else c
        if len(c)!=7: print(f,n,len(c),line[:60]);bad+=1;continue
        if c[0] in seen: print("DUP",c[0],seen[c[0]],cur["id"])
        seen[c[0]]=cur["id"]
        cur["words"].append(c)
for p in packs:
    if len(p["words"])!=25: print("count",p["id"],len(p["words"]))
json.dump({"packs":packs},open("vocab.json","w",encoding="utf-8"),ensure_ascii=False,separators=(",",":"))
print(len(packs),sum(len(p["words"]) for p in packs),"bad",bad)
