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
    if os.getcwd() != original_pathway:
        os.chdir(original_pathway)
    if directory_Food_Calculator not in os.listdir(original_pathway):
        os.mkdir(directory_Food_Calculator)
        os.chdir(original_pathway)
        os.chdir(directory_Food_Calculator)
    os.chdir(directory_Food_Calculator)
    
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
    
def foodCalculator(w, x, y, z, l, m):
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
    for ingredient, total_serving, amount_used, store_cost in zip(w, x, y, z):
        print(f"The total serving of {ingredient}: {total_serving}")
        print(f"Amount of {ingredient} servings used: {amount_used}")
        print(f"The store cost of {ingredient}: {store_cost}")
        
    isCorrect = None
    while isCorrect == None:
        isCorrect = input(f"Is this info correct?: " )
        if isCorrect == 'y':
            print("\nAwesome! So here's how much each ingredient cost:\n")
        elif isCorrect == 'n':
            whichIngredient = None
            while whichIngredient == None:
                whichIngredient = input(f"Which ingredient is incorrectly inputted? (Pls note it's case sensitive):\n{w}\n").strip()
                for ingredient, total_serving, amount_used, store_cost in zip(w, x, y, z):
                    if whichIngredient == ingredient:
                        w.remove(ingredient)
                        x.remove(total_serving)
                        y.remove(amount_used)
                        z.remove(store_cost)
                        print(f"Alright, erasing ingredient, {whichIngredient}, data...")
                        foodCalculator(w, x, y, z, l, m) 
                    else:
                        print(f"Sorry, I dont see {whichIngredient}. Please try again")
                        whichIngredient = None
        else:
            print("Sorry, I don't understand. Do you mind typing that out again?")
            isCorrect = None
    
    empty_l = []
    empty_m = []
    l = empty_l
    m = empty_m
    for ingredient, total_serving, amount_used, store_cost in zip(w, x, y, z):
        cost_per_serving2 = (total_serving)/(store_cost)
        l.append(cost_per_serving2)
        ingredients_actual_cost2 = (cost_per_serving2 * amount_used)
        m.append(ingredients_actual_cost2)
        print(f"{ingredient} actual cost is {ingredients_actual_cost2}")

    total = sum(m)
    total = int(total * 100) / 100
    print(f"Your meals total is {total}")
    print(w,x,y,z,l,m)
    is_that_all = None
    while is_that_all == None:
        is_that_all = input("Is that all the ingredients for this meal?(Y/N): ").lower().strip()
        if is_that_all == 'y':
            print("Alright, let's save this into the system!")
            print("Heading over to saving function...")
            createFolderandFile(w, x, y, z, l, m) 
        elif is_that_all == 'n':
            print("Let's make add some more ingredients!")
            foodCalculator(w,x,y,z,l,m)
        else:
            print("Sorry, I don't have autocorrect yet so I don't understand, my friend. Please try again.")
            is_that_all = None
    
    


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

def accessFolderandFile():
    
    os.chdir(original_pathway)
    os.chdir(directory_Food_Calculator)
    if len(os.listdir()) == 0: # This is the Food Calculator folder is completely empty
        print("It seems barren. Let's go to the main menu.\nLoading main menu...")
        initiation()
    for mealFolders in os.listdir():
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

    for ingredient, total_serving, amount_used, store_cost, costPerServing, actualCost in zip(d["List of ingredients: "], d["Ingredients total serving: "], d["Amount of ingredients servings used: "], d["Ingredients store cost: "], d["Cost per serving: "], d["Ingredient actual cost: "]):
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
                print(ingredient)
                action = None
            elif action == 'total serving':
                print("")
                print(f"The {ingredient}'s total serving: {total_serving} ")
                action = None
            elif action == 'amount':
                print("")
                print(f"Amount of {ingredient} used (based on serving size): {amount_used}")
                action = None
            elif action == 'store cost':
                print("")
                print(f"{ingredient} store cost: {store_cost}")
                action = None
            elif action == 'serving cost':
                print("")
                print(f"{ingredient} cost per serving: {costPerServing}")
                action = None
            elif action == 'actual cost':
                print("")
                print(f"{ingredient} actual cost: {actualCost}")
                action = None
            elif action == 'all info':
                print(f"\n{access}'s cost is {total}\n")
                print(f"Ingredient: {ingredient}")
                print(f"The {ingredient}'s total serving: {total_serving}")
                print(f"Amount of {ingredient} used (based on serving size): {amount_used}")
                print(f"{ingredient} store cost: {store_cost}")
                print(f"{ingredient} cost per serving: {costPerServing}")
                print(f"{ingredient} actual cost: {actualCost}")
                action = None
            elif action == 'meal cost':
                print("")
                print(f"{access}'s cost is {total} ")
                action = None
            elif action == 'main menu':
                print("\nGot it. Returning to main menu...\n")
                initiation()
            else:
                print("\nSorry, I don't have autocorrect so I wasn't sure what you meant. Please try again.")
                action = None        
    # list_of_ingredients = []                # w
    # ingredients_total_serving = []          # x
    # amount_ingredients_used = []            # y
    # ingredients_store_cost = []             # z
    # 
    # cost_per_serving = []                   # l                 Last two are byproducts of foodCalculator()
    # ingredient_actual_cost = []             # m


def updateIngredient(tempw, tempx, tempy, tempz, templ, tempm, user_input_w, user_input_x, user_input_y, user_input_z):
   
    for ingredient, total_serving, amount_used, store_cost, costPerServing, actualCost in zip(tempw, tempx, tempy, tempz, templ, tempm):
        if ingredient == user_input_w:
            tempw.remove(ingredient)
            tempx.remove(total_serving)
            tempy.remove(amount_used)
            tempz.remove(store_cost)
            templ.remove(costPerServing)
            tempm.remove(actualCost)
    
    tempw.append(user_input_w)
    tempx.append(user_input_x)
    tempy.append(user_input_y)
    tempz.append(user_input_z)

    cost_per_serving2 = (user_input_x)/(user_input_z)
    templ.append(cost_per_serving2)
    ingredients_actual_cost2 = (cost_per_serving2 * amount_used)
    tempm.append(ingredients_actual_cost2)

    
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
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    initiation()
