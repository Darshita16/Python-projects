def read_deck(filename):
    file=open(filename,'r');
    text=file.readlines();
    deck=[];
    for line in text:
        line=line.strip();
        deck.append(line);
        if line == "Joker" or line=='':
            deck.remove(line);
    return deck;

def shuffle(deck):
    shuffled_deck=[]
    left=deck[:(len(deck)//2)];
    right=deck[(len(deck)//2):];
    for i in range(len(left)):
        shuffled_deck.append(left[i]);
        shuffled_deck.append(right[i]);
    return shuffled_deck;

def deal_card(shuffled_deck, number_of_cards):
    agent=[]
    if len(shuffled_deck)>=  number_of_cards:
        if number_of_cards ==1:
            agent.append(shuffled_deck.pop());
        
        elif number_of_cards > 1:
            for i in range(number_of_cards):
                agent.append(shuffled_deck.pop());  
        return agent;
    else:
        return None;
    
def card_value(card):
    cut_text=card.split()[0]
    
    if cut_text =='Ace':
        value=11;
    elif cut_text == '2':
        value =2;
    elif cut_text == '3':
        value =3;
    elif cut_text == '4':
        value =4;    
    elif cut_text == '5':
        value =5;
    elif cut_text == '6':
        value =6;    
    elif cut_text == '7':
        value =7;
    elif cut_text == '8':
        value =8;
    elif cut_text == '9':
        value =9;   
    elif cut_text == "Jack" or cut_text=="Queen" or cut_text=="King" or cut_text=="10":
        value =10;
        
    return value;

def hand_value(hand):
    total=0
    for i in range(len(hand)):
        x=hand[i]
        values=card_value(x);
        total = total + values;
    return total;


def is_blackjack(hand):
    total2=hand_value(hand)
    if total2 == 21:
        return True;
    else:
        return False;
    return hand_value(hand)==21;
    
def should_hit(hand):
    value1=hand_value(hand);
    if value1 < 17:
        return True;
    else:
        return False;
   
def play_hand(hand, shuffled_deck):
    if len(shuffled_deck)>0:
        y= True;
    while should_hit(hand)==True and y== True:
        card1=deal_card(shuffled_deck,1);
        x=card1[0];
        hand.append(x);  
    
def compare_hands(agent_hand, dealer_hand):
    agent_total=hand_value(agent_hand);
    #print(agent_total);
    dealer_total=hand_value(dealer_hand);
    #print(dealer_total);
    deck='';
    if agent_total > 21 and dealer_total > 21:
        result = "Player busts"
    elif agent_total > 21:
        result = "Player busts!"
    elif dealer_total > 21:
        result = "Dealer busts!"
    else:
        if agent_total > dealer_total:
            result = "Player wins!"
        elif dealer_total > agent_total:
            result = "Dealer wins!"
        else:
            result = "Push!"
    return result;
        
def main():
    filename=input("Enter filename: ");
    deck_of_cards=read_deck(filename);
    shuffled_deck=shuffle(deck_of_cards);
    
    while len(shuffled_deck)>10:
        number_of_cards=2;
        agent_hand=deal_card(shuffled_deck,number_of_cards);
        dealer_hand=deal_card(shuffled_deck,number_of_cards);
        play_hand(agent_hand,shuffled_deck);
        play_hand(dealer_hand,shuffled_deck);
        result=compare_hands(agent_hand,dealer_hand);
        print(result);
main();
