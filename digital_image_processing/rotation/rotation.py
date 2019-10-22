from matplotlib import pyplot as plt
from numpy import float32
import cv2


def get_rotation(img, pt1, pt2, rows, cols):
    """
    Get image rotation
    :param img: np.array
    :param pt1: 3x2 list
    :param pt2: 3x2 list
    :param rows: columns image shape
    :param cols: rows image shape
    :return: np.array
    """
    matrix = cv2.getAffineTransform(pt1, pt2)
    return cv2.warpAffine(img, matrix, (rows, cols))


if __name__ == "__main__":
    # read original image
    image = cv2.imread("lena.jpg")
    # turn image in gray scale value
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # get image shape
    img_rows, img_cols = gray_img.shape

    # set different points to rotate image
    pts1 = float32([[50, 50], [200, 50], [50, 200]])
    pts2 = float32([[10, 100], [200, 50], [100, 250]])
    pts3 = float32([[50, 50], [150, 50], [120, 200]])
    pts4 = float32([[10, 100], [80, 50], [180, 250]])

    # add all rotated images in a list
    images = [
        gray_img,
        get_rotation(gray_img, pts1, pts2, img_rows, img_cols),
        get_rotation(gray_img, pts2, pts3, img_rows, img_cols),
        get_rotation(gray_img, pts2, pts4, img_rows, img_cols),
    ]

    # plot different image rotations
    fig = plt.figure(1)
    titles = ["Original", "Rotation 1", "Rotation 2", "Rotation 3"]
    for i in range(0, len(images)):
        plt.subplot(2, 2, i + 1), plt.imshow(images[i], "gray")
        plt.title(titles[i])
        plt.axis("off")
        plt.subplots_adjust(left=0.0, bottom=0.05, right=1.0, top=0.95)
    plt.show()
