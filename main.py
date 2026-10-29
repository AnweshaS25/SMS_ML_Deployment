# Import FastAPI to create the API application
from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

# Import our existing ML prediction function
from predict import predict_sms

# Create our FastAPI application
app = FastAPI()

# Define the structure of an incoming SMS request
class SMSRequest(BaseModel):
    # BaseModel: Pydantic class used to define and validate incoming data

    # Require a non-empty SMS message
    message: str = Field(min_length=1)

    # Validate the SMS message before processing
    @field_validator("message")
    @classmethod
    def validate_message(cls, value):

        # Remove spaces from the beginning and end
        value = value.strip()

        # Reject messages containing only whitespace
        if not value:
            raise ValueError("SMS message cannot be empty or whitespace-only")

        # Return the validated message
        return value


# Create a GET endpoint to check whether the service is running
@app.get("/")
def home():

    # Return a simple status message
    return {"message": "SMS ML Prediction Service is running!"}


# Create a POST endpoint for SMS classification
@app.post("/predict")
def predict(request: SMSRequest):

    # Pass the received SMS to our trained ML model
    prediction, spam_probability = predict_sms(request.message)

    # Return the result as a JSON response
    return {
        "prediction": prediction,
        "spam_probability": round(float(spam_probability), 4)
    }