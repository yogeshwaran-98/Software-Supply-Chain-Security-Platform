from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Zero Trust Supply Chain Platform"
    }

@app.route("/health")
def health():
    return {
        "status": "healthy"
    }

# Intentionally vulnerable endpoint
@app.route("/execute")
def execute():
    code = request.args.get("code")

    if code:
        return str(eval(code))

    return "Provide ?code="

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)