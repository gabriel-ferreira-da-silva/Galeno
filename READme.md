# Galeno

Backend API services to provide predictions for diseases diagnosis using machine learning models (ann, clusters, bayes, gaussian). Backend is developed with python flask and mongoDB.

Galeno provides predictions based on ml models and data in MLMODELS directory. The models can be trained, updated and stored in mongo database and the system is run with python flask


<video width="320" height="240" controls>
  <source src="video.mov" type="video/mp4">
</video>


## suported analysis:

- **heart failure**
  - multilayer perceptron 
  - k means
  - k medoids
- **breast cancer**
  - gaussian process regressor
- **lung cancer**
  - multilayer perceptron

### Request endpoints example to heart failure's analysis

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{ \
  				"name":"lung-cancer-mlp"  ,  \
  				:input_array": [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]  \
  		}' \
  http://localhost:5000/api/models/predict
```





## <u> Galeno's workflow and archtecture</u>


![](https://github.com/gabriel-ferreira-da-silva/Galeno/blob/main/doc/img/newpattern.png?raw=true)

# <u> stack</u>

<div style="display:flex; flex-direction: row">
    <img src= "https://github.com/gabriel-ferreira-da-silva/gabriel-ferreira-da-silva/blob/main/flask.png?raw=true" style="width:80px; height:80px; margin:20px">
    <img src= "https://github.com/gabriel-ferreira-da-silva/gabriel-ferreira-da-silva/blob/main/bash.png?raw=true" style="width:80px; height:80px; margin:20px">
    <img src= "https://github.com/gabriel-ferreira-da-silva/gabriel-ferreira-da-silva/blob/main/react.png?raw=true" style="width:80px; height:80px; margin:20px">
    <img src= "https://github.com/gabriel-ferreira-da-silva/gabriel-ferreira-da-silva/blob/main/mongo.png?raw=true" style="width:80px; height:80px; margin:20px">
    <img src= "https://github.com/gabriel-ferreira-da-silva/gabriel-ferreira-da-silva/blob/main/scikit.png?raw=true" style="width:100px; height:80px; margin:20px">
</div>
