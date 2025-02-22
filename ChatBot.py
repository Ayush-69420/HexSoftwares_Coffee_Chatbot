# Function to print an error message for invalid input
def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

# Function to get the size of the drink from the user
def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
    
    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:
        print_message()
        return get_size()

# Function to get the type of drink from the user
def get_drink_type():
    res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
    
    if res == 'a':
        return 'brewed coffee'
    elif res == 'b':
        return 'mocha'
    elif res == 'c':
        return order_latte()
    else:
        print_message()
        return get_drink_type()

# Function to order a latte with a specific type of milk
def order_latte():
    res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')
    
    if res == 'a':
        return 'latte'
    elif res == 'b':
        return 'non-fat latte'
    elif res == 'c':
        return 'soy latte'
    else:
        print_message()
        return order_latte()

# Function to ask for additional options like cup preference
def extra_options():
    res = input("Would you like a plastic cup or did you bring your own reusable cup? \n[a] I'll need a cup. \n[b] Brought my own! \n> ")
    
    if res == 'a':
        print("Okay, no problem! We'll get you a plastic cup.")
    elif res == 'b':
        print("Great! We'll fill up your reusable cup.")
    else:
        print_message()
        return extra_options()

# Main function to run the coffee bot
def coffee_bot():
    # Print a welcome message
    print("Welcome to the cafe!")
    # Get the size of the drink from the user
    size = get_size()
    # Get the type of drink from the user
    drink_type = get_drink_type()
    # Ask for additional options
    extra_options()
    # Prompt the user for their name
    name = input("Can I get your name please? \n> ")
    # Print the final order
     # Print the final order
    print(f"Alright, that's a {size} {drink_type}!")
    # Thank the user and confirm the order
    print(f"Thanks, {name}! Your drink will be ready shortly.")
  


  # Call the main function to start the coffee bot
coffee_bot()