from flask import Flask, render_template, request
from texttable import TextTable
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        data = request.form.get('inputtext').strip()
        tt = TextTable(data)
        return render_template('index.html',table=tt.generate_table())
    return render_template('index.html')


if __name__ == "__main__":    
    app.run(debug=os.environ["debug"], port=os.environ["port"], host=os.environ["host"])