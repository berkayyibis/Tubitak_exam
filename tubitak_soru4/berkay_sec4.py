from PIL import Image
from numpy import asarray
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import math

def LineSum(img,p0,p1):
    # Get only one band
    imData = img[:,:,1]
    
    fig, ax = plt.subplots()

    x1=p0[0]
    y1=p0[1]
    x2=p1[0]
    y2=p1[1]

    m = (y2-y1) / (x2-x1)
    b = y1-m*x1

    sum = 0
    for x in range(x1,x2):
        y = m*x+b
        # draw line
        ax.scatter([int(x)], [int(y)],c='r', s=5 )
        if imData[int(x),int(y)] == 255:
            #ax.scatter([int(x)], [int(y)],c='r', s=5 )
            # ax.plot(int(x), int(y), '--', linewidth=5, color='firebrick') 
            sum = sum + 1

    # sum of the white pixels intersecting on given line
    print(sum)

    # imgplot = plt.imshow(imData)
    ax.set_title('Beyaz Renkli Pixel Toplamı {}'.format(sum))
    ax.imshow(imData)
    e1=Circle(tuple(p0),5)
    e2=Circle(tuple(p1),5)
    ax.add_patch(e1)
    ax.add_patch(e2)
    plt.show()

image = Image.open('C:/Users/Hp/Desktop/tubitak_part4/1.png')
img = asarray(image)
p0 = [4,345]
p1 = [289,49]

LineSum(img,p0,p1)
