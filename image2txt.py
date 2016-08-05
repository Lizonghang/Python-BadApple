from PIL import Image
import numpy

def image2txt(inputFile, outputFile):
	im = Image.open(inputFile).convert('L')
	charWidth = 300
	im = im.resize((charWidth, charWidth / 4))
	target_width, target_height = im.size
	data = numpy.array(im)[:target_height, :target_width]
	f = open(outputFile, 'w')
	for row in data:
		for pixel in row:
			if pixel > 127:
				f.write('#')
			else:
				f.write(' ')
		f.write('\n')
	f.close()