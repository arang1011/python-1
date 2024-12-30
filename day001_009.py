print("단수를 입력하세요")
a=int(input())
print("입력한 숫자는:"+str(a)+"입니다.")
for i in range(1,10):
    b=a*i
    print(str(a)+"X"+str(i)+" = " + str(b))