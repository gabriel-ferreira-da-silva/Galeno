use galeno_database


db.createCollection("lung-cancer", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "type", "disease", "model"],
      properties: {
        gender: {
          bsonType: "double",
          description: ""
        },
        age: {
          bsonType: "double",
          description: ""
        },
        smoking: {
          bsonType: "double",
          description: ""
        },
        yellow_fingers: {
          bsonType: "double",
          description: ""
        },
        anxiety:{
          bsonType: "double",
          description: ""
        },
        peer_pressure:{
          bsonType: "double",
          description: ""
        },
        chronic_disease:{
          bsonType: "double",
          description: ""
        },
        fatigue:{
          bsonType: "double",
          description: ""
        },
        allergy:{
          bsonType: "double",
          description: ""
        },
        wheezing:{
          bsonType: "double",
          description: ""
        },
        alcohol_consuming:{
          bsonType: "double",
          description: ""
        },
        coughing:{
          bsonType: "double",
          description: ""
        },
        shortness_of_breath:{
          bsonType: "double",
          description: ""
        },
        swallowing_difficulty:{
          bsonType: "double",
          description: ""
        },
        chest_pain:{
          bsonType: "double",
          description: ""
        },
        lung_cancer:{
          bsonType: "double",
          description: ""
        }        
      }
    }
  }
})

