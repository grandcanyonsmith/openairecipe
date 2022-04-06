import os
import openai
from requests_toolbelt import user_agent

# API key for OpenAI
openai.api_key = "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"

# Get topic from user
topic = input("Enter a topic: ")

# Generate goals of topic
print("Generating key goals for "+topic+"...")
print("")
def generate_goals(topic):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="# Write a recipe based on these ingredients and instructions:\n\n## Neural Networks\n\n### Goals of Neural Networks:\n\n- Collect as much data as possible\n- Train a neural network to recognize patterns in the data\n- Use the neural network to make predictions or decisions\n\n\n## Write a recipe based on these ingredients and instructions:\n\n## Social Media\n\n### Goals of Social Media:\n\n- Gain as many followers as possible\n- Engage with followers regularly\n- Post content that is interesting and engaging\n\n\n## Write a recipe based on these ingredients and instructions:\n\n## ERP\n\n### Goals of ERP:\n\n- To provide a single, integrated system for managing all aspects of the business\n- To automate and streamline business processes\n- To provide real-time visibility into all aspects of the business\n\n\n## Write a recipe based on these ingredients and instructions:\n\n## Interior Design\n\n### Goals of Interior Design:\n\n- To create a functional and aesthetically pleasing space\n- To use space efficiently\n- To incorporate the client's style and needs\n\n\n## Write a recipe based on these ingredients and instructions:\n\n## Personal Finances\n\n### Goals of Personal Finances:\n\n- To save money\n- To invest money\n- To spend money wisely\n\n\n## Write a recipe based on these ingredients and instructions:\n\n## Roth ira\n\n### Goals of  Roth IRA:\n\n- To provide tax-free growth potential\n- To provide tax-free withdrawals in retirement\n- To provide flexibility and control over your retirement savings\n\n\n## Write a recipe based on these ingredients and instructions:\n\n## "+topic+"\n\n### Goals of "+topic+":\n\n",
        temperature=0.3,
        max_tokens=120,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    
    return response.choices[0].text


def generate_ingredients(topic):
    # Generate key concepts
    goals = generate_goals(topic)
    print("goals:", goals)
    print("")



def break_goals_into_ingredients(goals):
    # Break goals into ingredients
    ingredients = []
    # split goal by \n
    goals = goals.split("\n")
    for goal in goals:
        ingredients.append(goal)
    return ingredients

def ask_user_to_select_ingredients(ingredients):
    # Ask the user to select one or more of the ingredients
    print("")
    print("Select one or more of the ingredients:")
    for i in range(len(ingredients)):
        print(str(i+1)+". "+ingredients[i])
    print("")
    ingredient_numbers = input("Enter the numbers of the ingredients you want to select: ")
    ingredient_numbers = ingredient_numbers.split(",")
    selected_ingredients = []
    for ingredient_number in ingredient_numbers:
        ingredient_number = int(ingredient_number)
        selected_ingredients.append(ingredients[ingredient_number-1])
    return selected_ingredients

def print_user_input(ingredient):
    # Print the user input
    print("")
    print("You selected: "+ingredient)
    print("")

# print(generate_goals(topic))
# print(break_goals_into_ingredients(generate_goals(topic)))
selected_ingredients = ask_user_to_select_ingredients(break_goals_into_ingredients(generate_goals(topic)))[0]

selected_ingredients = selected_ingredients.replace("- ", "")

print(selected_ingredients)