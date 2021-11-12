from flask import Flask, render_template
import main
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title = main.get_title(), img_url = main.get_image(), book_list = main.recommended_books())

if __name__ == "__main__":
    app.run()
