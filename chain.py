import openai  
import os
from config import API_KEY, SUMMARY_OUTPUT_PATH, TWITTER_OUTPUT_PATH, HASHTAGS_OUTPUT_PATH

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)
        
apikey = API_KEY
       

def fetch_gpt_response(prompt, model_engine='text-davinci-003', max_tokens=300):
    openai.api_key = apikey
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens
    )
    return response.choices[0].text.strip()
    
word1 = open_file('input.txt')

#Summary Chain 1
word2 = open_file('prompt.txt').replace('<<BLOG>>', word1)
word3 = fetch_gpt_response(word2)
print('/n/n/ Summary:', word3)
save_file(SUMMARY_OUTPUT_PATH, word3)

#Summary Chain 2
word4 = open_file('prompt2.txt').replace('<<TWT>>', word3)
word5 = fetch_gpt_response(word4)
print('/n/n/ Tweet:', word5)
save_file(TWITTER_OUTPUT_PATH, word5)

#Summary Chain 3
word6 = open_file('prompt3.txt').replace('<<POST>>', word5)
word7 = fetch_gpt_response(word6)
print('/n/n/ Hashtags:', word7)
save_file(HASHTAGS_OUTPUT_PATH, word7)








 

 
 
    
    
    
    
    

    
    
    
    
    