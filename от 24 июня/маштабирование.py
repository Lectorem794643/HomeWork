imageHeight = int(input())
imageWidth = int(input())
originalImage = []
for i in range(imageHeight):
    originalImage.append(input())
resizedImage = []
for i in originalImage[::2]:
    resizedImage.append(i[::2])
    imageHeight = imageHeight // 2
    imageWidth = imageWidth // 2
for i in resizedImage:
    print(i)
