# Skew-Correction-for-Text

In this repo, I created a Skew Correction for text using **OpenCV** and **Python**.

## How it works

- First, apply the **threshold** in the grayscale image
- **Dilates** a threshold image by using a specific structuring element
- Finds and draws **contours** in a dilated image
- Find the **rectangle** of the minimum area using contours
- Finally, **Wrap Transformation** with rectangle co-ordinates

## Installation

Install pre-requisites packages

```
pip install -r requirements.txt 
```

or

```
pip install numpy==1.22.0
pip install opencv-python==4.5.5.62
```
Am using NumPy version **1.22.0** and OpenCV version **4.5.5**, you can be used the updated version.

## How to run it

You can run the python file by giving this below command on your command prompt. Make sure you can use any image you want to give the correct image path after the --image argument.
```
python SkewCorrection.py --image images/img4.png
```

## Output
### Skew image
<img src='https://github.com/JafirDon/Skew-Correction-for-Text-Python/blob/main/images/img4.png' width="40%" ></img> <br><br>
### Skew Corrected image
<img src='https://github.com/JafirDon/Skew-Correction-for-Text-Python/blob/main/images/Rotated_image.jpg' width="40%" ></img>
