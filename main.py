def main():
    username = input("What's your name?")
    print(f"Hello, {username}.  It nice to meet you.")
    age = int(input("If it wouldn't be too much to ask, how old are you?"))
    print(f"{age}?!  Really?!  You look great!")
    bday = input("Did you have your birthday yet this year?")
    if bday == "no":    
        year_100 = 2025 + (99 - age)
    elif bday == "yes":
        year_100 = 2025 + (100 - age)
    print(f"Did you know you will be 100 in the year {year_100}?  That's pretty neat, huh?")

main()
