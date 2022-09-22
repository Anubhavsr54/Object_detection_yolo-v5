from detect import run 
import os
from PIL import Image
from applicationlogger.setup_logger import setup_logger
import base64
import streamlit as st
# creating logger instance
os.makedirs("mylogs", exist_ok=True)
log_file_path = os.path.join("mylogs", "infer.log")
logger = setup_logger("infer_logs", log_file=log_file_path)

def get_subdirs(b='.'):
    '''
        Returns all sub-directories in a specific Path
    '''
    result = []
    for d in os.listdir(b):
        bd = os.path.join(b, d)
        if os.path.isdir(bd):
            result.append(bd)
    return result

def get_detection_folder():
    '''
        Returns the latest folder in a runs\detect
    '''
    return max(get_subdirs(os.path.join('runs', 'detect')), key=os.path.getmtime)

def save_video(video_file):
    '''
        Saves the video file on local system
    '''
    video_file.seek(0)
    os.makedirs("inputs", exist_ok=True)
    path = os.path.join("inputs", video_file.name)
    with open(path, 'wb') as f:
        f.write(video_file.read())

def save_image(img_file):
    '''
        Saves the image file on local system
    '''
    img = Image.open(img_file)
    os.makedirs("inputs", exist_ok=True)
    path = os.path.join("inputs", img_file.name)
    img.save(path)

def infer_video(video_file):
    '''
        Runs the inference on the video file
    '''
    run(source=video_file,
        weights=os.path.join('weights', 'yolov5s.pt'))

def infer_image(image_file):
    '''
        Runs the inference on the image file
    '''
    run(source=image_file,
        weights=os.path.join('weights', 'yolov5s.pt'))


def infer(model, source, file_type):
    """
        Performs inference on yolov5 model
        Outputs:
            - detected result save will be local 

"""
    try:
        logger.info("Inferring on model: {} Input type {}".format(str(model), str(file_type)))
        run(model, source)
        logger.info("Inference on model: {} Input type {} completed".format(str(model), str(file_type)))
    except Exception as e:
        logger.error("Inference on model: {} Input type {} failed".format(str(model), str(file_type)))
        logger.error(e)


def get_binary_file_downloader_html(bin_file, file_label='File'):
    """Function to get download link for file.
    Source:- https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806/26
    """
    with st.spinner("Hold on while creating download link for results..."):
        with open(bin_file, 'rb') as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
        return href