from PIL import Image, ImageDraw, ImageFont

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

def createTextImage(phrase, width_limit, selected_font, padding_amount=10, text_colour=(0,0,0), bg_colour=(255,255,255)):
        phrase_cleaned = addconstraints(phrase, width_limit - 2*padding_amount, selected_font)
        bounding_box = selected_font.getsize_multiline(phrase_cleaned)
        text_image = Image.new("RGB", (width_limit, 2*padding_amount+bounding_box[1]), bg_colour)
        image_draw = ImageDraw.Draw(text_image)
        image_draw.text((padding_amount,0), phrase_cleaned, font=selected_font, fill=text_colour)
        return text_image

def fuseImageVertically(topImage, bottomImage):
        fused_image = Image.new("RGB", (max(topImage.width, bottomImage.width), topImage.height + bottomImage.height))
        fused_image.paste(topImage, (0,0))
        fused_image.paste(bottomImage, (0, topImage.height))
        return fused_image

font_name = 'Fonts/OpenSans-Regular.ttf'
font_size = 28
selectedfont = ImageFont.truetype(font_name, font_size)
phrase = "The quick brown fox jumped over the lazy dog"

input_image = Image.open("input.png")
text_image = createTextImage(phrase, input_image.width, selectedfont)

fuseImageVertically(text_image, input_image).save('output.png')
