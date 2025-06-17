from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Text and style settings
text = "WELCOME TO THE DEVOPS ARENA\nEnjoy !!!\n- Tejas Pandhare"
font_size = 20
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Substitute for Verdana
text_color = (255, 255, 255)  # White

# Create a dummy image to calculate text size
dummy_img = Image.new("RGB", (1, 1))
draw = ImageDraw.Draw(dummy_img)
font = ImageFont.truetype(font_path, font_size)
bbox = draw.multiline_textbbox((0, 0), text, font=font, spacing=4)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Padding
padding = 20
img_width = text_width + 2 * padding
img_height = text_height + 2 * padding

# Create diagonal gradient background
def create_gradient(w, h, start_color, end_color):
    base = np.zeros((h, w, 3), dtype=np.uint8)
    for y in range(h):
        for x in range(w):
            factor = (x + y) / (w + h)
            color = [
                int(start_color[i] * (1 - factor) + end_color[i] * factor)
                for i in range(3)
            ]
            base[y, x] = color
    return Image.fromarray(base)

start_color = (255, 0, 255)     # Magenta
end_color = (128, 0, 128)       # Dark Magenta
background = create_gradient(img_width, img_height, start_color, end_color)

# Draw text
draw = ImageDraw.Draw(background)
draw.multiline_text((padding, padding), text, fill=text_color, font=font, spacing=4)

# Save image
background.save("tp_01.png", format="PNG", optimize=True)
print("Image saved as 'tp_01.png'")
