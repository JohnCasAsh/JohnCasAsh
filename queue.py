from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    message = "Hello, World!"  # Message to display in the HTML
    return render_template('index.html', message=message)  # Pass message to HTML

if __name__ == '__main__':
    app.run(debug=True)
