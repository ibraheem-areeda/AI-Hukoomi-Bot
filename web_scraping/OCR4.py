import pytesseract
from PIL import Image
import cv2
import re
from web_scraping.vehicle_validation import vehicle_validation

def image_info_extractor():


    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    front_face_license = '../images/user_image_input1.jpeg'  # USER INPUT FRONT FACE OF LICENCE
    rear_face_license = '../images/user_image_input2.jpeg'  # USER INPUT REAR FACE OF LICENSE

    def preprocess_image(image_path, save_path=None):
        image = cv2.imread(image_path)
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        denoised = cv2.fastNlMeansDenoising(gray, h=10)
        sharpened = cv2.GaussianBlur(denoised, (0, 0), 3)
        enhanced = cv2.addWeighted(denoised, 1.5, sharpened, -0.5, 0)
        
        _, thresholded = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        
        preprocessed = cv2.fastNlMeansDenoising(thresholded, h=10)
        
        pil_image = Image.fromarray(preprocessed)
        
        if save_path:
            pil_image.save(save_path)
        
        return pil_image

    def extract_text(image):
        text = pytesseract.image_to_string(image, lang='eng+ara', config='--psm 6')
        return text

    front_processed_path = '../images/2front_processed.jpg'
    front_image = preprocess_image(front_face_license, save_path=front_processed_path)
    text = extract_text(front_image)

    number_pattern = r'\b(\d{2})-(\d+)\b'
    number_match = re.search(number_pattern, text)
    first_two_numbers = number_match.group(1) if number_match else None
    remaining_numbers = number_match.group(2) if number_match else None

    rear_processed_path = '../images/3rear_processed.jpg'
    rear_image = preprocess_image(rear_face_license, save_path=rear_processed_path)
    rear_text = extract_text(rear_image)

    registration_number_pattern = r'\b(133\d+)\b'
    registration_number_match = re.search(registration_number_pattern, rear_text)
    registration_number = registration_number_match.group(1) if registration_number_match else None

    print("First Two Numbers:", first_two_numbers)
    print("Remaining Numbers:", remaining_numbers)


    print("Registration Number:", registration_number)
        

    return vehicle_validation(remaining_numbers, first_two_numbers, registration_number)
