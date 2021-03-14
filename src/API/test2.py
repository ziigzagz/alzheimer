from PIL import Image, ImageDraw

if __name__ == '__main__':
    height = 600
    width = 600
    image = Image.new(mode='L', size=(height, width), color=255)

    # Draw a line
    draw = ImageDraw.Draw(image)
    x = image.width / 2
    y_start = 0
    y_end = image.height
    line = ((x, y_start), (x, y_end))
    draw.line(line, fill=128)
    del draw

    image.show()