count = 0
score = 0
import random
while count < 3:
    count += 1
    my_num = random.randint(1,100)
    comp_num = random.randint(1,100)
    print('your number is:',my_num)
    guess = input("guess weather your num is higher or lower then that of computer's num:")
    print('computer number is:',comp_num)
    if guess == 'higher' and my_num > comp_num:
        print('you are right!')
        score += 1
        print('your score is:',score)
    elif guess == 'lower' and my_num < comp_num:
       print('you are right!')
       score += 1
       print('your score is:',score)
    else:
        print('you are wrong')
        print('your score is',score)
print('Thanks for playing')
print('Good job! you played very well')