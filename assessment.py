print(">>Welcome to the Mall")
print(">>Please select the section.")
floor_1="cloth section"
floor_2="perfume section"
floor_3="play section"
floor_4="hotel section" 
mall={
    "cloth_section":["rare rabit","baggi","lenin","jacey","celvin"],
    "perfume_section":["park avenvue","villan","fogg","sk","men in blue"],
    "play_section":["water fall","video games","club"],
    "hotel_section":["romantic","sana","pvr","taj"]
}
print(floor_1)
print(floor_2)
print(floor_3)
print(floor_4)
user=input("enter your section:")
if user==floor_1:
    print(f"{user} is in first floor. And the brands shown below: ")
    print(mall["cloth_section"])
    user_1=input("enter your cloth brand:")
    if user_1 in mall["cloth_section"]:
        print(f"{user_1} is available .")
    else:
        print(f"sorry, {user_1} is not available.")

elif user==floor_2:
    print(f"{user} is in second floor. And the brands shown below: ")
    print(mall["perfume_section"])
    user_2=input("enter your perfume brand name:")
    if user_2 in mall["perfume_section"]:
        print(f"{user_2} is available .")
    else:
        print(f"sorry, {user_2} is not available.")

elif user==floor_3:
    print(f"{user} is in third floor. And the type of games are shown below: ")
    print(mall["play_section"])
    user_3=input("enter your game name:")
    if user_3 in mall["play_section"]:
        print(f"{user_3} is available .")
    else:
        print(f"sorry, {user_3} is not available.")

elif user==floor_4:
    print(f"{user} is in fourth floor. And the hotel names are shown below: ")
    print(mall["hotel_section"])
    user_4=input("enter your hotel name:")
    if user_4 in mall["hotel_section"]:
        print(f"{user_4} hotel is available .")
    else:
        print(f"sorry, {user_4} is not available.")

else:
    print("Please enter valid section.")