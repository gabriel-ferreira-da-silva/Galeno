# Galeno development journal



## Base backend operations

![](/home/gabriel/Desktop/projetos2024/galeno/doc/img/Untitled(3).png)

### how data and models should relate

the goal of galeno is to be a well structure platform for disease analysis and diagnosis.

- a disease may be analyzed by multiple models
- models shall be trained by the same source of data
- models shall have a metadata header with their information such as 
- - name
  - type of model
  - last update timestamp
  - input description
  - output description

![collection-relations](/home/gabriel/Downloads/collection-relations.png)