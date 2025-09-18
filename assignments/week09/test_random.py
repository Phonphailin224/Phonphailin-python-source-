mport random
 
test_random = random.radaint(0,9)
 
guess_random = int(input("What is your guess number? : "))
 
if test_random == guess_number:
    print("ยูเก่งมากกก")
 
elif guess_number < test_random:
    print("อาาจจะยังน้าา")
 
elif guess_number > test_random:
    print("ผิดจ้า มากไปหน่อย")
