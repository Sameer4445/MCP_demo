from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load CSV file
df = pd.read_csv("students.csv")

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Use /students (GET). Query params: branch, year"})

@app.route("/students", methods=["GET"])
def get_students():
    branch = request.args.get("branch")
    year = request.args.get("year")

    result = df.copy()

    if branch:
        result = result[result["branch"].str.lower() == branch.lower()]
    if year:
        result = result[result["year"] == int(year)]

    return jsonify(result.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(port=5000)
