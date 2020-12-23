from flask import Flask, render_template, request, jsonify
import csv
app = Flask(__name__)

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/index_about.html')
def index_about():
    return render_template('index_about.html')

@app.route('/index_research.html')
def index_research():
    return render_template('index_research.html')

@app.route('/index_data.html')
def index_data():
    return render_template('index_data.html')

@app.route('/writings')
def get_writings():
    filterStr = request.args.get("filter", "")
    new_dic = []
    with open('Correlation.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if filterStr.lower() in row['Author'].lower():
                new_dic.append(row)
    return jsonify(new_dic)

if __name__ == '__main__':
    app.run(debug=True)






