import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def draw_single_card():
    c = random.randint(1,13)
    if c ==11:
        c='J'
    elif c==12:
        c='Q'
    elif c==13:
        c='K'
    elif c==1:
        c='A'
    return c

def hit_stand(cards_p1, cards_p2, chance):
    '''
    cards_p1 contains the cards of player 1.
    cards_p2 contains the cards of player 2.
    chance tells us the condition that is being followed by the bot or the user. 
    If the value of chance is 1, indicating that the user has chosen hit(draw_single_card is called and the card is appended  to the existing list of cards) the user has chose to draw another card. 
    So another card piles up in his deck and when the user does not want to draw any more cards he types in 'n'.
    Indicating that he wants to stand. 
    So now, the bot chooses his card.       
    If the user draws an 'A' then the value of the card is either 1 or 11.
    The value of 'JQk' is 10.
    The game continues like this.
    
    At the End, based on the existing conditions, winner will be chosen.
    '''
    p1_total=0
    p2_total=0
    if chance==1:
        print("Player 1 Cards:", cards_p1)
        for i in cards_p1:
            if str(i) in 'JQK':
                i=10
            elif str(i) =='A':
                if len(cards_p1) == 2:
                    if str(cards_p1[0]) == 'A':
                        #cards_p1[0] = 11
                        i=11
                    elif str(cards_p1[0]) != 'A' and str(cards_p1[1]) == 'A':
                        #cards_p1[1] = 11
                        i=11
                    elif str(cards_p1[0]) == 'A' and str(cards_p1[1]) == 'A':
                        #cards_p1[0] = 11
                        i=1
                else:
                    i=1
            p1_total+=i
        print("Player 1 Score is:", p1_total)
        if p1_total == 21:
            print("BlackJack!! You Win!!")
            choice()
        inp2='y'
        while inp2=='y':
            h_s=input("Do You Wish To Hit Or Stand (Y - Hit | N - Stand): ")
            h_s=h_s.lower()
            if h_s=='y':
                c = draw_single_card()
                cards_p1.append(c)
                print(cards_p1)
                p1_total=0
                for i in cards_p1:
                    if str(i) in 'JQK':
                        i=10
                    elif str(i) =='A':
                        if len(cards_p1) == 2:
                            if str(cards_p1[0]) == 'A':
                                #cards_p1[0] = 11
                                i=11
                            elif str(cards_p1[0]) != 'A' and str(cards_p1[1]) == 'A':
                                #cards_p1[1] = 11
                                i=11
                            elif str(cards_p1[0]) == 'A' and str(cards_p1[1]) == 'A':
                                #cards_p1[0] = 11
                                
                                i=1
                        else:
                            i=1
                    p1_total+=i
                if p1_total>21:
                    print("You Went Over! Computer Wins!!")
                    choice()
                chance=1
                hit_stand(cards_p1,cards_p2,chance)
            elif h_s=='n':
                chance=2
                hit_stand(cards_p1,cards_p2,chance)
            else:
                print("Invalid Input")
                inp2=input("Do You Wish To Re-Enter The Option: (Y - Yes | N - No): ")
                inp2=inp2.lower()
    elif chance==2:
        print("Computer's Cards:", cards_p2)
        for i in cards_p2:
            if str(i) in 'JQK':
                i=10
            elif str(i) =='A':
                if len(cards_p2) == 2:
                    if str(cards_p2[0]) == 'A':
                        #cards_p2[0] = 11
                        i=11
                    elif str(cards_p2[0]) != 'A' and str(cards_p2[1]) == 'A':
                        #cards_p2[1] = 11
                        i=11
                    elif str(cards_p2[0]) == 'A' and str(cards_p2[1]) == 'A':
                        #cards_p2[0] = 11
                        i=1
                else:
                    i=1
            p2_total+=i
        print("Computer's Score is:" ,p2_total)
        if p1_total == 21:
            print("BlackJack!! Computer Wins!!")
            choice()
        if p2_total>21:
            print("Computer Went Over! You Win!!")
            choice()
        elif p2_total>16:
            for p in cards_p1:
                if str(p) in 'JQK':
                    p=10
                elif str(p) =='A':
                    if len(cards_p1) == 2:
                        if str(cards_p1[0]) == 'A':
                            #cards_p1[0] = 11
                            p=11
                        elif str(cards_p1[0]) != 'A' and str(cards_p1[1]) == 'A':
                            #cards_p1[1] = 11
                            p=11
                        elif str(cards_p1[0]) == 'A' and str(cards_p1[1]) == 'A':
                            #cards_p1[0] = 11
                            p=1
                    else:
                        p=1
                p1_total+=p
            if p1_total>p2_total:
                print("You Win!!")
                choice()
            elif p1_total==p2_total:
                print("It's A Draw!!")
                choice()
            elif p1_total<p2_total:
                print("Computer Wins!!")
                choice()
            
        elif p2_total<=16:
            c = draw_single_card()
            cards_p2.append(c)
            for i in cards_p2:
                if str(i) in 'JQK':
                    i=10
                elif str(i) =='A':
                    if len(cards_p2) == 2:
                        if str(cards_p2[0]) == 'A':
                            #cards_p2[0] = 11
                            i=11
                        elif str(cards_p2[0]) != 'A' and str(cards_p2[1]) == 'A':
                            #cards_p2[1] = 11
                            i=11
                        elif str(cards_p2[0]) == 'A' and str(cards_p2[1]) == 'A':
                            #cards_p2[0] = 11
                            i=1
                    else:
                        i=1
                p2_total+=i
            print(cards_p2)
            chance=2
            hit_stand(cards_p1,cards_p2,chance)
            
        

def draw_cards():
    '''
    Taken Two Empty List in which player 1 and player 2 cards gets appended
    Every Card is Being Fetched By The Function draw_single_card()
    Appended The Cards Returned by draw_single_card() in the respective lists.
    The Final List Is No Longer an empty list. The cards have been appended and contains 2 cards each.
    Called Function hit_stand() to give the user the opportunity to draw another card or stand if theylike.
    '''
    cards_player1=[]
    cards_player2=[]
    chance=1
    p1c1=draw_single_card()
    p1c2=draw_single_card()
    p2c1=draw_single_card()
    p2c2=draw_single_card()
    cards_player1.append(p1c1)
    cards_player1.append(p1c2)
    cards_player2.append(p2c1)
    cards_player2.append(p2c2)
    print("Your Cards:", cards_player1)
    print("Computer's First Card:" , cards_player2[0])
    hit_stand(cards_player1, cards_player2, chance)
    
def welcome(): #Prints Logo. And Calls Function Draw_Cards().
    print(logo)
    draw_cards()
    
def choice(): #Asking The User If They Want To Play BlackJack. If They Enter Y, the game continues using Welcome() but is they enter N, the game stops because of SysExit Call. Else The sysytem Will show Invalid Input for any other Input.
    inp1='y'
    while inp1=='y':
        ch=input("Do you wish to play BlackJack: (Y - Yes | N - No): ")
        ch=ch.lower()
        if ch=='n':
            raise SystemExit 
        elif ch=='y':
            welcome() #Calling Welcome Function
            inp1="n"
        else:
            print("Invalid Input")
            inp1 = input("Do you wish to continue: (Y - Yes | N - No) ")
choice() #Calling Choice Function
