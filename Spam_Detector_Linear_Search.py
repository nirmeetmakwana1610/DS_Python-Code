blacklist = ["spam@gmail.com", "fake@yahoo.com", "abc@test.com"]

email = input("Enter Email : ")

flag = 0

for i in range(len(blacklist)):
    if blacklist[i] == email:
        flag = 1
        break

if flag == 1:
    print("Spam Email")
else:
    print("Safe Email")
