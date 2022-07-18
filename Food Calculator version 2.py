# Lets see if I can make Food Calculator V1 again but cleaner while not looking at the original
# Start time: Jul 7 2022 12:00 PM Central
# Last Updated: Jul 10 3:52 PM Central
# Complete Jul 10 4:00 PM Central
import pickle
import os



os.system("clear")

original_pathway = os.getcwd()
directory_Food_Calculator = "Food Calculator V2"

list_of_ingredients = []                # w
ingredients_total_serving = []          # x
amount_ingredients_used = []            # y
ingredients_store_cost = []             # z

cost_per_serving = []                   # l                 Last two are byproducts of foodCalculator()
ingredient_actual_cost = []             # m


def initiation():
    # print(os.getcwd())
    if os.getcwd() != original_pathway:
        os.chdir(original_pathway)
    if directory_Food_Calculator not in os.listdir(original_pathway):
        os.mkdir(directory_Food_Calculator)
        os.chdir(original_pathway)
        os.chdir(directory_Food_Calculator)
    os.chdir(directory_Food_Calculator)
    # print(os.getcwd())
    
    pick_function = None
    while pick_function == None:
        pick_function = input("Pick an option: calculate food cost (type calculate); access meals (type meals); or exit program (type exit)?: ").lower().strip()
        if pick_function == 'calculate':
            print("Alright, lets make some meals!\nLoading Food Calculator...\n")
            foodCalculator(list_of_ingredients, ingredients_total_serving, amount_ingredients_used, ingredients_store_cost, cost_per_serving, ingredient_actual_cost)
        elif pick_function == 'meals':
            print("Accessing meals...")
            accessFolderandFile()
        elif pick_function == 'exit':
            print("Ok dokes, till next time!")   
            break
        else:
            print("Sorry, I didn't understand. I dont have autocorrect yet so you got to type it out clearly.")
            pick_function = None
    
# This should be done Jul 9 10:53 AM
def foodCalculator(w, x, y, z, l, m):

    # print("foodCalculator MARKER 1 ============================================================================")
    # print(w, x, y, z, l, m)


    # w list_of_ingredients = []
    # x ingredients_total_serving = []
    # y amount_ingredients_used = []
    # z ingredients_store_cost = []

    # l cost_per_serving = []                  
    # m ingredient_actual_cost = [] 
    user_input_w = None
    while user_input_w == None:            
        try:
            user_input_w = input("Please enter ingredient: ").strip()
            user_input_x = float(input("Please enter ingredient's total serving: "))
            user_input_y = float(input("Please enter amount of serving used: "))
            user_input_z = float(input("Please enter ingredient's cost: "))
        except ValueError:
            print("It seems you've inputted something that's not a number. Please try again.")
            user_input_w = None


    if user_input_w not in w:
        w.append(user_input_w)    
        x.append(user_input_x)
        y.append(user_input_y)
        z.append(user_input_z)

    else:
        alreadyExist = None
        while alreadyExist == None:
            alreadyExist = input(f"The ingredient, {user_input_w}, is already in this list. Would you like to update the list with this data (update) or leave it as it is (continue)?: ").lower().strip()
            if alreadyExist == 'update':
                updateIngredient(w, x, y, z, l, m, user_input_w, user_input_x, user_input_y, user_input_z)
            elif alreadyExist == 'continue':
                print("Got it. Leaving it as it is.")
            else:
                print("Sorry, I don't have autocorrect yet so please try again.")
                alreadyExist = None

    print(f"\nList of ingredient(s): {w}")
    for idx, value in enumerate(w):
        for idx2, value2 in enumerate(x):
            for idx3, value3 in enumerate(y):
                for idx4, value4 in enumerate(z):
                    if idx == idx2 == idx3 == idx4:
                        print(f"The total serving of {value}: {value2}")
                        print(f"Amount of {value} servings used: {value3}")
                        print(f"The store cost of {value}: {value4}")
        
    isCorrect = None
    while isCorrect == None:
        isCorrect = input(f"Is this info correct?: " )
        if isCorrect == 'y':
            print("\nAwesome! So here's how much each ingredient cost:\n")
        elif isCorrect == 'n':
            whichIngredient = None
            while whichIngredient == None:
                whichIngredient = input(f"Which ingredient is incorrectly inputted? (Pls note it's case sensitive):\n{w}\n").strip()
                if whichIngredient in w:
                    for idx, value in enumerate(w):
                        for idx2, value2 in enumerate(x):
                            for idx3, value3 in enumerate(y):
                                for idx4, value4 in enumerate(z):
                                    if value == whichIngredient and idx == idx2 == idx3 == idx4:
                                        w.remove(value)
                                        x.remove(value2)
                                        y.remove(value3)
                                        z.remove(value4)
                                
                                        print(f"Alright, erasing ingredient, {whichIngredient}, data...")
                                        foodCalculator(w, x, y, z, l, m) 
        else:
            print("Sorry, I don't understand. Do you mind typing that out again?")
            isCorrect = None
    
    # print("ENUMERATE MARKER ============================================================================")
    empty_l = []
    empty_m = []
    l = empty_l
    m = empty_m
    # print(w,x,y,z,l,m)
    for idx, value in enumerate(w):
        for idx2, value2 in enumerate(x):
            for idx3, value3 in enumerate(y):
                for idx4, value4 in enumerate(z):
                    if idx == idx2 == idx3 == idx4:
                        cost_per_serving2 = (value2)/(value4)
                        l.append(cost_per_serving2)
                        ingredients_actual_cost2 = (cost_per_serving2 * value3)
                        m.append(ingredients_actual_cost2)
                        # print("foodCalculator 'TOTAL' MARKER ============================================================================")
                        print(f"{value} actual cost is {ingredients_actual_cost2}")

    total = sum(m)
    # print("foodCalculator MARKER TOTAL ============================================================================")
    print(f"Your meals total is {total}")
    print(w,x,y,z,l,m)
    is_that_all = None
    while is_that_all == None:
        is_that_all = input("Is that all the ingredients for this meal?(Y/N): ").lower().strip()
        if is_that_all == 'y':
            print("Alright, let's save this into the system!")
            print("Heading over to saving function...")
            createFolderandFile(w, x, y, z, l, m) # Technically dont need total; could just do sum(m) to get the total when accessing files
        elif is_that_all == 'n':
            print("Let's make add some more ingredients!")
            foodCalculator(w,x,y,z,l,m)
        else:
            print("Sorry, I don't have autocorrect yet so I don't understand, my friend. Please try again.")
            is_that_all = None
    
    


# This should be done Jul 9 10:53 AM
def createFolderandFile(w, x, y, z, l, m):
    os.chdir(original_pathway)
    os.chdir(directory_Food_Calculator)
    mealname = input("Please enter a meal name: ")
    mealname = mealname + " meal"
    print(f"Creating {mealname} folder...")

    d = {
        "List of ingredients: ": w,                         # w
        "Ingredients total serving: ": x,                   # x
        "Amount of ingredients servings used: ": y,         # y
        "Ingredients store cost: ": z,                      # z
        
        "Cost per serving: ": l,                              # l                 Last two are byproducts of foodCalculator()
        "Ingredient actual cost: ": m                         # m
    } 

    try:
        os.mkdir(mealname)
    except OSError:
        print(f"{mealname} could not be created. Please check to see if it's made already. Otherwise, please choose a different name.")
        createFolderandFile(w, x, y, z, l, m)
    else:
        print(f"Creation of {mealname} was successful")
    print("Now, going to save the ingredients file...")
    os.chdir(mealname)
    pickle.dump(d, open("ingredients data", 'wb'))
    print("Ingredients saved!")
    print("Going back to Food Calculator V2 folder...")
    os.chdir(original_pathway)
    os.chdir(directory_Food_Calculator)


    print("What would you like to do now?")
    chooseFunction = None
    while chooseFunction == None:
        chooseFunction = input("Make more meals (calculate), access your meals (meals), or exit program (exit)?: ").lower().strip()
        if chooseFunction == 'calculate':
            print("Alright, let's make more meals!")
            foodCalculator(list_of_ingredients, ingredients_total_serving, amount_ingredients_used, ingredients_store_cost, cost_per_serving, ingredient_actual_cost)
        elif chooseFunction == 'meals':
            accessFolderandFile()
        elif chooseFunction == 'exit':
            print("Till next time!")
            break
        else:
            print("Sorry, you mind repeating that?")
            chooseFunction = None

# This should be done now Jul 10 4:00 PM
def accessFolderandFile():
    
    os.chdir(original_pathway)
    os.chdir(directory_Food_Calculator)
    # print(os.getcwd())
    if len(os.listdir()) == 0: # This is the Food Calculator V2 folder is completely empty
        print("It seems barren. Let's go to the main menu.\nLoading main menu...")
        initiation()
    for mealFolders in os.listdir():
        # print("accessFolderandFile MARKER 1 ============================================================================")
        # print(mealFolders)
        if 'meal' in mealFolders:
            print(mealFolders)
        else: # This is if there's a hidden DS Store file
            print("It seems barren. Let's go to the main menu.\nLoading main menu...")
            initiation()
    access = None
    while access == None:
        access = input("Which meal would you like to look at? (Pls note that input is case sensitive): ").strip()
        try:
            print(f"Attmepting to access {access}...")
            os.chdir(access)
            print("Attempt success. Now accessing ingredients...")
            d = pickle.load(open('ingredients data','rb'))
        except FileNotFoundError:
            print("Sorry, it seems that you mightve mistyped. What was that again?")
            access = None
 
    action = None
    while action == None: 
        action = input("\nWhat would you like to do? \nList of ingredients (type list)\nWhat is the ingredients' total serving (type total serving)\nWhat is the amount of the ingredient used (type amount)\nWhat is the store cost of the ingredient (type store cost)\nIngredient's cost per serving (type serving cost)\nIngredient's actual cost (type actual cost)\nGet meal's cost (type meal cost)\nAll of the above (type all info)\nReturn to main menu (type main menu)\nType here: ").lower().strip() # Last Checkpoint 2:16 PM
        # d = {
        # "List of ingredients: ": w,                         # w
        # "Ingredients total serving: ": x,                   # x
        # "Amount of ingredients servings used: ": y,         # y
        # "Ingredients store cost: ": z,                      # z
        # 
        # "Cost per serving: ": l,                              # l                 Last two are byproducts of foodCalculator()
        # "Ingredient actual cost: ": m                         # m
    # } 
        total = sum(d["Ingredient actual cost: "])
        if action == 'list':
            print("")
            print(f"These are the ingredients used in {access}: ")
            for w in d["List of ingredients: "]:
                print(w)
            action = None
        elif action == 'total serving':
            print("")
            for idx, w in enumerate(d["List of ingredients: "]):
                for idx2, x in enumerate(d["Ingredients total serving: "]): # LASTKJALKFJSLKFSFLJLKFASJLJSFLJAFSLKJ
                    if idx == idx2:
                        print(f"The {w}'s total serving: {x} ")
                        action = None

        elif action == 'amount':
            print("")
            for idx, w in enumerate(d["List of ingredients: "]):
                for idx3, y in enumerate(d["Amount of ingredients servings used: "]):
                    if idx == idx3:
                        print(f"Amount of {w} used (based on serving size): {y}")
                        action = None

        elif action == 'store cost':
            print("")
            for idx, w in enumerate(d["List of ingredients: "]):
                for idx4, z in enumerate(d["Ingredients store cost: "]):
                    if idx == idx4:
                        print(f"{w} store cost: {z}")
                        action = None
        elif action == 'serving cost':
            print("")
            for idx, w in enumerate(d["List of ingredients: "]):
                for idx5, l in enumerate(d["Cost per serving: "]):
                    if idx == idx5:
                        print(f"{w} cost per serving: {l}")
                        action = None
        elif action == 'actual cost':
            print("")
            for idx, w in enumerate(d["List of ingredients: "]):
                for idx6, m in enumerate(d["Ingredient actual cost: "]):
                    if idx == idx6:
                        print(f"{w} actual cost: {m}")
                        action = None
        elif action == 'all info':
            print(f"\n{access}'s cost is {total}\n")
            for idx, w in enumerate(d["List of ingredients: "]):
                for idx2, x in enumerate(d["Ingredients total serving: "]):
                    for idx3, y in enumerate(d["Amount of ingredients servings used: "]):
                        for idx4, z in enumerate(d["Ingredients store cost: "]):
                            for idx5, l in enumerate(d["Cost per serving: "]):
                                for idx6, m in enumerate(d["Ingredient actual cost: "]):
                                    if idx == idx2 == idx3 == idx4 == idx5 == idx6:
                                        print(f"Ingredient: {w}")
                                        print(f"The {w}'s total serving: {x}")
                                        print(f"Amount of {w} used (based on serving size): {y}")
                                        print(f"{w} store cost: {z}")
                                        print(f"{w} cost per serving: {l}")
                                        print(f"{w} actual cost: {m}")
                                        action = None
        elif action == 'meal cost':
            print("")
            print(f"{access}'s cost is {total} ")
            action = None
        elif action == 'main menu':
            print("Got it. Returning to main menu...")
            initiation()
        else:
            print("Sorry, I don't have autocorrect so I wasn't sure what you meant. Please try again.")
            action = None        
    # list_of_ingredients = []                # w
    # ingredients_total_serving = []          # x
    # amount_ingredients_used = []            # y
    # ingredients_store_cost = []             # z
    # 
    # cost_per_serving = []                   # l                 Last two are byproducts of foodCalculator()
    # ingredient_actual_cost = []             # m


# This should also be done Jul 9 10:53 AM
def updateIngredient(tempw, tempx, tempy, tempz, templ, tempm, user_input_w, user_input_x, user_input_y, user_input_z):
    # print("updateIngredient MARKER 1 ============================================================================") 
    # print(tempw, tempx, tempy, tempz, templ, tempm)
    for idx, value in enumerate(tempw):
        for idx2, value2 in enumerate(tempx):
            for idx3, value3 in enumerate(tempy):
                for idx4, value4 in enumerate(tempz):
                    for idx5, value5 in enumerate(templ):
                        for idx6, value6 in enumerate(tempm):
                            if value == user_input_w and idx == idx2 == idx3 == idx4 == idx5 == idx6:
                                tempw.remove(value)
                                tempx.remove(value2)
                                tempy.remove(value3)
                                tempz.remove(value4)
                                templ.remove(value5)
                                tempm.remove(value6)
    total = sum(tempm)
    # print("updateIngredient MARKER 2 ============================================================================") 
    # print(tempw, tempx, tempy, tempz, templ, tempm, total)
    tempw.append(user_input_w)
    tempx.append(user_input_x)
    tempy.append(user_input_y)
    tempz.append(user_input_z)

    cost_per_serving2 = (user_input_x)/(user_input_z)
    templ.append(cost_per_serving2)
    ingredients_actual_cost2 = (cost_per_serving2 * value3)
    tempm.append(ingredients_actual_cost2)

    # total2 = sum(tempm)
    # print("updateIngredient MARKER 3 ============================================================================") 
    # print(tempw, tempx, tempy, tempz, templ, tempm, total2)
    chooseFunction = None
    while chooseFunction == None:
        chooseFunction = input(f"Alright, ingredient, {user_input_w}, has been updated. Would you like to add more ingredients (more) or is that all for this meal (finish)?: ").lower().strip()
        if chooseFunction == 'more':
            print("Sounds good. Let's make add some more!")
            foodCalculator(tempw, tempx, tempy, tempz, templ, tempm)
        elif chooseFunction == 'finish':
            print("Awesome. Let's name this meal and save it into the system!")
            createFolderandFile(tempw, tempx, tempy, tempz, templ, tempm) 
        else:
            print("Sorry, I don't have autocorrect yet, I didn't understand what you said. Please try again.")
            chooseFunction = None
        

if __name__  == "__main__":
    initiation()




'''
Jul 7
2:16 PM
Ngl, this is starting to get tiresome. Perhaps coding nonstop for almost 7 days straight isn't the healthiest thing to do. I guess
I'll stop for now (Jul 7 2:16 PM) and focus on leetcode problems. Maybe that'll help. I can't go back home till 4 PM since the apartment has been blasted with
pesticides or whatnot. If only my roommates knew how to keep their rooms clean... Besides that, I manage to find a really neat private spot where I can truly
relax, not having to worry about any subtle noises I could make at the library.
'''
'''
Jul 8
8:00 AM
I'm starting to think I might getting a little too obsessed with this whole project; although I was planning to add other features to this such as barcode scanner
and web scraping, I didn't think I would be coming back to 'update' this project so soon. I was planning to leave it as it is, with faults and all, and go onto
a new python file to work on the other features. I guess I can't. The bugs are bothering me and I want to add some new user friendly features that arent barcode or 
web scraping or whatever. Thus far, I managed to make it 'cleaner' than Food Calculator V1; it's much easier to start from scratch since I have a better idea what the program 
would be. I'm adding updateIngredient() into the thing so that if the user accidentally misinputs or simply wants to change something in the ingredient data, they would be able 
to without starting all over from square one. Apparently, it didn't do that in the first version.
'''
'''
Jul 10
8:03 AM
It seems I forgot to log what happened yesterday. Oh well. I managed to finish all the functions except for accessFolderandFiles() yesterday. Too many details to try and remember.
I want to incorporate a way to edit the ingredients after accessing them, but after running some code in my head, that would be quite a hassle to do and take some time
that I don't exactly I have. I still need to study up on algorithms and applications of it as well as Big O. I also need to get more projects done to prove my work experience.
Troublesome. If only I could code nonstop; however, my limiting factor rn is my lower back. I wonder if there's a way to completely prevent that. Proper posture can only hold out
for so long. I'm getting way off topic. I'm going to finish up the accessFolderandFiles() today and move on to the next project: a barcode scanner. 
3:52 PM
Project is practically complete. There are some features that I still want to add, but for now, this will do. All loose ends should be dealt with and should be functionally
properly now. Onto the next project that will eventually be a feature to this: barcode scanner. 
'''