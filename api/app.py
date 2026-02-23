from flask import Flask, request, jsonify
from services.PredictServices import prediction_service
from services.TrainServices import train_service

app = Flask(__name__)

model = train_service()

@app.route("/categorize", methods=["POST"])
def get_categorization():
    req = request.get_json()

    if not req or "title" not in req:
        return jsonify({"status": "error", "message": "Missing title field"}), 400

    prediction = prediction_service(req["title"], model)

    return jsonify({
        "status": "success",
        "category": prediction
    }), 200