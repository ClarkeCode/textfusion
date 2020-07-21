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



if __name__ == "__main__":
        import argparse
        parser = argparse.ArgumentParser(
                #usage="%(prog)s [OPTIONS] MESSAGE INPUT [OUTPUT]",
                description="Fuse any provided text with the indicated image")
        parser.add_argument(
                "-v", "--version", action="version",
                version = f"{parser.prog} version 0.1.0")
        parser.add_argument("message")
        parser.add_argument("inputfilename")
        parser.add_argument("outputfilename", nargs="?", default="output.png")
        parser.add_argument("-s", "--fontsize", type=int, default=30)
        parser.add_argument("-f", "--fontname", default="Fonts/OpenSans-Regular.ttf")

        parser.add_argument("-tbg", "--textbackgroundrgb", nargs=3, type=int, default=[255,255,255])
        parser.add_argument("-fc", "--fontcolour", nargs=3, type=int, default=[0,0,0]) 
        
        
        args = parser.parse_args()
        print(args)
        
        selectedfont = ImageFont.truetype(args.fontname, args.fontsize)
        input_image = Image.open(args.inputfilename)
        text_image = createTextImage(args.message, input_image.width, selectedfont)
        fuseImageVertically(text_image, input_image).save(args.outputfilename)
