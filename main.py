from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def index_about():
    return render_template('index_about.html')

@app.route('/research')
def index_research():
    return render_template('index_research.html')

@app.route('/data')
def index_data():
    return render_template('index_data.html')


def get_search_results(q):
    if q == "Akutagawa":
        result = ["Rashomon", "Majutsu"]
    else:
        result = [""]
    return result

@app.route('/search', methods=["get", "post"])
def search():
    q=request.values.get("q", "")
    print(q)
    result = get_search_results(q)
    return render_template('search.html', q=q, result=result)

if __name__ == '__main__':
    app.run(debug=True)



