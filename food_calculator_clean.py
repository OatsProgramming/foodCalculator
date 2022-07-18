import os
import pickle

os.system("clear")

# w is ingredient name
# x is cost per serving
# y is user's number of serving used in the meal
# z is total cost of ingredient (x * y)

w = []
x = []
y = []
z = []



original_pathway = os.getcwd()
directory_Food_Calculator = "Food Calculator"

def meals():
    os.chdir(original_pathway)
    os.chdir(directory_Food_Calculator)
    meal_list = [meal for meal in os.listdir() if 'meal' in meal]

    if len(meal_list) == 0:
        print("\nIt seems that there's nothing here. Quite barren. Let's head back to the main menu.")
        print("Going to main menu...\n")
        initiation()

    meal_folder = None
    while meal_folder == None:
        print("") # This is just to make the output look cleaner when listing all meal items in the meal list
        for mealItem in meal_list:
            print(mealItem) 
        meal_folder = input("\nWhich meal would you like to look at: ")
        try:
            os.chdir(meal_folder)
        except OSError:
            print(f"The meal, {meal_folder}, does not exist. Please try again.")
            meals()
        else:
            print(f"Opening {meal_folder} folder...\n")
            print(os.listdir())
            if 'ingredients' in os.listdir():
                dictionary = pickle.load(open("ingredients","rb"))
            print("Now accessing ingredients file...")
    
    w_dict = dictionary["Name of ingredient(s): "]
    x_dict = dictionary["Cost per serving: "]
    y_dict = dictionary["Amount of servings used: "] 
    z_dict = dictionary["Total cost per use: "]
    total = sum(z_dict)

    meal_files = None
    while not meal_files:
        meal_files = input(f"What would you like to look at: \n\nList of Ingredients (type list) \nIngredients Cost Per Serving (type cost) \nAmount of ingredient servings used in {meal_folder} (type servings) \nTotal Cost of {meal_folder} (type total cost) \nAll Info (type all info) \nReturn to main menu (type main menu) \n\nType here: ").lower().strip()
        if meal_files == "list": 
            print(f"\nList of ingredients:\n{w_dict}\n")
            meal_files = None
        elif meal_files == 'cost': 
            print(w_dict)
            for idx1, ingredient in enumerate(w_dict):
                for idx2, cost in enumerate(x_dict):
                    if idx1 == idx2:
                        print(f"\n{ingredient} Cost Per Serving:\n{cost}\n")
            meal_files = None
        elif meal_files == 'servings':
            for idx1, ingredient in enumerate(w_dict):
                for idx3, serving in enumerate(y_dict):
                    if idx1 == idx3:
                        print(f"\nAmount of {ingredient} servings used in {meal_folder}:\n{serving}\n ")
            meal_files = None
        elif meal_files == 'total cost':
            print(f"\nTotal Cost of {meal_folder}:\n{total}\n")
            meal_files = None
        elif meal_files == 'all info':
            print("Now listing all information...\n")
            print(f"\nList of ingredients:\n{w_dict}\n")
            for idx1, ingredient in enumerate(w_dict):
                for idx2, cost in enumerate(x_dict):
                    for idx3, serving in enumerate(y_dict):
                        if idx1 == idx2 == idx3:
                            print(f"{ingredient} Cost Per Serving:\n{cost}\n")
                            print(f"Amount of {ingredient} servings used in {meal_folder}:\n{serving}\n ")
            print(f"Total Cost of {meal_folder}:\n{total}\n")
            meal_files = None 
        elif meal_files == 'main menu':
            print("\nGoing to Main Menu...\n")
            initiation()
        else: 
            print("Sorry. I don't have autocorrect yet so I have no idea what youre saying.")
            meal_files = None
        # To calculate the ingredient per serving and add it to the dictionary. 
def foodCalculator(w, x, y, z):
    print(w, x, y, z) # Jul 8 Note: There are still issuse here. It does not fix the ingredient's info if incorrectly inputted. 
    user_ingredient_name = None
    user_ingredient_price = None
    user_ingredient_serving = None
    

    while user_ingredient_name == None:

        user_ingredient_name = input("Name: ")
        user_ingredient_price = input("Cost: ")
        user_ingredient_serving = input("Total serving: ")

        cost_per_serving = float(user_ingredient_price) / float(user_ingredient_serving)
        user_choice_of_serving = float(input("How many servings are you putting in? "))
        total_cost_of_serving = cost_per_serving * user_choice_of_serving

        if user_ingredient_name not in w:
            w.append(user_ingredient_name)
        if cost_per_serving not in x:
            x.append(cost_per_serving)
        if user_ingredient_serving not in y:
            y.append(user_choice_of_serving)
        if total_cost_of_serving not in z:
            z.append(total_cost_of_serving)

        d = (f"\nName of ingredient: {user_ingredient_name} \nPrice/Total Serving: {cost_per_serving} \nAmount of servings used: {user_choice_of_serving} \nTotal cost per use: {total_cost_of_serving}\n")
        isCorrect = None
        while isCorrect == None:
            isCorrect = input(f"Is the following correct: \n{d}\n(Type Y or N): ").lower()
            print(w)
            print(x)
            print(y)
            print(z)

            if isCorrect == "n":
                foodCalculator(w, x, y, z)
            elif isCorrect == "y":
                all_done = None
                while not all_done:
                    all_done = input("Is that all the ingredients for this meal (Y/N)?: ").lower() 
                    if all_done == "y":
                        print("Heading over to the 'folder and file' function")
                        meal_total_cost = sum(z)
                        createFolderandFile(w, x, y, z, meal_total_cost) # (w, x, y, z) will help transfer over ingredient data to createFolderandFile() function
                    elif all_done == 'n':
                        print("Gotcha. Lets add some more ingredients!")
                        foodCalculator(w, x, y, z)
                    else: 
                        print("Sorry. Idk what you said. Maybe a grammatical error? Please try again.")
                        all_done = None
            else:
                print("Invalid input. Try again")
                isCorrect = None
        return d


# To create meal folders and ingredient files 
# Note to self: by setting parameters, it can help transfer data from one function to another if needed
def createFolderandFile(w, x, y, z, total):

    d = {
    "Name of ingredient(s): ": w, 
    "Cost per serving: ": x, 
    "Amount of servings used: " : y, 
    "Total cost per use: " : z
    }


    print(d)
    # This is for now; still have to find a way to get the sum from "Total cost per serving" of all ingredients
    tempmealname = input("What is the name of your meal?: ").strip()
    mealname = tempmealname + " " + "meal"
    try:
        os.mkdir(mealname)
    except OSError:
        print(f"\n{mealname} folder could not be created. Please check Documents if it exists already\n")
        createFolderandFile(w, x, y, z, total)
    else:
        print(f"\n{mealname} folder was successfully made. Now adding ingredients info into the folder\n")
    
    os.chdir(mealname) # Goes to the mealname folder
    pickle.dump(d, open("ingredients","wb")) # Dumps all the ingredients data
    os.chdir(directory_Food_Calculator) # Goes back to the Food Calculator folder
    print (f"The sum of your {mealname} is {total}")
       

    
    choose_a_function = None
    while not choose_a_function:
        choose_a_function = input("What would you like to do? Add more meals (type more) or get meal list? (type meals) or end program (type end)?: ").lower()
        if choose_a_function == "more":
            foodCalculator(w, x, y, z)
            choose_a_function = None
        elif choose_a_function == "meals":
            meals()
            choose_a_function = None
        elif choose_a_function == "end":
            return ("Alright. Have a good day!")
        else:
            print("Invalid input. Try again")
            choose_a_function = None


def initiation():
    os.chdir(original_pathway)
    if directory_Food_Calculator not in os.listdir(original_pathway):
        print("Food Calculator folder not found. Creating new Food Calculator folder...\n")
        os.mkdir(directory_Food_Calculator)
        print(os.listdir())

    print(os.getcwd())
    if os.getcwd() != directory_Food_Calculator:
        os.chdir(directory_Food_Calculator)
        print(os.getcwd())
    
            
    initiateProgram = None
    while not initiateProgram:
        initiateProgram = input("How can I help you? (Type either food calculator or meals or end program): ").lower()
        if initiateProgram == "food calculator":
            print("Cool! Let's get started.")
            foodCalculator(w, x, y, z)
        elif initiateProgram == "meals":
            meals()
            initiateProgram = None
        elif initiateProgram == 'end program':
            return ("Alright, ending program. Till next time!")
        else:
            print("Sorry. I'm a computer with OCD; you got to type it out right. What was that again?")
            initiateProgram = None


# Just for good habits
if __name__ == "__main__":
    initiation()