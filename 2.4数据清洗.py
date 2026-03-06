s=" Agent:007_Bond; Coords:(40,74); Items:gun,money,gun; Mission:2025-RESCUE-X "
#去除首尾空格
s=s.strip()
#分割
s=s.split("; ")
a=s[2].replace(":",",")
#去重装备
a=set(a.split(","))
a.remove("Items")
#将集合转换成列表
s[2]=list(a)

t=s[1]
t=t.strip("Coords:")
t=t.strip("(")
t=t.strip(")")
x,y=t.split(",")
#坐标元组
coords_touple=(int(x),int(y))

#存入字典
Dict={}
Dict[s[0][0:5]]=s[0][6:]
Dict[s[1][0:6]]=coords_touple
Dict["Items"]=s[2]
Dict[s[3][0:7]]=s[3][8:]
print(Dict)