from PIL import Image, ImageDraw, ImageFont
import numpy as np
import math

# Constants
text = "This is DEVOPS Arena\nEnjoy your journey !!!\n \nWarm Wishes  \n-Tejas Pandhare"
font_size = 32
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
canvas_size = (800, 600)
padding = 20
num_frames = 20  # More frames for smoother animation
spacing = 6

# Load font
font = ImageFont.truetype(font_path, font_size)

# Calculate text size
dummy_img = Image.new("RGB", (1, 1))
draw = ImageDraw.Draw(dummy_img)
bbox = draw.multiline_textbbox((0, 0), text, font=font, spacing=spacing)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Center text
x = (canvas_size[0] - text_width) // 2
y = (canvas_size[1] - text_height) // 2


# Function: Create diagonal gradient
def create_gradient(w, h, start_color, end_color, shift=0):
    base = np.zeros((h, w, 3), dtype=np.uint8)
    for y in range(h):
        for x in range(w):
            factor = ((x + y + shift) % (w + h)) / (w + h)
            color = [
                int(start_color[i] * (1 - factor) + end_color[i] * factor)
                for i in range(3)
            ]
            base[y, x] = color
    return Image.fromarray(base)


# Generate animated frames
frames = []
for i in range(num_frames):
    # Animation factor from 0 to 1 and back (like a sine wave)
    pulse = 0.5 * (1 + math.sin(2 * math.pi * i / num_frames))
    # Text color pulses between white and light magenta
    text_color = (
        int(255 * pulse),
        int(200 * pulse),
        int(255 * pulse)
    )

    # Create gradient with animated shift
    shift = i * 25
    bg = create_gradient(*canvas_size, (255, 0, 255), (128, 0, 128), shift)
    draw = ImageDraw.Draw(bg)
    draw.multiline_text((x, y), text, fill=text_color, font=font, spacing=spacing)
    frames.append(bg)

# Save as animated GIF
frames[0].save("animated_tp.gif", format="GIF", save_all=True, append_images=frames[1:], duration=100, loop=0)
print("🎉 Enhanced animated GIF saved as 'animated_tp.gif'")
