import streamlit as st
import os
from st_utils import *
from streamlit.elements.image import _np_array_to_bytes


# Title
st.markdown("<h1 style='text-align: center;'>🤖 Object Detection with YoloV5 🤖</h1>", unsafe_allow_html=True)

input_file = st.sidebar.file_uploader("Uplode your file",
                         type=["jpeg", "jpg", "mp4"],
                         help="Upload your file here or drag and drop here.")

# Infer button
infer_btn = st.sidebar.button("Infer", help="click to infer")

# detecting input type. image or video
if input_file is not None:
    if input_file.name.endswith(".mp4"):
        input_type = 'video'
        st.sidebar.info("You uploaded a video file")
        st.sidebar.video(input_file)
        save_video(input_file) # saving video file on local system for inference
        st.success("Video file is ready for inference")

        # doing inference on video
        if infer_btn:
            with st.spinner("Hold on while model is detecting objects..."):
                path = os.path.join("inputs", input_file.name)
                infer(model="./weights\yolov5s.pt",
                    source=path,
                    file_type="video")
            st.balloons()
            st.success("Inference done, Below is the result.")
            # getting the path of result video
            res = os.path.join(get_detection_folder(), input_file.name) #  full path of the latest result video
            st.video(res)
            with st.spinner("Hold on while creating download link for the result..."):
                st.markdown(get_binary_file_downloader_html(res, 'Video'), unsafe_allow_html=True) # Putting Download link on the page
    
    else:
        input_type = 'image'
        st.sidebar.info("You uploaded an image file")
        st.sidebar.image(input_file)
        save_image(input_file) # saving image file on local system for inference
        st.success("Image file is ready for inference.")
        
        # doing inference on image
        if infer_btn:
            with st.spinner("Hold on while model is detecting objects... "):
                path = os.path.join("inputs", input_file.name)
                model_path = os.path.join("weights", "yolov5s.pt")
                infer(model=model_path,
                    source=path,
                    file_type="image")
            st.balloons()
            st.success("Inference done, Below is the result.")
            # getting the path of result image
            res = os.path.join(get_detection_folder(), input_file.name) #  full path of the latest result image
            st.image(res)
            with st.spinner("Hold on while creating download link for the result..."):
                st.markdown(get_binary_file_downloader_html(res, 'Image'), unsafe_allow_html=True) # Putting Download link on the page

else:
    st.info("Please upload a file or select from Sample files.")
    st.markdown("<h3 style='text-align: center;'>🤖 Sample Files 🤖</h3>", unsafe_allow_html=True)
    file = st.selectbox("Select a file", ["None","Image", "Video"])
    if file == "Image":
        st.sidebar.info("You selected an image file")
        st.sidebar.image(os.path.join("samples_inputs", "road.jpg"))
        st.success("Image file is ready for inference.")
        # doing inference on image
        if infer_btn:
            with st.spinner("Hold on while model is detecting objects... "):
                path = os.path.join("samples_inputs", "road.jpg")
                model = os.path.join("weights", "yolov5s.pt")
                infer(model=model,
                    source=path,
                    file_type="image")
            st.balloons()
            st.success("Inference done, Below is the result.")
            # getting the path of result image
            res = os.path.join(get_detection_folder(), "road.jpg") #  full path of the latest result image
            st.image(res)
            with st.spinner("Hold on while creating download link for the result..."):
                st.markdown(get_binary_file_downloader_html(res, 'Image'), unsafe_allow_html=True) # Putting Download link on the page
    
    elif file == "Video":
        st.sidebar.info("You selected a video file")
        st.sidebar.video(os.path.join("samples_inputs", "road.mp4"))
        st.success("Video file is ready for inference.")
        # doing inference on video
        if infer_btn:
            with st.spinner("Hold on while model is detecting objects..."):
                path = os.path.join("samples_inputs", "road.mp4")
                model = os.path.join("weights", "yolov5s.pt")
                infer(model=model,
                    source=path,
                    file_type="video")
            st.balloons()
            st.success("Inference done, Below is the result.")
            # getting the path of result video
            res = os.path.join(get_detection_folder(), "road.mp4") #  full path of the latest result video
            st.video(res)
            with st.spinner("Hold on while creating download link for the result..."):
                st.markdown(get_binary_file_downloader_html(res, 'Video'), unsafe_allow_html=True) # Putting Download link on the page

st.write("Codes are here. [Github](https://github.com/Anubhavsr54/)")