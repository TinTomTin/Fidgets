from PIL import Image, ImageDraw

class LegoArtPic:
    def __init__(self, pillSize, pilsX, pilsY):
        self.pillSize = pillSize
        self.pilsX = pilsX
        self.pilsY = pilsY
    


image = Image.new("RGB", (400, 400), "#000012")
draw = ImageDraw.Draw(image)
for x in range(5):
    px = x * 20
    points = [(px, 20), (px + 20, 40)]
    draw.ellipse(points, fill="#002200", outline="#004400", width=2)
image.save("first.gif")