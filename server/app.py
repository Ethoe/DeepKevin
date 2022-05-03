from flask import Flask, render_template, session
import generate_text as gpt

app = Flask(__name__)

app.config.update(SECRET_KEY='osd(99092=36&462134kjKDhuIS_d23')


@app.route('/')
def index():
    print("serving")
    generator = gpt.Generator()
    text = generator.generate()
    return render_template('index.html', text=text)


if __name__ == "__main__":
    app.run()
