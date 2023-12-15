import random, os
from PIL import ImageFont, Image, ImageDraw

tiers = {
    "S": [ (255, 127, 127), 0 ],
    "A": [ (191, 255, 127), 1 ],
    "B": [ (255, 223, 127), 2 ],
    "C": [ (127, 255, 255), 3 ],
    "D": [ (127, 191, 255), 4 ],
    "E": [ (255, 127, 255), 5 ],
    "F": [ (191, 127, 191), 6 ]
}

def visualize(tier_list):
    height = 1500
    width = 3400

    font = ImageFont.truetype("arial.ttf", 30)
    tier_font = ImageFont.truetype("arial.ttf", 30)
    
    image = Image.new("RGB", (width, height), "black")

    x = 0
    y = 0

    for i in tiers:
        if tiers[i][1]+1 > len(tier_list):
            break
        if y == 0:
            draw = ImageDraw.Draw(image)
            draw.rectangle(( y, x, y + 200, x + 200 ), fill=tiers[i][0])
            draw.text(( y + 80, x + 75 ), i, font=tier_font, fill="black")
            y += 200
        for character in tier_list[tiers[i][1]]:
            char_name = character.split(".")[0].replace("_", " ").title()

            char_img = Image.open(open(f"images/{character}", "rb"))
            char_img = char_img.resize((200, 200))

            image.paste(char_img, (y, x, y + 200, x + 200))

            draw = ImageDraw.Draw(image)
            
            draw.text((y, x), char_name, font=font, fill="white")

            y += 200

        x += 200
        y = 0

    image.show("Tier List")
    image.save(open("image.png", "wb"), format="png")

def generate_tier(characters: list, tier_list: list, num_of_chars: int, tier: int):
    tier_list.append([])

    for i in range(num_of_chars):
        if len(characters) > 0:
            char = random.choice(characters)
            tier_list[tier].append(char)
            characters.remove(char)
            continue
        break
    
    return tier_list

def main(characters: list, tier_list: list, num_of_chars: int):
    _tier = 0
    for tier in tiers:
        if len(characters) > 0:
            tier_list = generate_tier(characters, tier_list, num_of_chars, _tier)
            _tier += 1
            continue
        break

    return tier_list

if __name__ == "__main__":
    characters = os.listdir("images")
    
    tier_list = []

    num_of_chars = round((len(characters)/len(tiers))+1)

    tier_list = main(characters, tier_list, num_of_chars)
    
    visualize(tier_list)