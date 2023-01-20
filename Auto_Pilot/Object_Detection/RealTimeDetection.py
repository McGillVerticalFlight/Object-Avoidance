#refer to
#https://github.com/abdelrahman-gaber/tf2-object-detection-api-tutorial/blob/master/detect_objects.py
#modified to meet our need
import os
import cv2
import time

from detector import DetectorTF2

#Global variable
GENERAL_PATH = os.path.dirname(__file__)

CKPT_PATH = "ssd_mobnet_x320\saved_model"
CKPT_FULL_PATH = os.path.join(GENERAL_PATH,CKPT_PATH)
LABEL_MAP_FULL_PATH = os.path.join(GENERAL_PATH,"label_map.pbtxt")
CLASS_IDS = [1,2]

THRESHOLD=0.7

VIDEO_PATH = 1
def DetectFromVideo(detector, Video_path, output_dir='output/'):

	cap = cv2.VideoCapture(int(Video_path))


	while(True):
		ret, img = cap.read()

		if not ret:
			raise Exception("Unable to read from camera")
			cap.release()
			break

		timestamp1 = time.time()
		det_boxes = detector.DetectFromImage(img)
		elapsed_time = round((time.time() - timestamp1) * 1000) #ms
		img = detector.DisplayDetections(img, det_boxes, det_time=elapsed_time)

		cv2.imshow('TF2 Detection', cv2.resize(img, (1280, 720)))
		if cv2.waitKey(10) & 0xFF == ord('q'):
			cap.release()
			cv2.destroyAllWindows()
			break



	if save_output:
		out.release()


def DetectImagesFromFolder(detector, images_dir):

	for file in os.scandir(images_dir):
		if file.is_file() and file.name.endswith(('.jpg', '.jpeg', '.png')) :
			image_path = os.path.join(images_dir, file.name)
			print(image_path)
			img = cv2.imread(image_path)
			det_boxes = detector.DetectFromImage(img)
			img = detector.DisplayDetections(img, det_boxes)

			cv2.imshow('TF2 Detection', img)
			cv2.waitKey(0)






detector = DetectorTF2(CKPT_FULL_PATH, LABEL_MAP_FULL_PATH,CLASS_IDS,THRESHOLD)
DetectFromVideo(detector, VIDEO_PATH)

cv2.destroyAllWindows()
