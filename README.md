# Description
> These are all projects from the **"Multi-disciplinary Project"** module, 
studying at **Vietnamese-German University**, _Foundation Year_.

# List of projects
- AI Camera based on Google Teachable Machine

# How to use
> Before using, please clone it to your local device by using this command `git clone https://github.com/KhavidBap/VGU_AIoT.git`

## AI Camera
> This model detects whether you are wearing glasses, not wearing glasses or if there is no object in the picture to detect. The output will be the subject that object related with the highest percentage, also its percentage.

`> Class: WithGlasses`

`> Confidence Score: 0.999998`

> There are 2 files in this folder, including: 
- `main.py`: The input is one or more images, the output is what mentioned above by each image.
> Put your image(s) in your folder, then change the code in `main.py` by changing the `<image_path>` in `image = Image.open("<image_path>").convert("RGB")` same name as your image file(s).
- `camera_detect.py`: The input is the video from your webcam device, the output is what mentioned above by real-time.
> Download DroidCam from any Android devices. Connect this local device and DroidCam with the same Wi-fi. Then copy the IP shown on the DroidCam into `camera = cv2.VideoCapture("<ip>")` (IP has the format as `https://x.x.x.x/video`)


