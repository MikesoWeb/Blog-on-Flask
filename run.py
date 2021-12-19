from blog import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # disable debug mode when deploy on server
        app.run(debug=True, port=5000, host='0.0.0.0')

