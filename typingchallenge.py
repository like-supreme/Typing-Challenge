import time 
import random
from words import word_list as wordlist
def user_time_calculation():
    word = random.choice(wordlist)
    print(f"Your word is: {word}")    
    start_time = time.time()
    user_inp = input()
    end_time = time.time()
    total_time_used = end_time - start_time
    if user_inp == word:  
        print(f"Your elapsed time: {total_time_used}")
        return total_time_used
    else:
        print("Your input does not match")
        return None
game_is_on = True
while game_is_on:
    total_time_used = user_time_calculation()
    if total_time_used <= 5:
        print("congrats")
        wanna_cont = input("do you want to play next round ? y/n...")
        if wanna_cont == "y":
            time.sleep(3)
            user_time_calculation()
        elif wanna_cont == "n":
            break
        else: 
            print("Invalid output. Please try again.")
            break
    elif total_time_used > 5:
        print("You failed try again.")
        break

        