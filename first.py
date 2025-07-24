"""write a python program which will keep adding  a stream of numbers inputted by the user  .the adding stops as soon as
 user presses q key on the on the key board """

sum=0
li=[]
while(True):
    print("take usre input for price of itrm")
    user_input=input("enter number:")

    if user_input.replace('.', '', 1).isdigit() or (user_input.startswith('-') and user_input[1:].replace('.', '', 1).isdigit()):
        li.append(user_input)
        sum=sum+float(user_input)
    elif user_input=="q":
        print("you exit from loop")
        break
    else:
        print("invalid number")

print(sum)

print(li)
for i in range(len(li)):
    print(f"{i} : {li[i]}")
