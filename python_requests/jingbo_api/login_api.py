# import requests
# url = "http://119.3.25.53:8090/jeeplus/a/login"
# data = {
#     "username": "admin",
#     "password": "juzhen06",
#     "rememberMe": "on"
# }
# headers = {
#     "Content-Type":"application/x-www-form-urlencoded"
# }
# res = requests.post(url=url,data=data)
# print(res.status_code,res.headers,res.text)
# for j in range (1,10):
#     for i in range (1,j+1):
#         print(i*j,end="   ")
#     print(" ")

for i in range(1,10):   #for循环-9*9乘法表
    print("")  #i循环一次换行
    for j in range(1,10):
        if j<=i:
            print(j,"*",i,"=",j*i," ",end="")

for x in range(1,10):
    for y in range(1,x+1):
        print("{}*{}={}  ".format(y,x,x*y),end="")
    print("")


j=1
n=0
while j<10:
    i=1
    while i<=j:
        n=i*j
        print(i,"*",j,'=',n,end="\t")
        i+=1
    j+=1
    print('')