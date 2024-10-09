# Galeno

Backend API services to provide predictions for diseases diagnosis using machine learning models (ann, clusters, bayes, gaussian). Backend is developed with python flask and mongoDB.

Galeno provides predictions based on ml models and data in MLMODELS directory. The models can be trained, updated and stored in mongo database and the system is run with python flask

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
  --data '{"input_array": [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]}' \
  http://localhost:5000/api/heartfailure/predict/mlp
  
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"input_array": [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]}' \
  http://localhost:5000/api/heartfailure/predict/kmean
  
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"input_array": [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]}' \
  http://localhost:5000/api/heartfailure/predict/kmedoid

```

## workflow of Galeno


![](https://github.com/gabriel-ferreira-da-silva/Galeno/blob/main/doc/img/Untitled(3).png?raw=true)

## stack



![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_wAM-QRdFtITvOLKa6Yfscv5mewaggdAJTdyxsRjqaf-lrXWtauyitvbEIQrGLMvylQ&usqp=CAU)







![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThejmwKaSdHRIvI4IPLvGudxHKM92fKiSDuA&s)