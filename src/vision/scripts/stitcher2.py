import cv2
from PIL import Image
import numpy as np

path = "src/vision/scripts/images/"

img1 = cv2.imread(path + "image_cam1.jpg")
img2 = cv2.imread(path + "image_cam2.jpg")

scale = 2

img1 = cv2.resize(img1, (int(640/scale), int(480/scale)))
img2 = cv2.resize(img2, (int(640/scale), int(480/scale)))

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

print(len(img1))

_, img1 = cv2.threshold(img1, 120, 255, type= cv2.THRESH_BINARY)
_, img2 = cv2.threshold(img2, 120, 255, type= cv2.THRESH_BINARY)

print(len(img2))

def center(dim):
    return (int(dim[0]/2), int(dim[1]/2))

def sub_dim(dim1, dim2):
    return (dim1[0] - dim2[0], dim1[1] - dim2[1])

def offset(dim, off):
    return (dim[0] + off[0], dim[1] + off[1])

def concat():
    #global img2
    #img2 = cv2.rotate(img2, cv2.ROTATE_180)
    im1 = Image.fromarray(img1)
    im2 = Image.fromarray(img2)
    dst_dim = (im1.width + im2.width, im1.height)
    dst = Image.new('RGB', dst_dim)
    off = 100 # 104
    off = int(off/scale)
    dst.paste(im2, (0,0))
    dst.paste(im1, (off,0))
    dst2 = Image.new('RGB', dst_dim)
    dst2.paste(im1, (off,0))
    dst2.paste(im2, (0,0))
    dst3 = Image.new('RGB', dst_dim)
    dst3.paste(im1, (off,0))
    dst2 = Image.new('RGB', dst_dim)
    dst2.paste(im1, (off,0))
    dst2.paste(im2, (0,0))

    #res = np.asarray(dst) - np.asarray(dst2)
    res = np.bitwise_xor(np.asarray(dst), np.asarray(dst2))

    res2 = np.bitwise_and(np.asarray(dst3), res)
    print(res.shape)

    
    return res, res2

newim, new2 = concat()

while True:
    cv2.imshow('concat', newim)
    cv2.imshow('frame1', img1)
    cv2.imshow('frame2', img2)
    cv2.imshow('frame3', new2)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()