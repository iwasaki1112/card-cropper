import cv2
import numpy as np

def rotate_to_vertical(img):
    h, w, _ = img.shape
    if w > h:  # 横向きの場合
        img = cv2.transpose(img)
        img = cv2.flip(img, flipCode=0)  # 0はX軸での反転を意味します
    return img

def create_rounded_rectangle(img, radius=20):  # 半径を15に変更
    rounded_rect = np.zeros(img.shape, dtype=np.uint8)
    
    h, w, _ = img.shape

    # 四隅の円を描画
    cv2.circle(rounded_rect, (radius, radius), radius, (255, 255, 255), -1)
    cv2.circle(rounded_rect, (w - radius, radius), radius, (255, 255, 255), -1)
    cv2.circle(rounded_rect, (radius, h - radius), radius, (255, 255, 255), -1)
    cv2.circle(rounded_rect, (w - radius, h - radius), radius, (255, 255, 255), -1)

    # 四辺の矩形を描画
    cv2.rectangle(rounded_rect, (radius, 0), (w - radius, h), (255, 255, 255), -1)
    cv2.rectangle(rounded_rect, (0, radius), (w, h - radius), (255, 255, 255), -1)

    return cv2.bitwise_and(img, rounded_rect)
