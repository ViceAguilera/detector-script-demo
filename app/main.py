"""
Main script for processing license plate detection and recognition.
"""
import json
import requests
import cv2
import easyocr
from ultralytics import YOLO

reader = easyocr.Reader(['en'] , gpu=False)

def http_post(score, img_name, text):
    """
    Send a POST request to the API.

    Args:
        score (float): Confidence score of the license plate text.
        img_name (str): Name of the image file.
        text (str): License plate text.

    Returns:
        None
    """
    url = "http://localhost:8000/api/registers"

    data = {
        "prediction_accuracy": score,
        "vehicle_image": img_name,
        "license_plate_image": "license_plate.jpg",
        "license_plate": text
    }

    json_data = json.dumps(data)

    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json_data, headers=headers, timeout=10)

    if response.status_code == 200:
        print("The request was sent successfully.")
    else:
        print(response.status_code)
        print("An error occurred while sending the request.")

def read_license_plate(license_plate_crop):
    """
    Read the license plate text from the given cropped image.

    Args:
        license_plate_crop (numpy.ndarray): Cropped image containing the license plate.

    Returns:
        tuple: Tuple containing the formatted license plate text and its confidence score.
    """

    detections = reader.readtext(license_plate_crop)

    for detection in detections:
        _, text, score = detection

        text = text.upper().replace(' ', '')
        if len(text) >= 6 and len(text) <= 10 and text.isalnum() and score >= 0.7 and not text.isalpha():
            return text, score

    return None, None

def main():
    """
    Main function
    """
    cap = cv2.VideoCapture("video/sample.mp4")
    license_plate_model = YOLO('model/licence_plate.pt')
    results = {}
    frame_nmr = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: failed to capture image")
            break
        result = license_plate_model(frame, agnostic_nms=True)[0]
        results[frame_nmr] = {}
        for detection in result.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = detection

            license_plate_crop = frame[int(y1):int(y2), int(x1):int(x2), :]
            license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
            _, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 150, 255, cv2.THRESH_BINARY)
            license_plate_text, license_plate_text_score = read_license_plate(license_plate_crop_thresh)

            if license_plate_text is not None:
                results[frame_nmr] = {
                    'license_plate': {
                        'bbox': [x1, y1, x2, y2],
                        'text': license_plate_text,
                        'bbox_score': score,
                        'text_score': license_plate_text_score
                    }
                }
                print("License plate:", license_plate_text)
                print("Detected with", "{:.2f}".format(license_plate_text_score * 100), "% confidence")
                photo = "sample" + str(frame_nmr) + ".jpg"
                #http_post(license_plate_text_score, photo, license_plate_text)

        frame_nmr += 1

    cap.release()

if __name__ == "__main__":
    main()
