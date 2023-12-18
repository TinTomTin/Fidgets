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

    
def generatePillArt(legoArtPic, inputImage, outFileName):
    colorAdjustedImage = inputImage.convert(mode="P", palette=1, colors=16, dither=3).resize([48, 48])
    inputPixelMap = colorAdjustedImage.load()
    inputPalette = colorAdjustedImage.getpalette()

    image = Image.new("RGB", (legoArtPic.pixelLength(), legoArtPic.pixelHeight()), "#000012")
    draw = ImageDraw.Draw(image)
    for x in range(legoArtPic.pilsX):
        for y in range(legoArtPic.pilsY):
            px = x * legoArtPic.pillSize
            py = y * legoArtPic.pillSize
            paletteIndex = inputPixelMap[x, y] * 3
            fillColor = (inputPalette[paletteIndex], inputPalette[paletteIndex + 1], inputPalette[paletteIndex +2])
            outlineColor = (fillColor[0] + 25, fillColor[1] + 25, fillColor[2] + 25)
            points = [(px, py), (px + legoArtPic.pillSize, py + legoArtPic.pillSize)]
            draw.ellipse(points, fill=fillColor, width=3, outline=outlineColor)
    image.save(outFileName)
    image.show()


exp = LegoArtPic(50, 48, 48)

inputImage =  Image.open("Boerneef.jpg")
#print('Colors in P mode image: {cols}'.format(cols=len(colorAdjust.getcolors())))
#colorAdjust = inputImage.convert(mode="RGB", colors=16, dither=3)
#rgbImage = colorAdjust.convert(mode="RGB", colors=16, palette=1).resize([48,48])
#print('Colors in RGB mode image: {cols}'.format(cols=len(rgbImage.getcolors())))

#generatePillArt(exp, inputImage, "20231218.gif")


#TODO: print col number in each pill
#TODO: split into 9 (3 x 3) tiles
#TODO: load custom palette
#TODO: source image as parameter

