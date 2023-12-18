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
            #outlineColor = (sourceColor[0] + 25, sourceColor[1] + 25, sourceColor[2] + 25)
            points = [(px, py), (px + legoArtPic.pillSize, py + legoArtPic.pillSize)]
            draw.ellipse(points, fill=sourceColor, width=3)
    image.save(outFileName)
    image.show()


exp = LegoArtPic(50, 48, 48)

inputImage =  Image.open("Boerneef.jpg")
colorAdjust = inputImage.convert(mode="P", palette=1, colors=16, dither=3)
#colorAdjust = inputImage.convert(mode="RGB", colors=16, dither=3)
#colorAdjust.save("lowCol4.gif")
#rgbImage = colorAdjust.convert(mode="RGB", colors=16, palette=1)
#rgbImage.save("lowColRGB.jpg")
#inputImage2 = Image.open("lowCol3.gif")
smallNeef = colorAdjust.resize([48, 48])
pixelMap = smallNeef.load()
colors = smallNeef.getcolors()
palette = smallNeef.getpalette()
print(palette[13 * 3])
print(palette[13 * 3 + 1])
print(palette[13 * 3 + 2])



#smallNeef.save("smallneef3.gif")
#print(pixelMap[0,0])
#print(pixelMap[1,0])
#print(pixelMap[2,0])
#print(pixelMap[3,0])
#print(pixelMap[4,0])
#print(pixelMap[5,0])
#print(pixelMap[6,0]) #13
#generatePillArt(exp, pixelMap, "20231212.gif")



