
from operator import index
import random
#START TEST ZONEv2(successful)
print('Thank you for choosing SkyNet Industries for planning out your daily scheduling!')
#Below are all lists stored in variables needed to make the 'return_item_for_schedule' work.
parameters_for_destination = [["King Aruthur's Round Table", "the Surface of the Sun", "the Kremlin", "the local Dump", "the Future"], "If you really don't want to do ANY sight seeing type 'Skip' and then press 'Enter'. Otherwise type anything else followed by 'Enter' to start again: ", "After running a diagnostic brain scan it looks like our most compatable destination for you is", 'nowhere']
parameters_for_transportation = [['Rocket Ship', 'Submarine', 'Teleporter', 'Hamster Wheel', 'Glider'], "If you really feel like walking enter 'Skip'. Otherwise type anything else followed by 'Enter' to start again: ", "After checking all available transport it looks like our most compatable transportation for you is a", 'foot']
parameters_for_restaurant = [["the Tun Tavern","The Chow Hall", "the McDonalds Top Secret Platinum Club", "Bob's Burgers", "Costco"], "If you really don't feel hungry enter 'Skip'. Otherwise type anything else followed by 'Enter' to start again: ", "After a quick search through all available restaurants with seating available it looks like our most compatable restaurant for you is", 'home']
parameters_for_entertainment = [["swiming with sharks", "selling your freedom to fight in the Colosseum", "playing chess against ME your LOVING computer", "challenging your arch-nemesis too a duel (Black Powder Pisols only)"], "If you really don't feel like having fun enter 'skip'. Otherwise type anything followed by 'Enter' to start again: ", "After checking our data bases for the activity which scores highest for Dopamine and Serotonin releases, you would have most fun", 'watching the grass grow']
#Below is our money maker. Used and re-used to allow the user to return a random list item to add to their schedule. It will repeat through the list until the user makes a decision.
def return_item_for_schedule(master_list):
    item_chosen = False
    disregarded_items = []
    while item_chosen == False:
            if len(master_list[0]) == 0:
                skip_list_or_repeat_options = input(master_list[1]).upper()
                if skip_list_or_repeat_options == 'SKIP':
                    return master_list[3]
                else:
                    master_list[0] = disregarded_items
                    disregarded_items = []
            selected_list_item = random.choice(master_list[0])
            current_index = master_list[0].index(selected_list_item)
            user_confirmation = input(master_list[2] + ' ' + selected_list_item + """. Does this sound good to you? 
            Y/N: """).upper()
            if user_confirmation == 'Y' or user_confirmation == 'YES':
                print('Great! onto the next decision.')
                return(selected_list_item)
            else:
                if len(master_list[0]) == 1:
                    print('Not making it easy for me huh...')
                else:
                    print('No worries, lets look through our options again.')
                disregarded_items.append(master_list[0].pop(current_index))
#Here we use our variables from above, each variable contains all FOUR required values to make the function run. 
chosen_destination = return_item_for_schedule(parameters_for_destination)
chosen_restaurant = return_item_for_schedule(parameters_for_restaurant)
chosen_transport = return_item_for_schedule(parameters_for_transportation)
chosen_entertainment = return_item_for_schedule(parameters_for_entertainment)
#list to be passed into the confirmation function.
final_list = [chosen_destination, chosen_restaurant, chosen_transport, chosen_entertainment]
#This function call gives the user a change to look over their schedule and make last minute changes or continue.
def final_confirmation():
    print(f'Alright, Reviewing your days schedule you will be: traveling by {chosen_transport} to {chosen_destination} to do some sight seeing. After which you will eat at {chosen_restaurant} and will close the day off by {chosen_entertainment}.')
    confirmed = input(f"""To confirm your day type 'Yes' then enter. 
    To randomly re-select destination type 'Destination' then enter. 
    To randomly re-select transportation type 'Transportation' then enter.
    To randomly re-select restaurant type 'Restaurant' then enter.
    To randomly re-select entertainment type 'Entertainment' then enter.
    Type Command here: """).upper()
    if confirmed == 'Y' or confirmed == 'YES':
        return True
    else:
        return confirmed
#Once final_confirmation returns True then we move to the Final block of code.
confirmed = final_confirmation()
#Kind of like a router this bad boy can send the user to whatever spot in the code they need to go to get another part of their schedule.
while confirmed != True:
    if confirmed == 'DESTINATION':
        chosen_destination = return_item_for_schedule(parameters_for_destination)
        confirmed = final_confirmation()
    elif confirmed == 'TRANSPORTATION':
        chosen_transport = return_item_for_schedule(parameters_for_transportation)
        confirmed = final_confirmation()
    elif confirmed == 'RESTAURANT':
        chosen_restaurant = return_item_for_schedule(parameters_for_restaurant)
        confirmed = final_confirmation()
    elif confirmed == 'ENTERTAINMENT':
        chosen_entertainment = return_item_for_schedule(parameters_for_entertainment)
        confirmed = final_confirmation()
    else:
        print("Sorry, you didn't input a valid command.")
        confirmed = final_confirmation()
#Final chunk of code that runs once the user confirms up in the 'final_confirmation' 
if confirmed == True:
    print(f"Enjoy traveling by {chosen_transport}, eating at {chosen_restaurant}, basking in the awesomeness of {chosen_destination}, and of course enjoy {chosen_entertainment}. Thank you for choosing SKYNET Inc, where we make your life our number 1 priority.")