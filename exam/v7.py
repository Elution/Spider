with open("mrscjb_fmt.txt",'r',encoding="utf-8") as f:
    x = 0
    for i in f.readlines():
        x += 1
        print("table.insert (ar,\""+ i.rstrip("\n") +"\")")
    print(x)