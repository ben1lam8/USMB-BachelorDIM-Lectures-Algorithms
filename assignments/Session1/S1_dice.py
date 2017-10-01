## @namespace S1_dice
# A dice game simulation
# 
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import random;


# Global variables
player_score = 0;
computer_score = 0;
turn_count = 0;


## Game main logic
#
def main():
    
    #Init the game
    print("========================================================================");
    print("===            Yay! Welcome to the Incredible Dice Game !            ===");
    print("========================================================================\n");
    
    print("Rules are easy :");
    print("-    You play against the computer");
    print("-    You can throw the dice as many times as you want");
    print("-    Each time, the dice value will be added to your turn score");
    print("-    If the dice shows a 1, your turn ends and you lose your turn score");
    print("-    Reach 100 points to win ! GOOD LUCK\n");
    
    #Iterate trough turns until someone wins
    while(player_score < 100 and computer_score < 100):
        
        #Init the turn
        global turn_count;
        turn_count += 1;
        
        print("---------------------------------------------");
        print("                 ROUND {t} !                 ".format(t=turn_count));
        print("Player : {p} pts |  vs  | Computer : {c} pts\n".format(p=player_score, c=computer_score))
        print("---------------------------------------------");
        
        #Switch between turns
        if turn_count%2 == 1:
            player_turn();
        else:
            computer_turn();
            
        #Quit if someone wins
        if player_score >= 100 :
            print("YOU WIN !");
            print("Congratulations !");
            break;
        elif computer_score >= 100 :
            print("COMPUTER WINS");
            print("Sorry. Come back soon... and retry ;)");
            break;
    
    #That' all, Folks !
    print("End of the game !");
    print("Final scores : ");
    print("Player : {p} pts |  vs  | Computer : {c} pts\n".format(p=player_score, c=computer_score))
    print("Goodbye !");
    
## Handles a player round
#
def player_turn():
    print("PLAYER TURN !");
    print("-------------");
    
    turn_score = 0;
    keep_playing=True;
    
    raw_input("Press ENTER to throw the dice...");
    while keep_playing:
        
        dice = random.randint(1, 6);
        
        if dice==1: 
            print("Too Bad... it's a 1");
            turn_score=0;
            break;
        else:
            print("Got a {d}".format(d=dice));
            turn_score += dice;
            
            print("Your turn-score is {ts} pts".format(ts=turn_score));
            
            while True:
                key = raw_input("Keep playing ? y/n (a 1 will make you lose the turn...");
                if key == 'y':
                    break;
                elif key == 'n':
                    keep_playing = False;
                    break;
                else :
                    print("I don't understand your answer... ");
            
    raw_input("You won {p} points (press enter to continue)\n".format(p=turn_score));
    global player_score;
    player_score += turn_score;
    
## Handles a computer round
#
def computer_turn():
    print("COMPUTER TURN !");
    print("---------------");
    
    turn_score = 0;
    keep_playing=True;
    
    while keep_playing:
        print("Throwing the dice...");
        
        dice = random.randint(1, 6);
        
        if dice==1: 
            print("Too Bad... it's a 1");
            turn_score=0;
            break;
        else:
            print("Got a {d}".format(d=dice));
            turn_score += dice;
            
            print("Keep playing ? y/n (a 1 will make you lose the turn...")
            key = random.choice(['y', 'y', 'y', 'y', 'y', 'n',]);
            print("{k}".format(k=key));
            if key == 'y':
                continue;
            elif key == 'n':
                keep_playing = False;
                break;

    raw_input("Computer won {p} points (press enter to continue)\n".format(p=turn_score));
    global computer_score;
    computer_score += turn_score;

#Launch the game !
main();
    