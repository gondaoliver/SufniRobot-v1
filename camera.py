from flask import Flask, Response
import cv2

# Initialize Flask app
app = Flask(__name__)

# Open the webcam
camera = cv2.VideoCapture(0)
camera.set(3, 1280)
camera.set(4, 720)


# Function to generate the frames for video streaming
def generate_frames():
    while True:
        # Read a frame from the webcam
        success, frame = camera.read()
        
        if not success:
            break
        else:
            # Convert the frame to JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
            # Yield the frame to stream to the browser
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# Route for the camera stream
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Route for the homepage (with video streaming embedded)
@app.route('/')
def index():
    return """
    <html>
        <head>
            <title>Live Camera Stream</title>
        </head>
        <body>
            <h1>Camera Stream</h1>
            <img src="/video_feed" width="640" height="480" />
        </body>
    </html>
    """

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
