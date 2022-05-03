from flask import Flask, render_template, request
import generate_text as gpt

app = Flask(__name__)

app.config.update(SECRET_KEY='osd(99092=36&462134kjKDhuIS_d23')


@app.route('/', methods=["GET", "POST"])
def index():
    text = ""
    temp = 1
    length = 50
    words = ""
    if request.method == "POST":
        generator = gpt.Generator()
        temp = request.form.get('temp')
        length = request.form.get('length')
        words = request.form.get('words')
        text = generator.generate(temprature=float(temp), length=int(length), prefix=words)
    
    return render_template('index.html', text=text, temp=temp, length=length, words=words)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()
