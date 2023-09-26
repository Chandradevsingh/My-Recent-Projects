#string concatenation (aka How to put strings together)
#suppose we want to create a string that says "subscribe to _____"
# youtuber = "Dev Chauhan" #some string variable

# #a few ways to do this
# print("subscribe to "+ youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")


# adj = input("Adjective: ")
# verb1 = input("Verb: ")
# verb2 = input("verb: ")
# famous_person = input("Famous Person: ")
# madlibs = f"Computer programming is so {adj}! It makes me so excited all the time because \
# i love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"



# print(madlibs)

Noun1 = input("Noun : ")
Noun2 = input("Noun : ")
Noun3 = input("Noun : ")
Noun4 = input("Noun : ")
Noun5 = input("Noun : ")
Noun6 = input("Noun : ")
Noun7 = input("Noun : ")
Noun8 = input("Noun : ")
plural_noun1 =  input("Plural Noun : ")
adjective1 = input("Adjective : ")
adjective2 = input("Adjective : ")
adjective3 = input("Adjective : ")
adjective4 = input("Adjective : ")
adjective5 = input("Adjective : ")
verb1 = input("Verb : ")
place1 = input("Place : ")
place2 = input("Place : ")
Color1 = input("Color : ")
Animal1 = input("Animal : ")
food1 = input("Food : ")
Unit_of_time1 = input("Unit of Time : ")
City1 = input("City : ")
City2 = input("City : ")
Mode_of_transportation1 = input("Mode of Transportation : ")
Emotion1 = input("Emotion : ")

madlibs = f"""Title: A Day at the {Noun1}  
Once upon a time in {City1}, I decided to have an adventurous day at the {Noun2}. As I stepped out of my {Mode_of_transportation1}, I couldn't help but notice the {adjective1} sky above me.
I started my day by exploring the {place1} where I stumbled upon a {Noun3} that seemed out of place. I picked it up and noticed a {Color1} glow emanating from it. It felt {adjective2} to the touch.
With the mysterious {Noun4} in my pocket, I continued my journey to the {Noun5}. There, I encountered a friendly {Animal1}, who offered to be my tour guide. We embarked on a {adjective3} adventure together, exploring the {Noun6} and discovering hidden {plural_noun1} along the way.
As the sun began to set, I found the perfect spot to {verb1} and enjoy a {adjective4} picnic. I feasted on {food1} while watching the {Noun7} go by.
With a heart full of {Emotion1}, I realized that this had been the most {adjective5} day of my life. I headed back to {City2} with memories that would last a {Unit_of_time1} and the {Noun8} that had made it all possible."""

print(madlibs)