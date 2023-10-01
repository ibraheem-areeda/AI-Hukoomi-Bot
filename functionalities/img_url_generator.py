import base64
import requests

def image_to_base64(image_path):

    with open(image_path, "rb") as image_file:
        encoded_bytes = base64.b64encode(image_file.read())
        encoded_string = encoded_bytes.decode('utf-8')
        return encoded_string
    
def img_url_generator(image_path):
    url = "https://api.imgbb.com/1/upload"
    image_base64 = image_to_base64(image_path)
    payload = {
        'key': "f79ac5a6e8f4a1e56b9ad2b245229f04",
        'image': image_base64
    }
    response = requests.post(url, payload)
    response_json = response.json()
    
    if response.status_code == 200 and 'data' in response_json:
        image_url = response_json['data']['url']
        return image_url
    else:
        return None