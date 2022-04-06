import openai
openai.api_key = "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"

# Extracts topic data from a given text using OpenAI's GPT-3 API.
# The text is formatted to match the format of the training data.
# The text is then passed to the API, which returns a list of possible completions.
# The first completion is returned.
# @param topic: The topic to extract data from
# @param data: The text to extract data from
# @param num_tokens: The number of tokens to use
# @return: The extracted data as a string
def extract_topic_data(topic, data, num_tokens, num_tries):
    print("Fetching topic data...\n")
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=data + "\n\n\n"
               "Topic = " + topic + "\n\n\n"
               "What are 7 key points of " + topic + " that I should learn?\n"
               "1. What are the goals of " + topic + "?\n"
               "2. What are the key concepts " + topic + "?\n"
               "3. What are the key skills?\n"
               "4. What are the key strategies?\n"
               "5. What are the key resources?\n"
               "6. Examples\n"
               "7. What are the key equations used in " + topic + "?\n\n\n"
               "Example\n"
               "Goal:\n"
               "Correctly solve various types of financial equations.\n\n"
               "Key Concepts:\n"
               "Equations\n"
               "Algebra\n"
               "Solving for variables\n"
               "Financial concepts (interest, annuities)\n\n"
               "Key Skills:\n"
               "Solving Equations \n"
               "Manipulating\n"
               "Algebraic Expressions\n\n\n"
               "Use the Example format above to answer the topic questions for " + topic +":\n\n\n",
        temperature=0.4,
        max_tokens=num_tokens,
        top_p=1.0,
        frequency_penalty=0.8,
        presence_penalty=0.0
    )
    if response.choices[0].text == "" or response.choices[0].text == " ":
        return extract_topic_data(topic, data, num_tokens, num_tries + 1)
    else:
        return response.choices[0].text, num_tokens


# Extracts keywords from a given text using OpenAI's GPT-3 API.
# The text is formatted to match the format of the training data.
# The text is then passed to the API, which returns a list of possible completions.
# @param num_tokens: The number of tokens to use
# The first completion is returned.
# @param data: The text to extract keywords from.
# @return: The extracted keywords as a string
def extract_keywords(data, num_tokens, num_tries):
    print("Extracting keywords...\n")

    keywords = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Example Keywords:\n-Advancing the ball\n-Downs\n-Line of Scrimmage\n\n"
               "Extract keywords from the following text using the Example keywords format. Use hyphens for multi-word keywords:\n\n"
               + data + "\n\nKeywords:\n",
        temperature=0.42,
        max_tokens=num_tokens,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    if keywords.choices[0].text == "" or keywords.choices[0].text == " ":
        return extract_keywords(data, num_tokens, num_tries + 1)
    else:
        return keywords.choices[0].text, num_tokens

# Extracts keywords from a given text and returns them as a list. Removes punctuation and makes lowercase.
# @param data: The text to extract keywords from.
# @return: The extracted keywords as a list
def extract_keywords_list(data):
    keywords = set(x.strip('.,!?;-') for x in data.lower().split())  # Removes punctuation and makes lowercase.

    keywords_list = []
    for i in keywords:
        keywords_list.append(i)  # Adds each keyword to a list.

    return keywords_list





# Main function
def main():
    topic = input("Topic: ")
    data, num_tokens = extract_topic_data(topic, "", 800, 2)
    keywords, num_tokens = extract_keywords(data, num_tokens, 3)
    keywords_list = extract_keywords_list(keywords)
    print("Keywords: " + str(keywords_list) + "\n")
    print("Data: " + data + "\n")



if __name__ == "__main__":
    main()
