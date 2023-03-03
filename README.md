# Skin Disease Prediction using Image Processing
This project aims to predict skin diseases using image processing techniques. Skin diseases are a significant public health concern globally. Early detection of skin diseases can help in effective treatment and prevention of serious health issues.

This project leverages image processing techniques to analyze skin lesion images and classify them into different skin disease categories, including melanoma, nevus, and basal cell carcinoma.
# Tech Stacks
- django
- numpy
- Pytorch
- torchvision
- Pillow
- HTML
- CSS
- Bootstrap
- python
# Installation
To run this project, you need to install the following dependencies:
- Python 3.8.11
- Django==4.0.3
- numpy==1.22.2
- Pillow==9.0.1
- urllib3==1.26.8
- onnxruntime==1.10.0
- idna==3.3
- whitenoise==6.0.0
You can install the dependencies using pip:
```bash
  pip install  Django==4.0.3 numpy==1.22.2 Pillow==9.0.1
  - etc

```

other dependencies are available requirement.txt file and you can install these dependencies just one commond
```bash
  pip install -r requirements.txt

```

## Usage

After installing dependencies which are mention in requirements.txt file

1. Go To New Terminal of code editor
2. Type command
 ```
python manage.py runserver
```
<img width="724" alt="server" src="https://user-images.githubusercontent.com/126494872/222790296-ef9b7e87-1b2c-4494-9b16-6957433f71ad.png">

## Dataset
This project uses the HAM10000 dataset, which contains 10015 dermatoscopic images of pigmented skin lesions. The dataset consists of 7 different categories of skin diseases: melanoma, nevus, seborrheic keratosis, basal cell carcinoma, actinic keratosis, benign keratosis, and dermatofibroma.
This site using dataset from [kaggle ](https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000)

## Model
This project uses a convolutional neural network (CNN) to classify skin lesion images. The CNN has the following architecture:

- Convolutional layer with 32 filters and a kernel size of 3x3.
- Max pooling layer with a pool size of 2x2.
- Convolutional layer with 64 filters and a kernel size of 3x3.
- Max pooling layer with a pool size of 2x2.
- Convolutional layer with 128 filters and a kernel size of 3x3.
- Max pooling layer with a pool size of 2x2.
- Fully connected layer with 128 neurons.
- Output layer with 7 neurons.
The model achieves an accuracy of over 90% on the test set.

## ScreenShots
- Register
<img width="958" alt="Rejister" src="https://user-images.githubusercontent.com/126494872/222789636-c0d4084d-9a90-4176-bbea-b9562f871825.png">
- Uploading an image
<img width="860" alt="uploading" src="https://user-images.githubusercontent.com/126494872/222789789-bfb24dcc-3ce5-4566-8842-f4c1b1fa440d.png">

- Result
<img width="637" alt="resulting" src="https://user-images.githubusercontent.com/126494872/222789900-0bcfe9bd-5f08-42e4-81f3-a705323ddc8a.png">


## Contributors
- Abdur Reman 
- M.Ilyas  
- M.Arslan 
- Hunza Batool





