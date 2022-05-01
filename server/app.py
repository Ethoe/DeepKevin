from flask import Flask, render_template, g
import generate_text as gpt

app = Flask(__name__)


@app.route('/')
def index():
    generator = gpt.Generator()
    text = generator.generate()
    print(text)
    return render_template('index.html', text=text)


if __name__ == "__main__":
    app.run()
