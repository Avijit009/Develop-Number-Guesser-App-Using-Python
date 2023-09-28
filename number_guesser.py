import random
low = 1
high = 50

iterate_times = 5



def playGame():
    win = False
    #Taking random number from 1 to 50
    correct_ans = random.randint(low, high)
    # print(correct_ans)

    for i in range (iterate_times):
        guessed_number = int(input("Enter the number you guessed: "))
        # print(i)
        if guessed_number == correct_ans:
            print("You Win!")
            win = True
            break
        
        elif guessed_number < correct_ans:
            print(" Correct answer is greater!")

        elif guessed_number > correct_ans:
            print(" Correct answer is smaller!")
        
        attempts_left = iterate_times - (i + 1)
        print(f"Attempts left: {attempts_left}")

    if not win:
        print("You lose!")

    print("Correct Answer is: ", correct_ans)

def main():
    while True:
        playAgain = int(input("Enter 1 to play and 0 to stop: "))
        if playAgain == 1:
            playGame()
        elif playAgain == 0:
            break
        else:
            print("Invalid input. Please enter 1 to play or 0 to stop.")

if __name__ == "__main__":
    main()
