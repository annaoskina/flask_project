from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def index_about():
    return render_template('index_about.html')

def index_data():
    return render_template('index_data.html')

if __name__ == '__main__':
    app.run(debug=True)

