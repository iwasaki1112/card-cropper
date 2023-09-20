from fastapi import FastAPI, HTTPException, UploadFile, File
from typing import List
import cv2
import numpy as np
from utils import rotate_to_vertical, create_rounded_rectangle

app = FastAPI()
@app.post("/process_cards/")


# directory = "./original_cards"
# index = 0;
# for filename in os.listdir(directory):
#   if filename.startswith("._"):  # macOSのメタデータファイルをスキップ
#         continue

#   if filename.endswith(".jpg") or filename.endswith(".png"):
#     filepath = os.path.join(directory, filename)
    
#     image = cv2.imread(filepath)
#     if image is None:
#       print("Failed to load the image." + filepath)
#       exit()
    
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     _, thresholded = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
#     contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
#     for _, contour in enumerate(contours):
#         # 輪郭の面積を計算
#         area = cv2.contourArea(contour)
        
#         # 小さな輪郭は無視
#         if area < 1000:
#             continue

#         # ローテーションを考慮した最小の外接矩形を取得
#         rect = cv2.minAreaRect(contour)
#         box = cv2.boxPoints(rect)
#         box = np.intp(box)

#         # 外接矩形をもとにカードを切り出す
#         width, height = int(rect[1][0]), int(rect[1][1])
#         src_pts = box.astype("float32")
#         dst_pts = np.array([[0, height-1],
#                             [0, 0],
#                             [width-1, 0],
#                             [width-1, height-1]], dtype="float32")
#         M = cv2.getPerspectiveTransform(src_pts, dst_pts)
#         warped = cv2.warpPerspective(image, M, (width, height))
        
#         # 画像が横向きの場合は縦向きにする
#         warped = rotate_to_vertical(warped)

#         # 画像の高さや横幅が10px以下のものは無視
#         if warped.shape[0] <= 10 or warped.shape[1] <= 10:
#             continue

#         # 切り出したカードの縁を角丸にする
#         rounded = create_rounded_rectangle(warped)

#         output_filename = f'./cards/card_{index}.png'

#         # 切り出したカードを保存
#         cv2.imwrite(output_filename, rounded)
#         index += 1
