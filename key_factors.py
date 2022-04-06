import time
import os
import openai

from new_topic_deep_dive import main

# API key for OpenAI
openai.api_key = "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"

# Get topic from user
topic = input("Enter a topic: ")

"""
Generates goals for a given topic

Parameters:
    topic (str): The topic for which to generate goals

Returns:
    str: The generated goals for the given topic
"""

def generate_goals(topic):
    return generate_goals_openai(topic)

    """
    Generates ingredients for a given topic

    Parameters:
        topic (str): The topic for which to generate goals

    Returns:
        list: The generated ingredients for the given topic
    """

def generate_ingredients(topic):
    return generate_ingredients_openai(topic)


def generate_goals_openai(topic):
    """
    Generates goals for a given topic

    Parameters:
        topic (str): The topic for which to generate goals

    Returns:
        str: The generated goals for the given topic
    """
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


def generate_ingredients_openai(topic):
    """
    Generates ingredients for a given topic

    Parameters:
        topic (str): The topic for which to generate goals

    Returns:
        list: The generated ingredients for the given topic
    """
    return break_goals_into_ingredients(generate_goals(topic))



def break_goals_into_ingredients(goals):
    """
    Breaks goals into ingredients

    Parameters:
        goals (str): The goals to break into ingredients

    Returns:
        list: The ingredients for the given goals
    """
    # Break goals into ingredients
    ingredients = []
    # split goal by \n
    goals = goals.split("\n")
    for goal in goals:
        ingredients.append(goal)
    return ingredients

def ask_user_to_select_ingredients(ingredients):
    """
    Asks the user to select one or more of the ingredients

    Parameters:
        ingredients (list): The ingredients to select from

    Returns:
        list: The selected ingredients for the given ingredients
    """
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
    """
    Prints the user input

    Parameters:
        ingredient (str): The ingredient to print for the given ingredient
    """
    # Print the user input for the given ingredient
    print("")
    print("You selected: "+ingredient)
    print("")

selected_ingredients = ask_user_to_select_ingredients(generate_ingredients(topic))


print("")
print("Generating key concepts for "+topic+"...")
def generate_key_concepts(topic):
    """
    Generates key concepts for a given topic.
    """
    
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Write a recipe based on these ingredients and instructions:\n\nNeural Networks\n\nKey Concepts\n\n-Used to model complex patterns in data.\n-Processing nodes, or neurons, that can learn to recognize patterns of input data.\n-Image recognition, pattern recognition, and classification tasks.\n-Neural networks can be trained using a variety of different training algorithms, including backpropagation, stochastic gradient descent, and evolutionary algorithms.\n\n\nWrite a recipe based on these ingredients and instructions:\n\nInterior Design\n\nKey Concepts\n\n-The art and science of improving the interior of a building to achieve a healthier and more aesthetically pleasing environment for the people using the space.\n-Interior design is a multifaceted profession that includes conceptual development, space planning, site inspections, programming, research, communicating with the stakeholders of a project, construction management, and execution of the design.\n\n\nWrite a recipe based on these ingredients and instructions:\n\nSocial Media\n\nKey Concepts\n\n-Web-based and mobile technologies that turn communication into an interactive dialogue.\n-Builds relationships and connects people.\n-Creates communities of people with similar interests.\n-People use social media to share information, ideas, personal messages, and other content.\n\n\nWrite a recipe based on these ingredients and instructions:\n\nERP\n\nKey Concepts\n\n-Enterprise resource planning.\n-A software system that helps businesses manage their finances, inventory, and other business operations.\n-ERP systems are used by businesses of all sizes, from small businesses to large enterprises.\n\n\nWrite a recipe based on these ingredients and instructions:\n\nPersonal Finances\n\nKey Concepts\n\n-The process of planning and managing your personal finances.\n-Includes budgeting, saving, and investing.\n-Personal finance is a lifelong process.\n\n\nWrite a recipe based on these ingredients and instructions:\n\n"+topic+"\n\nKey Concepts\n\n",
    temperature=0.3,
    max_tokens=120,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    
    return response.choices[0].text

# print(generate_key_concepts(topic))

print(generate_key_concepts(topic))
# Generate key algorithms of topic
print("")
print("Generating key algorithms for "+topic+"...")
print("")
def generate_key_algorithms(topic):
    """
    Generates key algorithms for the given topic.

    Parameters:
        topic (str): The topic to generate key algorithms for.

    Returns:
        str: The generated key algorithms.
    """

    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="# Key Equations and Algorithms\n\n## Machine Learning\n\n### Perceptron Learning Algorithm:\n### Equation:\nW(t+1) = W(t) + alpha * (d - y(t)) * x(t)\n### Algorithm:\n1. Initialize the weights to 0 or small random numbers\n2. For each training example x(t):\n    1. Compute the output value y(t)\n    2. Update the weights\n\n### Support Vector Machine Learning Algorithm:\n### Equation:\nW(t+1) = W(t) + alpha * (d - y(t)) * x(t)\n### Algorithm:\n1. Initialize the weights to 0 or small random numbers\n2. For each training example x(t):\n    1. Compute the output value y(t)\n    2. Update the weights\n\n### Logistic Regression Learning Algorithm:\n### Equation:\nW(t+1) = W(t) + alpha * (d - y(t)) * x(t)\n### Algorithm:\n1. Initialize the weights to 0 or small random numbers\n2. For each training example x(t):\n    1. Compute the output value y(t)\n    2. Update the weights\n\n\n\n## Interior Design\n\n### Fibonnaci Sequence:\n### Equation:\nF(n) = F(n-1) + F(n-2)\n### Algorithm:\n1. Initialize the first two terms of the sequence\n2. For each term after the first two:\n    1. Compute the next term\n    2. Update the first an\n### Equation:\nP = M * (1 - (1 / (1 + r)^n))\n### Algorithm:\n1. Determine the mortgage second terms\n\n### Golden Ratio:\n### Equation:\nphi = (1 + sqrt(5)) / 2\n### Algorithm:\n1. Compute the value of phi\n2. Use phi to determine the proportions of a design\n\n\n\n## Real Estate\n\n### Mortgage Payment:\n### Equation:\nM = P * (r(1 + r)^n) / ((1 + r)^n - 1)\n### Algorithm:\n1. Determine the loan amount (P)\n2. Determine the interest rate (r)\n3. Determine the loan term (n)\n4. Compute the mortgage payment (M)\n\n### Mortgage Interest:\n### Equation:\nI = M * r * n\n### Algorithm:\n1. Determine the mortgage payment (M)\n2. Determine the interest rate (r)\n3. Determine the loan term (n)\n4. Compute the mortgage interest (I)\n\n### Mortgage Principal:\n### Equation:\nP = M * (1 - (1 / (1 + r)^n))\n### Algorithm:\n1. Determine the mortgage payment (M)\n2. Determine the interest rate (r)\n3. Determine the loan term (n)\n4. Compute the mortgage principal (P)\n\n### Loan Amount:\n### Equation:\nP = M / ((r(1 + r)^n) / ((1 + r)^n - 1))\n### Algorithm:\n1. Determine the mortgage payment (M)\n2. Determine the interest rate (r)\n3. Determine the loan term (n)\n4. Compute the loan amount (P)\n\n### Loan Term:\n### Equation:\nn = log(M / (M - P * r)) / log(1 + r)\n### Algorithm:\n1. Determine the mortgage payment (M)\n2. Determine the interest rate (r)\n3. Determine the loan amount (P)\n4. Compute the loan term (n)\n\n### Loan Interest Rate:\n### Equation:\nr = (M / P - 1) / n\n### Algorithm:\n1. Determine the mortgage payment (M)\n2. Determine the loan amount (P)\n3. Determine the loan term (n)\n4. Compute the interest rate (r)\n\n\n\n## Stock Market\n\n### Stock Price:\n### Equation:\nP = E / (1 + r)\n### Algorithm:\n1. Determine the expected return (E)\n2. Determine the required return (r)\n3. Compute the stock price (P)\n\n### Expected Return:\n### Equation:\nE = P * (1 + r)\n### Algorithm:\n1. Determine the stock price (P)\n2. Determine the required return (r)\n3. Compute the expected return (E)\n\n### Required Return:\n### Equation:\nr = (E / P) - 1\n### Algorithm:\n1. Determine the expected return (E)\n2. Determine the stock price (P)\n3. Compute the required return (r)\n\n### Dividend Yield:\n### Equation:\nDY = D / P\n### Algorithm:\n1. Determine the dividend (D)\n2. Determine the stock price (P)\n3. Compute the dividend yield (DY)\n\n### Capital Gains Yield:\n### Equation:\nCY = (P1 - P0) / P0\n### Algorithm:\n1. Determine the stock price at the beginning of the period (P0)\n2. Determine the stock price at the end of the period (P1)\n3. Compute the capital gains yield (CY)\n\n### Total Return:\n### Equation:\nTR = DY + CY\n### Algorithm:\n1. Determine the dividend yield (DY)\n2. Determine the capital gains yield (CY)\n3. Compute the total return (TR)\n\n\n\n## Roth IRA\n\n### Future Value:\n### Equation:\nFV = PV * (1 + r)^n\n### Algorithm:\n1. Determine the present value (PV)\n2. Determine the interest rate (r)\n3. Determine the number of periods (n)\n4. Compute the future value (FV)\n\n### Present Value:\n### Equation:\nPV = FV / (1 + r)^n\n### Algorithm:\n1. Determine the future value (FV)\n2. Determine the interest rate (r)\n3. Determine the number of periods (n)\n4. Compute the present value (PV)\n\n### Interest Rate:\n### Equation:\nr = (FV / PV)^(1 / n) - 1\n### Algorithm:\n1. Determine the future value (FV)\n2. Determine the present value (PV)\n3. Determine the number of periods (n)\n4. Compute the interest rate (r)\n\n### Number of Periods:\n### Equation:\nn = log(FV / PV) / log(1 + r)\n### Algorithm:\n1. Determine the future value (FV)\n2. Determine the present value (PV)\n3. Determine the interest rate (r)\n4. Compute the number of periods (n)\n\n\n\n\n## Color Wheel\n\n### Color Scheme:\n### Equation:\nComplementary Colors: C = (255 - R, 255 - G, 255 - B)\n\nAnalogous Colors: A = (R + dr, G + dg, B + db)\n\nSplit-Complementary Colors: SC = (R + dr, G - dg, B - db)\n\nTriadic Colors: T = (R + dr, G + dg, B - db)\n\nTetradic Colors: TT = (R + dr, G - dg, B + db)\n\nSquare Colors: S = (R + dr, G + dg, B + db)\n\n### Algorithm:\n1. Determine the color scheme\n2. Determine the starting color (R, G, B)\n3. Determine the color difference (dr, dg, db)\n4. Compute the complementary color (C), analogous color (A), split-complementary color (SC), triadic color (T), tetradic color (TT), or square color (S)\n\n\n\n## "+topic+"\n\n###",
    temperature=0.3,
    max_tokens=350,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    return response.choices[0].text

print(generate_key_algorithms(topic))


print("")
print("Generating key concepts for "+topic+"...")
def generate_key_concepts(topic):
    """
    Generates key concepts for a given topic.
    """
    
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Write a recipe based on these ingredients and instructions:\n\nNeural Networks\n\nKey Concepts\n\n-Used to model complex patterns in data.\n-Processing nodes, or neurons, that can learn to recognize patterns of input data.\n-Image recognition, pattern recognition, and classification tasks.\n-Neural networks can be trained using a variety of different training algorithms, including backpropagation, stochastic gradient descent, and evolutionary algorithms.\n\n\nWrite a recipe based on these ingredients and instructions:\n\nInterior Design\n\nKey Concepts\n\n-The art and science of improving the interior of a building to achieve a healthier and more aesthetically pleasing environment for the people using the space.\n-Interior design is a multifaceted profession that includes conceptual development, space planning, site inspections, programming, research, communicating with the stakeholders of a project, construction management, and execution of the design.\n\n\nWrite a recipe based on these ingredients and instructions:\n\nSocial Media\n\nKey Concepts\n\n-Web-based and mobile technologies that turn communication into an interactive dialogue.\n-Builds relationships and connects people.\n-Creates communities of people with similar interests.\n-People use social media to share information, ideas, personal messages, and other content.\n\n\nWrite a recipe based on these ingredients and instructions:\n\nERP\n\nKey Concepts\n\n-Enterprise resource planning.\n-A software system that helps businesses manage their finances, inventory, and other business operations.\n-ERP systems are used by businesses of all sizes, from small businesses to large enterprises.\n\n\nWrite a recipe based on these ingredients and instructions:\n\nPersonal Finances\n\nKey Concepts\n\n-The process of planning and managing your personal finances.\n-Includes budgeting, saving, and investing.\n-Personal finance is a lifelong process.\n\n\nWrite a recipe based on these ingredients and instructions:\n\n"+topic+"\n\nKey Concepts\n\n",
    temperature=0.3,
    max_tokens=120,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    
    return response.choices[0].text

print(generate_key_concepts(topic))

print("")
def format_goal(selected_ingredients):
    goal = selected_ingredients[0]
    goal = goal.replace('- ', '').replace('-', '')
    return goal


def generate_key_strategies(topic,goal):
    """
    Generates key strategies for a given topic and goal. 
    """
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="# Real Estate:\n\nTo make money\n\n## Key Strategies:\n\n1. **Find a good location.** Look for a location that is in demand, has good potential for appreciation, and is in a good school district.\n2. **Buy a fixer-upper.** Look for a property that needs some work but has good bones. By fixing it up, you can add value to the property and make a good profit when you sell.\n3. **Invest in rental property.** Rental property can be a great way to make money, especially if you invest in a location that is in demand.\n4. **Flip houses.** Buying a property, fixing it up, and then selling it for a profit can be a great way to make money in the real estate market.\n5. **Get a good real estate agent.** A good real estate agent will be able to help you find the right property, negotiate the best price, and get the best deal on your investment.\n\n\n\n# Interior Design:\n\nTo incorporate the client's style and needs\n\n## Key Strategies:\n\n1. **Create a mood board.** This will help you get an idea of the overall style and feel of the space.\n2. **Choose a color scheme.** This will help you create a cohesive look.\n3. **Select furniture and accessories.** This will help you pull the space together.\n4. **Edit and accessorize.** This will help you create a space that is both stylish and functional.\n\n\n\n# Personal Fashion:\n\nTo be well-dressed\n\n## Key Strategies:\n\n1. **Dress for your body type.** Not all styles will look good on everyone. Find styles that flatter your figure and make you feel confident.\n2. **Find your own style.** Don't try to copy someone else's style. Find what works for you and what makes you feel good.\n3. **Invest in quality pieces.** Buy fewer pieces that are well-made and will last longer.\n4. **Accessorize.** Accessories can make an outfit. Choose wisely and don't go overboard.\n5. **Edit your closet.** Get rid of clothes that you don't wear or that don't fit. This will make getting dressed easier and help you build a wardrobe you love.\n\n\n\n# Creating a mood board:\n\nTo find inspiration for your project\n\n## Key Strategies:\n\n1. **Find inspiration.** Look for images that inspire you and that capture the feeling you want for your project.\n2. **Create a collage.** Arrange your images in a way that is pleasing to the eye.\n3. **Edit your board.** Remove any images that don't fit with the overall feeling you are going for.\n4. **Save your board.** Save your board so you can refer back to it when you are working on your project.\n\n\n\n# Choosing a color scheme:\n\nTo choose a sad color scheme\n\n## Key Strategies:\n\n1. **Choose a color palette.** Pick a few colors that you want to use in your space.\n2. **Test your colors.** Paint a sample of each color on a piece of paper or on the wall to see how they look in the space.\n3. **Edit your colors.** If you don't like the way the colors look together, choose a different palette.\n4. **Save your colors.** Once you have a color scheme you like, save it so you can refer back to it when you are working\n\n\n\n# Selecting furniture and accessories:\n\nTo choose furniture and accessories that fit your space\n\n## Key Strategies:\n\n1. **Measure your space.** This will help you know what size furniture and accessories will fit in your space.\n2. **Choose furniture that is versatile.** Look for pieces that can be used in multiple ways.\n3. **Accessorize.** Use accessories to add color, texture, and interest to your space.\n4. **Edit your selections.** If you don't love it, don't put it in your space.\n\n\n\n# "+topic+":\n\n"+goal+"\n\n## Key Strategies:\n\n",
        temperature=0.3,
        max_tokens=120,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    return response.choices[0].text



def generate_key_skills(topic):

    """
    Generates key skills for a given topic.
    """
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="# Key Skills - Interior Design\n\n- Space Planning\n- Color Schemes\n- Furniture Selection\n- Project Management\n\n\n# Key Skills - ERP Implementation\n\n- Business Process Mapping\n- System Configuration\n- Training\n- Change Management\n\n\n# Key Skills - Neural Networks\n\n- Data Pre-Processing\n- Neural Network Architectures\n- Hyperparameter Tuning\n- Model Evaluation\n\n\n# Key Skills - Event Planning\n\n- Budgeting\n- Venue Selection\n- Vendor Management\n- Event Coordination\n\n\n# Key Skills - Accounting\n\n- Financial Reporting\n- Tax Preparation\n- Accounts Payable/Receivable\n- Bookkeeping\n\n\n# Key Skills - Financial Reporting\n\n- Financial Analysis\n- Financial Modeling\n- Variance Analysis\n- Financial Statement Preparation\n\n\n# Key Skills - Networking in the NBA\n\n- Relationship Building\n- Strategic Planning\n- Business Development\n- Negotiation\n\n\n# Key Skills - Nutrition\n\n- Dietary Assessment\n- Nutrition Education\n- Meal Planning\n- Supplement Recommendations\n\n# Key Skills - Python coding\n\n- Data structures\n- Algorithms\n- Object Oriented Programming\n- Functional Programming\n\n# Key Skills - Real Estate\n\n- Property Valuation\n- Market Analysis\n- Investment Analysis\n- Negotiation\n\n\n# Key Skills - Proposal Writing\n\n- Needs Assessment\n- Solution Design\n- Cost Analysis\n- Writing and Editing\n\n# Key Skills - "+topic,
    temperature=0.3,
    max_tokens=120,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    
    return response.choices[0].text


def generate_key_strategies_and_skills(topic, selected_ingredients):
    goal = format_goal(selected_ingredients)
    print("Generating key strategies for "+topic+"...")
    print(generate_key_strategies(topic,goal))
    print("")
    print("Generating key skills for "+topic+"...")
    print(generate_key_skills(topic))

generate_key_strategies_and_skills(topic, selected_ingredients)


# if __name__ == "__main__":
#     generate_goals()