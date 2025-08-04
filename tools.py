import cv2
import base64
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

# Capture an image from the default webcam and return it as Base64 encoded string
def capture_image() -> str:
    """
    Captures one frame from the default webcam, resizes it,
    encodes it as Base64 JPEG (raw string) and returns it.
    """
    for idx in range(4):
        cap = cv2.VideoCapture(idx)  # Let OpenCV choose backend
        if cap.isOpened():
            for _ in range(10):  # Warm up camera
                cap.read()
            ret, frame = cap.read()
            cap.release()
            if not ret:
                continue
            # Optional: Save image
            cv2.imwrite("sample.jpg", frame)
            # Encode as JPEG
            ret, buf = cv2.imencode('.jpg', frame)
            if ret:
                return base64.b64encode(buf).decode('utf-8')
    raise RuntimeError("Could not open any webcam (tried indices 0-3)")

capture_image() # Call the function to test it


from groq import Groq

def analyze_image_with_query(query: str) -> str:
    """
    Expects a string with 'query'.
    Captures the image and sends the query and the image to
    to Groq's vision chat API and returns the analysis.
    """
    img_b64 = capture_image()
    model="meta-llama/llama-4-maverick-17b-128e-instruct"
    
    if not query or not img_b64:
        return "Error: both 'query' and 'image' fields required."

    client=Groq()  
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{img_b64}",
                    },
                },
            ],
        }]
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content

# query = "What is in this image?"
# print(analyze_image_with_query(query))  # Call the function to test it

