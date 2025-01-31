# CS8 Project 1 
# Student Name: Luz Jauregui
# A3! Personality Quiz: What Mankai Company Troupe would you be in?

spring = 0
summer = 0
autumn = 0
winter = 0

print("A3! Personality Quiz: What Mankai Company Troupe would you be in?\n")
print("Mankai Company is a theater company famous for its concept of four different troupes, one for each season, which all have their own themes that range from comedy acts to action-packed stage plays. \nFind out what troupe you would be in based on your personality with this quiz. The quiz will consist of 10 multiple choice questions.")

quiz = input("Would you like to take the personality quiz? \n")
print()

if quiz == "yes" or quiz == "Yes":
    
    print("Welcome to the Mankai Company Personality Quiz!\n")
    print("Answer the following multiple-choice questions to find out which troupe suits you best!\n\n")

    print("Question 1. What's your ideal way to spend an afternoon?")
    print("\nA. A picnic at the park.\nB. A beach day with friends.\nC. Training for an intense competition.\nD. Stay home and watch a movie or your current favorite show")
    print()
    a1 = input("Answer: ")
    print()
    
    if a1 == "A" or a1 == "a":
        spring += 1
    elif a1 == "B" or a1 == "b":
        summer += 1
    elif a1 == "C" or a1 == "c":
        autumn += 1
    elif a1 == "D" or a1 == "d":
        winter += 1

    print("Question 2. What's your go-to aesthetic?\n")
    print("A. whimsicle and dreamy.\nB. bold and vibrant.\nC. edgy and striking.\nD. elegant and minimalist.")
    a2 = input("Answer: ")
    print()

    if a2 == "A" or a2 == "a":
        spring += 1
    elif a2 == "B" or a2 == "b":
        summer += 1
    elif a2 == "C" or a2 == "c":
        autumn += 1
    elif a2 == "D" or a2 == "d":
        winter += 1
          
    print("Question 3. What role do you usually play in a group?\n")
    print("A. The optimistic dreamer\nB. The life of the party\nC. The cool leader\nD. The wise, quiet supporter ")
    a3 = input("Answer: ")
    print()
    
    if a3 == "A" or a3 == "a":
        spring += 1
    elif a3 == "B" or a3 == "b":
        summer += 1
    elif a3 == "C" or a3 == "c":
        autumn += 1
    elif a3 == "D" or a3 == "d":
        winter += 1
        
    print("Question 4. What's your favorite genre of stories?\n")
    print("A. Classic fairytales with a magical twist\nB. Feel-good comedies that make you laugh out loud\nC. Action and thrilling adventures\nD. Emotional dramas that leave a lsating impact")
    a4 = input("Answer: ")
    print()
    
    if a4 == "A" or a4 == "a":
        spring += 1
    elif a4 == "B" or a4 == "b":
        summer += 1
    elif a4 == "C" or a4 == "c":
        autumn += 1
    elif a4 == "D" or a4 == "d":
        winter += 1
    
    print("Question 5. Which activity sounds most appealing to you?\n")
    print("A. Take a peaceful stroll through a flower garden\nB. Go with friends to a festival\nC. Play a competitive game with friends\nD. Writing poetry or journaling your thoughts")
    a5 = input("Answer: ")
    print()

    if a5 == "A" or a5 == "a":
        spring += 1
    elif a5 == "B" or a5 == "b":
        summer += 1
    elif a5 == "C" or a5 == "c":
        autumn += 1
    elif a5 == "D" or a5 == "d":
        winter += 1

    print("Question 6. How do you handle challenges? \n")
    print("A. Stay optimistic and trust things will work out\nB. Use humor and energy to keep spirits up\nC. Face them head-on with determination\nD. Analyze and approach with calm, logical thinking")
    a6 = input("Answer: ")
    print()

    if a6 == "A" or a6 == "a":
        spring += 1
    elif a6 == "B" or a6 == "b":
        summer += 1
    elif a6 == "C" or a6 == "c":
        autumn += 1
    elif a6 == "D" or a6 == "d":
        winter += 1
        
    print("Question 7. What's your favorite season?\n")
    print("A. Blossoming spring\nB. Hot, sunny summer\nC. Crisp, colorful autumn\nD. Calm snowy winter")
    a7 = input("Answer: ")
    print()

    if a7 == "A" or a7 == "a":
        spring += 1
    elif a7 == "B" or a7 == "b":
        summer += 1
    elif a7 == "C" or a7 == "c":
        autumn += 1
    elif a7 == "D" or a7 == "d":
        winter += 1

    print("Question 8. What's your best trait?\n")
    print("A. Kindness\nB. Lively\nC. Determined\nD. Thoughtfulness")
    a8 = input("Answer: ")
    print()

    if a8 == "A" or a8 == "a":
        spring += 1
    elif a8 == "B" or a8 == "b":
        summer += 1
    elif a8 == "C" or a8 == "c":
        autumn += 1
    elif a8 == "D" or a8 == "d":
        winter += 1

    print("Question 9. If you were in a performance, what role would you want to play?\n")
    print("A. The dreamy protagonist\nB. The comedic relief who brings joy to everyone\nC. The hero who saves the day\nD. The deep and emotional character")
    a9 = input("Answer: ")
    print()

    if a9 == "A" or a9 == "a":
        spring += 1
    elif a9 == "B" or a9 == "b":
        summer += 1
    elif a9 == "C" or a9 == "c":
        autumn += 1
    elif a9 == "D" or a9 == "d":
        winter += 1

    print("Question 10. Choose a color set:\n")
    print("A. Pastel colors\nB. Bright colors\nC. Dark warm colors\nD. Cool tone colors")
    a10 = input("Answer: ")
    print()

    if a10 == "A" or a10 == "a":
        spring += 1
    elif a10 == "B" or a10 == "b":
        summer += 1
    elif a10 == "C" or a10 == "c":
        autumn += 1
    elif a10 == "D" or a10 == "d":
        winter += 1


    if spring > summer and spring > autumn and spring > winter:
        print("You belong in Spring Troupe! 🌸\n")
        print("You're kind-hearted, creative, and optimistic!")
        print("You bring people together with your warm energy. You love classic and fairytale-like stories. You see the beauty in the world and believe in happy endings!" )

    elif summer > spring and summer > autumn and summer > winter:
        print("You belong in Summer Troupe! ☀️\n")
        print("You're lively, outgoing, and enthusiastic!")
        print("You thrive in fun, chaotic situations, and love to make others laugh. People admire your confidence and spontaneity, and you always know how to brighten the mood.")        

    elif autumn > spring and autumn > summer and autumn > winter:
        print("You belong in Autumn Troupe! 🍁\n") # \U0001F341 fall
        print("You're independent, focused, and resilient!")
        print("You love challenges and push yourself to be the best. Your cool and sometimes intimidating aura hides a deeply passionate side that shines when you're doing what you love.")

    elif winter > spring and winter > summer and winter > autumn:
        print("You belong in Winter Troupe! ❄️ \n") # \u2744 snowflake
        print("You're calm, introspective, and emotionally deep.")
        print("You appreciate beauty in the little things and often think before you speak. People find you mysterious but comforting, and your wisdom and grace leave a lasting impression.")

    elif spring == 0 and summer == 0 and autumn == 0 and winter == 0:
        print("Please try again later.")
        print("Reminder: To answer the question enter the corresponding letter.")
        
    elif spring == max(spring, summer, autumn, winter):
        if spring == summer:
            print("You could be in either Spring or Summer troupe!\n")
            
            print("You're kind-hearted, creative, and optimistic! Perfect for Spring Troupe! 🌸")
            print("You bring people together with your warm energy. You love classic and fairytale-like stories. You see the beauty in the world and believe in happy endings!\n" )
            print("But you're also lively, outgoing, and enthusiastic! Perfect for Summer Troupe! ☀️")
            print("You thrive in fun, chaotic situations, and love to make others laugh. People admire your confidence and spontaneity, and you always know how to brighten the mood.")        

        elif spring == autumn:
            print("You could be in either Spring or Autumn troupe!\n")
            
            print("You're kind-hearted, creative, and optimistic! Perfect for Spring Troupe! 🌸")
            print("You bring people together with your warm energy. You love classic and fairytale-like stories. You see the beauty in the world and believe in happy endings!\n" )
            print("You're also independent, focused, and resilient! Perfect for Autumn Troupe! 🍁")
            print("You love challenges and push yourself to be the best. Your cool and sometimes intimidating aura hides a deeply passionate side that shines when you're doing what you love.")

        elif spring == winter:
            print("You could be in either Spring or Winter troupe!\n")
            
            print("You're kind-hearted, creative, and optimistic! Perfect for Spring Troupe! 🌸")
            print("You bring people together with your warm energy. You love classic and fairytale-like stories. You see the beauty in the world and believe in happy endings!\n" )
            print("You're also calm, introspective, and emotionally deep. Perfect for Winter Troup[e! ❄️")
            print("You appreciate beauty in the little things and often think before you speak. People find you mysterious but comforting, and your wisdom and grace leave a lasting impression.")

    elif summer == max(spring, summer, autumn, winter):
        if summer == autumn:
            print("You could be in either Summer or Autumn troupe!\n")
            
            print("You're lively, outgoing, and enthusiastic! Perfect for Summer Troupe! ☀️")
            print("You thrive in fun, chaotic situations, and love to make others laugh. People admire your confidence and spontaneity, and you always know how to brighten the mood.\n")
            print("You're also independent, focused, and resilient! Perfect for Autumn Troupe! 🍁")
            print("You love challenges and push yourself to be the best. Your cool and sometimes intimidating aura hides a deeply passionate side that shines when you're doing what you love.")


        elif summer == winter:
            print("You could be in either Summer or Winter troupe!\n")
            print("You're lively, outgoing, and enthusiastic! Perfect for Summer Troupe! ☀️")
            print("You thrive in fun, chaotic situations, and love to make others laugh. People admire your confidence and spontaneity, and you always know how to brighten the mood.\n")        
            print("You're also calm, introspective, and emotionally deep. Perfect for Winter Troup[e! ❄️")
            print("You appreciate beauty in the little things and often think before you speak. People find you mysterious but comforting, and your wisdom and grace leave a lasting impression.")

    elif autumn == winter:
        print("You could be in either Autumn or Winter troupe!\n")
        print("You're independent, focused, and resilient! Perect for Autumn Troupe! 🍁")
        print("You love challenges and push yourself to be the best. Your cool and sometimes intimidating aura hides a deeply passionate side that shines when you're doing what you love.\n")
        print("You're also calm, introspective, and emotionally deep. Perfect for Winter Troup[e! ❄️")
        print("You appreciate beauty in the little things and often think before you speak. People find you mysterious but comforting, and your wisdom and grace leave a lasting impression.")

    #else:
        #print("Please try again later.")
        #print("Reminder: To answer the question enter the corresponding letter.")

else:
    print("Thank you for your consideration. Come back whenever you'd like to take the personality test! 😊")
    
