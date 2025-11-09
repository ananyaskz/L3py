a=int(input("Enter amount: "))
n1=a//500
n2=(a%500)//100
n3=((a%500)%100)//50
print("500 rupee notes: ",n1)
print("100 rupee notes: ",n2)
print("50 rupee notes: ",n3)