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

    
def generatePillArt(legoArtPic, inputPixelMap, outFileName):
    image = Image.new("RGB", (legoArtPic.pixelLength(), legoArtPic.pixelHeight()), "#000012")
    draw = ImageDraw.Draw(image)
    for x in range(legoArtPic.pilsX):
        for y in range(legoArtPic.pilsY):
            px = x * legoArtPic.pillSize
            py = y * legoArtPic.pillSize
            sourceColor = inputPixelMap[x, y]
            outlineColor = (sourceColor[0] + 5, sourceColor[1] + 5, sourceColor[2] + 5)
            points = [(px, py), (px + legoArtPic.pillSize, py + legoArtPic.pillSize)]
            draw.ellipse(points, fill=sourceColor, outline="#888888", width=3)
    image.save(outFileName)


exp = LegoArtPic(50, 48, 48)

inputImage =  Image.open("Boerneef.jpg")
inputImage.load()

smallNeef = inputImage.resize([48, 48])
pixelMap = smallNeef.load()
#smallNeef.save("smallneef.jpg")
print(pixelMap[1,1])
generatePillArt(exp, pixelMap, "20231205.gif")



