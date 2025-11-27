#BreachBot Sample Project
breachYear = 2019

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the Facebook data breach.")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, or (c) I would like to hear your reflection.")
  topic = input()

  if topic.lower() == "a":
    print("530 million users in 106 countries, FacebookPhone numbers, full names, locations, some email addresses, and other details from user profiles were posted to an amateur hacking ")

  elif topic.lower() == "b":
    print("In July 2019, months before patching up the aforementioned issue, Facebook reached a $5 billion settlement with the U.S. Federal Trade Commission for violating an agreement with the agency to protect user privacy.")

  elif topic.lower() == "c":
    break

  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")

  input("Press enter to continue\n")

#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#share my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to CIA Triad (b) my reaction, (c) my advice, or (d) none.")
  topic = input()

  if topic.lower() == "a":
    print("This data breach connects to confidentiality because Facebook data breach, unauthorized access to user data compromised the confidentiality of personal information, violating the principle of keeping data private and secure.")

  elif topic.lower() == "b":
    print("I disagree with the organization's response because I think facebook should have implemented stronger security measures to protect user data.")

  elif topic.lower() == "c":
    print("I would convince victims to take action by emphasizing the importance of securing their personal information. My advice would be to prioritize personal cybersecurity, stay vigilant for any unusual activities, and utilize available security features.")

  elif topic.lower() == "d":
    break

  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")

  input("Press enter to continue\n")

  print("Thanks for chatting with me, and I hope you learned something new!")
  
#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")
