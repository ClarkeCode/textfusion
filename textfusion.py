from PIL import Image, ImageDraw, ImageFont

image_width = 300
image_hight = 300
image_bg_colour = (255, 255, 255)
image = Image.new('RGB', (image_width, image_hight), color = image_bg_colour)

def addconstraints(text, constraint_value, thisfont):
        output = ""
        items = text.split()
        while len(items) != 0:
                chosen_word = items.pop(0)
                if output == "":
                        testval = chosen_word
                else:
                        testval = " ".join([output, chosen_word])
                if thisfont.getsize_multiline(testval)[0] > constraint_value:
                        output += "\n" + chosen_word
                else:
                        output = testval
        return output

font_name = 'Fonts/OpenSans-Regular.ttf'
font_size = 28
font_colour = (0, 0, 0)
selectedfont = ImageFont.truetype(font_name, font_size)
imagedraw = ImageDraw.Draw(image)

phrase = "The quick brown fox jumped over the lazy dog The quick brown fox jumped over the lazy dog"
phrase_cleaned = addconstraints(phrase, image_width, selectedfont)
imagedraw.text((10,10), phrase_cleaned, font=selectedfont, fill=font_colour)

image.save('output.png')


