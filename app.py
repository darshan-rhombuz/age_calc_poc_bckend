from flask import Flask, request, jsonify
from datetime import datetime, date

app = Flask(__name__)

def parse_flexible_date(date_str):
    """Try multiple date formats and normalize."""
    formats = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%d-%m-%Y", "%m-%d-%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    raise ValueError("Invalid date format. Please use YYYY-MM-DD, DD/MM/YYYY, or MM/DD/YYYY")

@app.route("/calculate-age", methods=["POST"])
def calculate_age():
    data = request.get_json()
    birthdate_str = data.get("birthdate")

    if not birthdate_str:
        return jsonify({"error": "Missing 'birthdate' field"}), 400

    try:
        birthdate = parse_flexible_date(birthdate_str)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return jsonify({
        "birthdate": birthdate.isoformat(),
        "age": age
    })

if __name__ == "__main__":
    app.run(debug=True)
