import re
import time
import openai
openai.api_key = "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"



def extract_topic_data(topic, data, num_tokens, num_tries):
    """
    # Extracts topic data from a given text using OpenAI's GPT-3 API. The text is formatted to match the format of the training data. The text is then passed to the API, which returns a list of possible completions. The first completion is returned.
    # @param topic: The topic to extract data from
    # @param data: The text to extract data from
    # @param num_tokens: The number of tokens to use
    # @param num_tries: The number of times to try to extract data
    # @return: The extracted data as a string
    """
    print("Fetching topic data...")

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=data + "\n\n\n"
               "Topic = " + topic + "\n\n\n"
               "What are 7 key points I should know for every new topic that I learn?\n"
               "1. What are the goals of the topic?\n"
               "2. What are the key concepts?\n"
               "3. What are the key skills?\n"
               "4. What are the key strategies?\n"
               "5. What are the key resources?\n"
               "6. Examples\n"
               "7. What are the key equations?\n\n\n"
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
               "Use the Example format above to answer the topic questions:\n\n\n",
        temperature=0.42,
        max_tokens=num_tokens,
        top_p=1,
        best_of=1,
        frequency_penalty=0,
        presence_penalty=0.0
    )
    if response.choices[0].text == "" or response.choices[0].text == " ":
        return extract_topic_data(topic, data, num_tokens, num_tries + 1)
    else:
        return response.choices[0].text, num_tokens




def extract_keywords(data, num_tokens, num_tries):
    """
    # Extracts keywords from a given text using OpenAI's GPT-3 API. The text is formatted to match the format of the training data. The text is then passed to the API, which returns a list of possible completions. The first completion is returned.
    # @param num_tokens: The number of tokens to use
    # @param num_tries: The number of times to try to extract keywords
    # @param data: The text to extract keywords from
    # @return: The extracted keywords as a string
    """
    print("Extracting keywords...")

    keywords = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Example Keywords:\n-Advancing the ball\n-Downs\n-Line of Scrimmage\n\n"
               "Extract keywords from the following text using the Example keywords format. Use hyphens for multi-word keywords:\n\n"
               + data + "\n\nKeywords:\n",
        temperature=0.3,
        max_tokens=num_tokens,
        top_p=1.0,
        frequency_penalty=0.8,
        presence_penalty=0.0
    )
    if keywords.choices[0].text == "" or keywords.choices[0].text == " ":
        return extract_keywords(data, num_tokens, num_tries + 1)
    else:
        return keywords.choices[0].text, num_tokens


def extract_keywords_list(data):
    """
    # Extracts keywords from a given text and returns them as a list of strings.
    # @param data: The text to extract keywords from
    # @return: The extracted keywords as a list of strings
    """

    return list({x.strip('.,!?;-') for x in re.split(' |\n', data.lower()) if len(x) > 1})


def learn_new_topic():
    """
    # This is the main function. The purpose of this program is to give a user the ability to learn new topics. The user can enter a topic and the program will extract data from the topic and return it to the user. The user can then enter a new topic and the program will extract data from the new topic.
    """
    while True:
        topic = input("Topic = ")
        data, num_tokens = extract_topic_data(topic, "", 1000, 0)
        time.sleep(10)
        keywords, num_tokens = extract_keywords(data, num_tokens, 0)
        keywords_list = extract_keywords_list(keywords)
        print(keywords_list)
        print(data)
        print(num_tokens)
        print(data)


if __name__ == "__main__":
    learn_new_topic()
