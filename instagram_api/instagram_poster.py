import os
from dotenv import load_dotenv
from instagrapi import Client

def post_dad(caption, imagepath="../INSTADAD/ready_to_post/post01.jpg"):
    load_dotenv()

    username = os.getenv("INSTAGRAM_USERNAME")
    password = os.getenv("INSTAGRAM_PASSWORD")
    

    client = Client()
    try:
        client.login(username, password)
    except ChallengeRequired:
        print("A challenge is required. Please manually log in to Instagram to solve the challenge.")
        return None

    try:
        media = client.photo_upload(imagepath, caption)
    except Exception as e:
        print(f"An error occurred while posting: {e}")
        return None
    
    
    return media