import cv2
import numpy as np

params = cv2.SimpleBlobDetector_Params()
params.minThreshold = 10
params.maxThreshold = 200
params.filterByColor = True
params.blobColor = 255
# params.filterByCircularity = False
params.filterByCircularity = True
params.minCircularity = 0.1
params.filterByConvexity = False
params.filterByInertia = False
params.filterByArea = True
params.minArea = 100
detector = cv2.SimpleBlobDetector_create(parameters=params)


def detect(img):
    blurred = cv2.blur(img, (5, 5))
    hls = cv2.cvtColor(blurred, cv2.COLOR_BGR2HLS)
    lightness_mask = cv2.inRange(hls[:, :, 1], 230, 255)
    darkness_mask = cv2.inRange(hls[:, :, 1], 0, 100)
    mask = cv2.inRange(hls[:, :, 0], 70 / 360 * 180, 90 / 360 * 180)
    # mask = cv2.bitwise_or(lightness_mask, mask)
    # mask = cv2.bitwise_and(cv2.bitwise_not(lightness_mask), mask)
    # mask = cv2.bitwise_and(cv2.bitwise_not(darkness_mask), mask)
    masked = cv2.bitwise_and(img, img, mask=mask)
    ones = (np.ones(hls.shape) * 255).astype(np.uint8)
    mask_gray = cv2.bitwise_and(ones, ones, mask=mask)
    keypoints = detector.detect(mask_gray)
    print(f'Detected {len(keypoints)} keypoints')
    for k in keypoints:
        print(f'  At {int(k.pt[0])}, {int(k.pt[1])} with size {k.size}')
    return keypoints, cv2.drawKeypoints(masked, keypoints, None, (0, 0, 255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
