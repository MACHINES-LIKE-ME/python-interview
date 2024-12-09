from app import app

if __name__ == "__main__":
    # Running Flask's development server directly:
    # When using `flask run`, the environment variable FLASK_APP=app/main.py will be used.
    app.run(host="0.0.0.0", port=5000, debug=True)
