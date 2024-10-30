# Galeno

Galeno is a robust backend API service designed to provide predictive analytics for disease diagnosis using various machine learning models, including artificial neural networks (ANN), clustering algorithms, and Gaussian models. The backend is developed using Python Flask and utilizes MongoDB for data storage.

Galeno operates by leveraging machine learning models stored in the MLMODELS directory. Users can train, update, and store these models in the MongoDB database, ensuring the system remains current and effective in delivering accurate predictions.

The frontend interface allows users to easily manage diseases and models, offering functionalities to add, delete, or train models as needed, streamlining the workflow for medical professionals and researchers.

![](https://github.com/gabriel-ferreira-da-silva/gabriel-ferreira-da-silva/blob/main/galeno.gif?raw=true)


## Dependendcies and Run

galeno depends on
 - mongoDB
 - react
 - flask

to build and run the application go to the directory and run the build.sh file

```
cd galeno
chmod +x build.sh
./build.sh
```

## suported analysis:

the build adds the following diseases and  models

- **heart failure**
  - multilayer perceptron 
  - k means
  - k medoids
- **breast cancer**
  - gaussian process regressor
- **lung cancer**
  - multilayer perceptron

new diseases and models can be added.

### Request endpoints

Example:

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{ \
    "name":"lung-cancer-mlp"  ,  \
    "input_array": [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]  \
  }' \
  http://localhost:5000/api/models/predict
```


## <u> Galeno's workflow and archtecture</u>


![](https://github.com/gabriel-ferreira-da-silva/Galeno/blob/main/doc/img/newpattern.png?raw=true)

# <u> stack</u>

<div style="display:flex; flex-direction: row">
    <img src= "https://github.com/gabriel-ferreira-da-silva/gabriel-ferreira-da-silva/blob/main/flask.png?raw=true" style="width:60px; height:70px; margin:20px">
    <img src= "https://github.com/gabriel-ferreira-da-silva/gabriel-ferreira-da-silva/blob/main/bash.png?raw=true" style="width:80px; height:80px; margin:20px">
    <img src= "https://github.com/gabriel-ferreira-da-silva/gabriel-ferreira-da-silva/blob/main/react.png?raw=true" style="width:80px; height:80px; margin:20px">
    <img src= "https://github.com/gabriel-ferreira-da-silva/gabriel-ferreira-da-silva/blob/main/mongo.png?raw=true" style="width:80px; height:80px; margin:20px">
    <img src= "https://github.com/gabriel-ferreira-da-silva/gabriel-ferreira-da-silva/blob/main/scikit.png?raw=true" style="width:100px; height:80px; margin:20px">
</div>
