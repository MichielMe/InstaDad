from PIL import Image, ImageDraw, ImageFont


def create_image(text):
    def text_wrap(text, font, max_width):
        lines = []
        words = text.split()
        estimated_line_length = 0
        line = ""

        for word in words:
            estimated_word_length = font.getlength(word + " ")
            estimated_line_length += estimated_word_length

            if estimated_line_length < max_width:
                line += word + " "
            else:
                lines.append(line)
                line = word + " "
                estimated_line_length = estimated_word_length

        lines.append(line)
        return lines

    # Create an image and draw object
    img = Image.open("image_creation/bg_images/bg-02.jpg")
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("../INSTADAD/fonts/Roboto-Medium.ttf", 44)

    max_width = 800
    initial_height = 120
    y_text = initial_height

    # text = "Text that goes on the image."
    wrapped_text = text_wrap(text, fnt, max_width)

    for line in wrapped_text:
        d.text((125, y_text), line, font=fnt, fill=(255, 255, 255))
        y_text += 62  # Increment Y position based on your desired line height

    img.save("../INSTADAD/ready_to_post/post01.jpg")
