use('galeno_database')

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
        description: {
          bsonType: "string",
          description: "description of the machine learning"
        },
        disease: {
          bsonType: "string",
          description: "name of the disease the model trained for"
        },
        type: {
          bsonType: "string",
          description: "The type of machine learning model"
        },
        last_update: {
          bsonType: ["date", "null"],
          description: "The date when the model was last updated"
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

db.createCollection("diseases", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "disease", "scaler"],
      properties: {
        name: {
          bsonType: "string",
          description: "The name of the disease classificaction"
        },
        description: {
          bsonType: "string",
          description: "description of the disease"
        },
        disease: {
          bsonType: "string",
          description: "name formal name of the disease"
        },
        input_description: {
          bsonType: "array",
          description: "Description of the model's input"
        },
        scaler: {
          bsonType: "binData",
          description: "scaler for inputs"
        }
      }
    }
  }
})

db.models.createIndex({ name: 1 }, { unique: true });
db.diseases.createIndex({ name: 1 }, { unique: true });