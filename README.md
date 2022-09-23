<p align="center">
<img src="https://forthebadge.com/images/badges/made-with-python.svg" >
</p>


<h2 align="center">
 🤖 Object Detection with YoloV5 🤖 
 </h2>

<p align="center">
<img align="center" src="diagram_yolo.png" >
</p>

Used state-of-the-art object detection model YoloV5   trained on [COCO 80 classes](https://github.com/ultralytics/yolov5/blob/master/data/coco.yaml), weights are downloaded. 

Used [streamlit](https://streamlit.io/) for the webpage

### To run the program on the local machine, follow below steps.
``` 1. Clone the repository ```

``` 2. Create an virtual env (python>=3.8)```

``` 3. pip install -r requirements.txt``` 

``` 4. streamlit run st.py ```

``` Application should open on your default browser```


You can upload an image or video file, the app will understand and will show you a message about your file type and inference will proceed as per your file type. Click on the `infer` button to start the inference. The inference will take time as per your file size and system configuration.
one sample image and video are provided contained in the `samples_inputs` folder, although it can perform detection from any video or image that is uploaded.
After the completion of the inference output will appear along with a download link for the file.


<p align="center">
<img align="center" src="scrren.jpg" >
</p>



### Contributor <img src="https://media3.giphy.com/media/1wrgDc6j07hAlM7Jml/giphy.gif?cid=790b7611e3af35beee6df1266c31edcabc53abfbbb82854c&rid=giphy.gif&ct=g" width="30"> 

[Anubhav Srivastav](https://www.linkedin.com/in/anubhav-srivastav-466a42194/)

## Acknowledge 
[yolov5 ultralytics](https://github.com/ultralytics/yolov5) 
