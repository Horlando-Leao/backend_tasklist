from app.main import app

@app.route('/')
def index():
    return "<h1>Welcome to CodingX</h1>"
