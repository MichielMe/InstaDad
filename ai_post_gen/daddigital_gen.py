import openai
import os
from dotenv import load_dotenv

load_dotenv()



def dad_post():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    first_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content": "You are a creative assistant specialized in crafting impactful and relatable content for modern fathers."
            },
            {
            "role": "user",
            "content": "I need an inspiring Instagram post for modern dads. Or a really good dad joke."
            },
            {
            "role": "assistant",
            "content": "Hey Dads, remember when you thought a 'dad bod' was a 6-pack? Now it's a snack pack and a multitool belt, and guess what? You're rocking it. You're the CEOs of bedtime stories and the champions of 'Don't tell mom' moments. Keep being the legends you are."
            },
            {
            "role": "user",
            "content": "Generate a similar post. Make sure it contains absolutely no emojis, hashtags, or quotation marks. The text has a maximum of 600 characters."
            }
        ],
        temperature=1,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the generated inspiring text
    inspiring_text = first_response['choices'][0]['message']['content']

    # Second API call to generate the caption
    second_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a creative assistant specialized in crafting engaging and relevant Instagram captions."},
            {"role": "user", "content": f"Generate a caption for this inspiring post: '{inspiring_text}'."},
            {"role": "assistant", "content": "Elevate your day with this thought and remember, the best inspiration comes from within. Don't forget to check out our dad-curated shop, link in bio."},
            {"role": "user", "content": "Proceed with generating a similar caption. Make it a maximum of 400 characters, and use relevant hashtags."}
        ],
        temperature=0.8,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the generated caption
    caption = second_response['choices'][0]['message']['content']
    
    return inspiring_text, caption



