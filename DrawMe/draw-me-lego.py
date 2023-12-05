from PIL import Image, ImageDraw

class LegoArtPic:
    def __init__(self, pillSize, pilsX, pilsY):
        self.pillSize = pillSize
        self.pilsX = pilsX
        self.pilsY = pilsY

    def pixelLength(self):
        return self.pilsX * self.pillSize
    
    def pixelHeight(self):
        return self.pilsY * self.pillSize

    

exp = LegoArtPic(50, 48, 48)
image = Image.new("RGB", (exp.pixelLength(), exp.pixelHeight()), "#000012")
draw = ImageDraw.Draw(image)
for x in range(exp.pilsX):
    for y in range(exp.pilsY):
        px = x * exp.pillSize
        py = y * exp.pillSize
        points = [(px, py), (px + exp.pillSize, py + exp.pillSize)]
        draw.ellipse(points, fill="#002200", outline="#004400", width=3)
image.save("20231128.gif")