import random
import time

def display(cards:list,limit:int=3, header:bool=True):
    count=0
    print("\n       ⬇COLUMN 1⬇","      ⬇COLUMN 2⬇","      ⬇COLUMN 3⬇\n") if header else ...
    for i in cards: 
        print("\t",f"{i:10}",end="")
        count+=1
        if count%limit==0:
            print("\n")

def distributer(cards:list):
    return cards[::3],cards[1::3],cards[2::3]

def sorter(cards:list):
    column_a,column_b,column_c = distributer(cards)
    select_column = column_selector()

    if select_column == 1:
        cards = column_c+column_a+column_b
    
    elif select_column == 2: 
        cards = column_a+column_b+column_c 
    
    elif select_column == 3: 
        cards = column_a+column_c+column_b 
    
    return cards

def column_selector():
    while True:
        select_column = input("\nWhich column has your card(1/2/3) ? : ")
        if select_column.isdigit():
            if int(select_column) in range(1,4):
                return int(select_column)
            else:
                print("Input the column number that contains your card")
        else:
            print("Invalid input..")
    
print("\n\t\t\t   CARD GAME\n\t\tI WILL FIND THE CARD IN YOUR MIND\n\n")

card_list = ["Ace(♣)" ,"2(♣)" ,"3(♣)" ,"4(♣)" ,"5(♣)" ,"6(♣)" ,"7(♣)" ,
            "8(♣)" ,"9(♣)" ,"10(♣)" ,"Jack(♣)" ,"Queen(♣)" ,"King(♣)" ,
            "Ace(♢)" ,"2(♢)" ,"3(♢)" ,"4(♢)" ,"5(♢)" ,
            "6(♢)" ,"7(♢)","8(♢)" ,"9(♢)" ,"10(♢)" ,
            "Jack(♢)" ,"Queen(♢)" ,"King(♢)","Ace(♡)" ,"2(♡)" ,
            "3(♡)" ,"4(♡)" ,"5(♡)" ,"6(♡)" ,"7(♡)" , "8(♡)" ,
            "9(♡)" ,"10(♡)" ,"Jack(♡)" ,"Queen(♡)" ,"King(♡)",
            "Ace(♠)" ,"2(♠)" ,"3(♠)","4(♠)" ,"5(♠)" ,"6(♠)" ,
            "7(♠)","8(♠)" ,"9(♠)" ,"10(♠)" ,"Jack(♠)" ,"Queen(♠)" ,
            "King(♠)"]
         
card_list_choice=[]

while True:
    random_card = random.choice(card_list)
    if random_card not in card_list_choice:
        card_list_choice.append(random_card)
        if len(card_list_choice)==21:
            break

card_list_display=[]
while True:
    random_display = random.choice(card_list_choice)
    if random_display not in card_list_display:
        card_list_display.append(random_display)
        if len(card_list_display)==21:
            break

display(card_list_display ,limit=7 , header= False)

print("\nThink about anyone card from the above list and keep it in your mind")

time.sleep(1.5)

while True:
    ready = input("Are you READY (y/n) ? : ")
    ready=ready.lower()
    if ready == "y":
        break
    elif ready == "n":
        exit()
    else :
        print("Invalid Move..")

display(card_list_choice)
list_2=sorter(card_list_choice)
display(list_2)
list_3=sorter(list_2)
display(list_3)
list_4=sorter(list_3)
print("The card in your mind is...",list_4[10],". HAHA\n")
