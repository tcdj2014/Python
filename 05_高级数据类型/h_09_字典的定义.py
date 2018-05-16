xiaoming = {
    "name": "小明",
    "性别": "男"
}
zhansan= {
    "name": "张三",
    "性别": "男"
}
xiaoming["年龄"]=20
xiaoming["性别"]="女"
print(xiaoming)

for k in xiaoming:
    print(k,xiaoming[k])

person=[
    xiaoming,
    zhansan
]

for p in person:
    print(p)