use galeno_database


db.createCollection("models", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "type", "disease", "model"],
      properties: {
        name: {
          bsonType: "string",
          description: "The name of the machine learning model"
        },
        disease: {
          bsonType: "string",
          description: "The disease that the model predicts"
        },
        type: {
          bsonType: "string",
          description: "The type of machine learning model"
        },
        last_update: {
          bsonType: ["date", "null"],
          description: "The date when the model was last updated"
        },
        input_description: {
          bsonType: "string",
          description: "Description of the model's input"
        },
        output_description: {
          bsonType: "string",
          description: "Description of the model's output"
        },
        model: {
          bsonType: "binData",
          description: "The actual machine learning model serialized as binary data"
        }
      }
    }
  }
})

