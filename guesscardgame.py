import random
import time

print("\n\t\t\t   CARD GAME\n")
    
print("\t\tI WILL FIND THE CARD IN YOUR MIND\n\n")

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


b=0
for i in card_list_display:
    print(f"{i:10}",end="")
    b=b+1
    if b%7 == 0:
        print("\n")

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


count=0
print("\n       ⬇COLUMN 1⬇","      ⬇COLUMN 2⬇","      ⬇COLUMN 3⬇\n")
for i in card_list_choice: 
    print("\t",f"{i:10}",end="")
    count+=1
    if count%3==0:
        print("\n")


list_1 = []
for i in card_list_choice:
    list_1.append(i)


column_a = list_1[::3]
column_b = list_1[1::3]
column_c = list_1[2::3]


while True:
    select_column = input("\nWhich column has your card(1/2/3) ? : ")

    if select_column.isdigit():
        if int(select_column) in range(1,4):
            break
        else:
            print("Input the column number that contains your card")

    else:
        print("Invalid input..")


#LIST 2
list_2=[]
if int(select_column) == 1:
    list_2 = column_c+column_a+column_b
 
elif int(select_column) == 2: 
    list_2 = column_a+column_b+column_c 
 
elif int(select_column) == 3: 
    list_2 = column_a+column_c+column_b 


count=0
print("\n       ⬇COLUMN 1⬇","      ⬇COLUMN 2⬇","      ⬇COLUMN 3⬇\n")
for i in list_2: 
    print("\t",f"{i:10}",end="")
    count+=1
    if count%3==0:
        print("\n")


column_p = list_2[::3]
column_q = list_2[1::3]
column_r = list_2[2::3]

while True:
    select_column = input("\nWhich column has your card(1/2/3) ? : ")
    if select_column.isdigit():
        if int(select_column) in range(1,4):
            break
        else:
            print("Input the column number that contains your card")
    elif select_column.isalpha():
        print("Invalid input..")


list_3=[]
if int(select_column) == 1:
    list_3 = column_r+column_p+column_q

elif int(select_column) == 2:
    list_3 = column_p+column_q+column_r

elif int(select_column) == 3:
    list_3 = column_p+column_r+column_q


count=0
print("\n       ⬇COLUMN 1⬇","      ⬇COLUMN 2⬇","      ⬇COLUMN 3⬇\n")
for i in list_3: 
    print("\t",f"{i:10}",end="")
    count+=1
    if count%3==0:
        print("\n")


column_x = list_3[::3]
column_y = list_3[1::3]
column_z = list_3[2::3]
    


while True:
    select_column = input("\nWhich column has your card(1/2/3) ? : ")

    if select_column.isdigit():
        if int(select_column) in range(1,4):
            break
        else:
            print("Input the column number that contains your card")

    else:
        print("Invalid input..")


list_4=[]
if int(select_column) == 1:
    list_4 = column_z+column_x+column_y

elif int(select_column) == 2:
    list_4 = column_x+column_y+column_z

elif int(select_column) == 3:
    list_4 = column_x+column_z+column_y

print("The card in your mind is...",list_4[10],". HAHA\n")
