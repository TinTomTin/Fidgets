from PIL import Image, ImageDraw, ImageFont

class LegoArtPic:
    def __init__(self, pillSize, pilsX, pilsY):
        self.pillSize = pillSize
        self.pilsX = pilsX
        self.pilsY = pilsY

    def pixelLength(self):
        return self.pilsX * self.pillSize
    
    def pixelHeight(self):
        return self.pilsY * self.pillSize

def generateColorLegend(pillSize, inputImage, outFileName):
    colorsUsed = inputImage.getcolors()
    palette = inputImage.getpalette()
    xStart = 30
    yPadding = 10
    fontOffset = int(pillSize / 2)
    legendImage = Image.new("RGB", (500, len(colorsUsed) * (pillSize + yPadding)), "#000000")
    legendDraw = ImageDraw.Draw(legendImage)
    legendDraw.font = ImageFont.truetype("FreeMono.ttf", size=30)
    for colNumber in colorsUsed:
        paletteIndex = colNumber[1] * 3
        fillColor = (palette[paletteIndex], palette[paletteIndex + 1], palette[paletteIndex +2])
        outlineColor = (fillColor[0] + 25, fillColor[1] + 25, fillColor[2] + 25)
        x1 = xStart
        y1 = colNumber[1] * pillSize + (colNumber[1] * yPadding)
        x2 = xStart + pillSize
        y2 = (colNumber[1] * pillSize ) + (colNumber[1] * yPadding) + pillSize
        points = [(x1, y1), (x2, y2)]
        legendDraw.ellipse(points, fill=fillColor, outline=outlineColor, width=3)
        legendDraw.text((x1 + fontOffset, y1 + fontOffset), str(colNumber[1]), fill='white', anchor='mm')
        legendDraw.text((xStart + 70, y1 + fontOffset), 'x {cnt}'.format(cnt = colNumber[0]), fill='white', anchor='lm')
    legendImage.save('{fn}-legend.gif'.format(fn=outFileName))
    

def generatePillArt(legoArtPic, inputImage, outFileName):
    colorAdjustedImage = inputImage.convert(mode="P", palette=1, colors=16, dither=3).resize([48, 48])
    inputPixelMap = colorAdjustedImage.load()
    inputPalette = colorAdjustedImage.getpalette()
    fontOffset = int(legoArtPic.pillSize / 2)

    image = Image.new("RGB", (legoArtPic.pixelLength(), legoArtPic.pixelHeight()), "#000012")
    draw = ImageDraw.Draw(image)
    draw.font = ImageFont.truetype("FreeMono.ttf", size=30)
    for x in range(legoArtPic.pilsX):
        for y in range(legoArtPic.pilsY):
            px = x * legoArtPic.pillSize
            py = y * legoArtPic.pillSize
            paletteIndex = inputPixelMap[x, y] * 3
            fillColor = (inputPalette[paletteIndex], inputPalette[paletteIndex + 1], inputPalette[paletteIndex +2])
            outlineColor = (fillColor[0] + 25, fillColor[1] + 25, fillColor[2] + 25)
            points = [(px, py), (px + legoArtPic.pillSize, py + legoArtPic.pillSize)]
            draw.ellipse(points, fill=fillColor, width=3, outline=outlineColor)
            draw.text((px + fontOffset, py + fontOffset), str(int(paletteIndex / 3)),fill=(200, 200, 200), anchor="mm")
    image.save(outFileName)
    generateColorLegend(legoArtPic.pillSize, colorAdjustedImage, outFileName)


exp = LegoArtPic(50, 48, 48)

inputImage =  Image.open("Kas2.jpg")
#print('Colors in P mode image: {cols}'.format(cols=len(colorAdjust.getcolors())))
#colorAdjust = inputImage.convert(mode="RGB", colors=16, dither=3)
#rgbImage = colorAdjust.convert(mode="RGB", colors=16, palette=1).resize([48,48])
#print('Colors in RGB mode image: {cols}'.format(cols=len(rgbImage.getcolors())))

generatePillArt(exp, inputImage, "Kas2.gif")


#TODO: split into 9 (3 x 3) tiles
#TODO: load custom palette
#TODO: source image as parameter
#TODO: generate image with pill legend
#TODO: share using streamlit

