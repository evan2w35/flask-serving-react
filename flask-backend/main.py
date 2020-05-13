import flask

app = flask.Flask("__main__")


@app.route("/")
def my_index():
    # return "Hello Python World"
    return flask.render_template("index.html", token="Hello React+Flask world!")


app.run(debug=True)
