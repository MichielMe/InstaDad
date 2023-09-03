from ai_post_gen.daddigital_gen import dad_post
from instagram_api.instagram_poster import post_dad
from image_creation.image_creator import create_image

def main():
    # Step 1: Generate inspiring text and caption
    inspiring_text, caption = dad_post()
    
    # Optional: Log the generated text and caption for debugging or auditing
    print(f"Generated Text: {inspiring_text}")
    print(f"Generated Caption: {caption}")
    
    create_image(inspiring_text)
    
    # # Post to instagram
    # post_dad(caption)
    
# ... (your existing imports and code)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
