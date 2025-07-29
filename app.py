from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def calculator():
    data = request.json
    operation = data.get("operation")
    a = data.get("a")
    b = data.get("b")
    result = None

    try:
        a = float(a)
        b = float(b)
    except (ValueError, TypeError):
        return jsonify(error="Invalid input.please enter numbers only."), 400

    if operation == "add":
       result = a + b
    elif operation == "subtract":
       result = a - b
    elif operation == "multiply":
       result = a * b
    elif operation == "divide":
       if b == 0:
           return jsonify(error="Division by zero is not allowed."), 400
       result = a / b
    else:
       return jsonify(error="Invalid operation. Use add, subtract, multiply, or divide."), 400
        
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)   
