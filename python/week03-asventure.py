
answer = ""

while answer != "burrito" and answer != "apple" and answer != "sleep":
  answer = input("""You walk to the fridge in the middle of the night to pick a snack.
You open the fridge and only find a left-over BURRITO and an APPLE; or you can go back to SLEEP.
Which one do you pick?
""")
  answer = answer.lower()
  print()

if answer == "burrito":
  while answer != "hospital" and answer != "sleep":
    answer = input("""You eat it.
But as soon as you eat the last bite, you feel it, the burrito was spoiled!
You have to go to the hospital and get an IV drip for 3 days.
Do you want to go to the HOSPITAL or try to SLEEP it off?
  """)
    answer = answer.lower()
    print()
  if answer == "hospital":
    while answer != "work" and answer != "borrow":
      answer = input("""You go to the hospital and get an IV drip for 3 days.
You feel better after the 3 days, but you have to pay a lot of money for the hospital bill.
Do you want to WORK extra hours to pay the bill or BORROW money from your friend?
  """)
      answer = answer.lower()
      print()
    if answer == "work":
      print("""You work extra hours to pay the bill.
You pay off the bill in 2 months and feel proud of yourself for being responsible.
You have learned your lesson and never eat spoiled food again.
  """)
    else:
      print("""You borrow money from your friend to pay the bill.
Your friend is very understanding and doesn't ask you to pay him back.
You feel grateful for having such a good friend and promise to be more careful with food in the future.
  """)
  
  else:
    while answer != "laxative" and answer != "hospital":
      answer = input("""You try to sleep it off, but you end up feeling worse and worse.
You wake up the next morning feeling very sick.
Do you look for a LAXATIVE in the fridge or go to the HOSPITAL?
  """)
      answer = answer.lower()
      print()
    if answer == "laxative":
      print("""You find a laxative in the fridge and take it.
It works and you feel better after a few hours.
You learn your lesson and never eat spoiled food again.
""")
    else:
      print("""You go to the hospital and get an IV drip for 3 days.
You feel better after the 3 days, but you have to pay a lot of money for the hospital bill.
You learn your lesson and never eat spoiled food again.
""")
elif answer == "sleep":
  while answer != "look" and answer != "go":
    answer = input("""You go back to sleep and wake up the next morning feeling great!
You are very hungry. Do you LOOK for something in the fridge or GO out to get breakfast?
  """)
    answer = answer.lower()
    print()
  if answer == "look":
    print("""You look in the fridge and find some leftovers from last night.
You eat the leftovers and have a great day!
  """)
  else:
    print("""You go out to get breakfast and find a nice cafe nearby.
You order a delicious breakfast and have a great day!
  """)
else:
  while answer != "eat" and answer != "throw":
    answer = input("""You eat the apple.
It tastes a little bit off, but you don't feel sick.
You go back to sleep and wake up the next morning feeling great!
You go look for the burrito for breakfast.
Do you want to EAT the burrito or THROW it away?
  """)
    answer = answer.lower()
    print()
  if answer == "eat":
    while answer != "take" and answer != "ignore":
      answer = input("""You eat the burrito for breakfast.
As soon as you eat the last bite, you feel it, the burrito was spoiled!
You find a laxative in the fridge.
Do you want to TAKE the laxative or IGNORE it?
  """)
      answer = answer.lower()
      print()
    if answer == "take":
      print("""You take the laxative and it works!
  """)
    else:
      print("""You ignore the laxative and end up having a very bad day.
  """)
  else:
    while answer != "order" and answer != "cook":
      answer = input("""You throw the burrito away.
Do you ORDER a pizza for breakfast or COOK something yourself?
  """)
      answer = answer.lower()
      print()
    if answer == "order":
      print("""You order a pizza for breakfast and it arrives in 30 minutes.
You enjoy your pizza and have a great day!
  """)
    else:
      print("""You cook something yourself and it turns out to be delicious!
You feel proud of yourself for being able to cook and have a great day!
  """)
