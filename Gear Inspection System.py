import cv2

ideal_img = cv2.imread("ideal.jpg", 0)
_, ideal_binary = cv2.threshold(ideal_img, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

sample2_img = cv2.imread("sample2.jpg", 0)
_, sample2_binary = cv2.threshold(sample2_img, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
diff2 = cv2.bitwise_xor(ideal_binary, sample2_binary)
contours2, _ = cv2.findContours(diff2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
broken2 = 0
worn2 = 0
min_worn_area = 10
for cnt in contours2:
    area = cv2.contourArea(cnt)
    if area > 200:
        broken2 += 1
    elif min_worn_area < area <= 200:
        worn2 += 1
print(f"Gear sample2.jpg -> Broken: {broken2}, Worn: {worn2}")

sample3_img = cv2.imread("sample3.jpg", 0)
_, sample3_binary = cv2.threshold(sample3_img, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
diff3 = cv2.bitwise_xor(ideal_binary, sample3_binary)
contours3, _ = cv2.findContours(diff3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
broken3 = 0
worn3 = 0
for cnt in contours3:
    area = cv2.contourArea(cnt)
    if area > 200:
        broken3 += 1
    elif min_worn_area < area <= 200:
        worn3 += 1
print(f"Gear sample3.jpg -> Broken: {broken3}, Worn: {worn3}")

sample4_img = cv2.imread("sample4.jpg", 0)
_, sample4_binary = cv2.threshold(sample4_img, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
diff4 = cv2.bitwise_xor(ideal_binary, sample4_binary)
contours4, _ = cv2.findContours(diff4, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
broken4 = 0
worn4 = 0
for cnt in contours4:
    area = cv2.contourArea(cnt)
    if area > 200:
        broken4 += 1
    elif min_worn_area < area <= 200:
        worn4 += 1
print(f"Gear sample4.jpg -> Broken: {broken4}, Worn: {worn4}")

sample5_img = cv2.imread("sample5.jpg", 0)
_, sample5_binary = cv2.threshold(sample5_img, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
diff5 = cv2.bitwise_xor(ideal_binary, sample5_binary)
contours5, _ = cv2.findContours(diff5, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
broken5 = 0
worn5 = 0
for cnt in contours5:
    area = cv2.contourArea(cnt)
    if area > 200:
        broken5 += 1
    elif min_worn_area < area <= 200:
        worn5 += 1
print(f"Gear sample5.jpg -> Broken: {broken5}, Worn: {worn5}")

sample6_img = cv2.imread("sample6.jpg", 0)
_, sample6_binary = cv2.threshold(sample6_img, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
diff6 = cv2.bitwise_xor(ideal_binary, sample6_binary)
contours6, _ = cv2.findContours(diff6, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
broken6 = 0
worn6 = 0
for cnt in contours6:
    area = cv2.contourArea(cnt)
    if area > 200:
        broken6 += 1
    elif min_worn_area < area <= 200:
        worn6 += 1
print(f"Gear sample6.jpg -> Broken: {broken6}, Worn: {worn6}")
