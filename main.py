############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os
import art_blackjack

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    user_score_21 = False
    print(art_blackjack.logo)
    
    user_card = random.sample(cards,2)
    user_score = sum(user_card)
    print(f"User Card : {user_card} \nUser Score : {user_score}")

    computer_card = random.sample(cards,2)
    computer_score = sum(computer_card)
    print(f"Dealer First Card : {computer_card[0]}")
    
    if user_score == 21:
        print("BlackJack ! User Win")
        print(f"User Card : {user_card} \nUser Score : {user_score} \nDealer Card : {computer_card} \nDealer Score : {computer_score}")
        user_score_21 = True
                
    if computer_score == 21:
        print("BlackJack ! Dealer Win")
        print(f"User Card : {user_card} \nUser Score : {user_score} \nDealer Card : {computer_card} \nDealer Score : {computer_score}")
        user_score_21 = True

    while user_score_21 == False:
        if computer_score < 17:
                new_card = random.choice(cards)
                computer_card.append(new_card)
                computer_score = computer_score + new_card
                if computer_score > 21:
                    user_score_21 = True
            
        if input("Do you want another card ? Type 'yes' or 'no' : ") == 'yes':
            new_card = random.choice(cards)
            user_card.append(new_card)
            user_score =sum(user_card)
            print(f"User Card : {user_card} \nUser Score : {user_score}")
            if user_score == 21:
                print(f"User Card : {user_card} \nUser Score : {user_score} \nDealer Card : {computer_card} \nDealer Score : {computer_score}")
                print("Congratulation, You Win") 
                user_score_21 = True
            if user_score > 21:
                print(f"User Card : {user_card} \nUser Score : {user_score} \nDealer Card : {computer_card} \nDealer Score : {computer_score}")
                user_score_21 = True
                
        else:
            if computer_score < 17:
                new_card = random.choice(cards)
                computer_card.append(new_card)
                computer_score = computer_score + new_card
                if computer_score > 21:
                    user_score_21 = True
                if user_score == 21:
                    print(f"User Card : {user_card} \nUser Score : {user_score} \nDealer Card : {computer_card} \nDealer Score : {computer_score}")
                    print("Better Luck Next Time, Dealer Win") 
                user_score_21 = True
            print(f"User Card : {user_card} \nUser Score : {user_score} \nDealer Card : {computer_card} \nDealer Score : {computer_score}")       
            user_score_21 = True
    
        
    if user_score != 21 and computer_score != 21:
        if user_score > 21:
            print("Better Luck Next Time, Dealer Win")   
        elif computer_score > 21:
            print("Congratulation, You Win")
        elif user_score > computer_score:
            print("Congratulation, You Win")   
        elif user_score < computer_score:
            print("Better Luck Next Time, Dealer Win")
        else:
            print("Its a Draw")
                
            
while input(f"<<<<<< Press any key + Enter to quit >>>>>> \nDo you want to play a game of BlackJack ? Type 'yes' or 'no' : ") == "yes":
    clear_screen()
    blackjack()
    