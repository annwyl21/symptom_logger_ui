from application import app

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

if __name__ == "__main__":
    # app.run(port=5000, debug=True)
    app.run()