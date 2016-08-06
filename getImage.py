import os

def getImage(videoPath, imagePath):
	img_count = 1
	crop_time = 0.0
	while crop_time <= 219.0:
		os.system('ffmpeg -i %s -f image2 -ss %s -vframes 1 %s.png' % (videoPath, str(crop_time), imagePath + str(img_count)))
		img_count += 1
		print 'Geting Image ' + str(img_count) + '.png' + ' from time ' + str(crop_time)
		crop_time += 0.1
	print 'Image Collected'

if __name__ == '__main__':
	videoPath = '/Users/mac/Desktop/badapple.avi'
	imagePath = '/Users/mac/Desktop/badapple/images/'
	getImage(videoPath, imagePath)
