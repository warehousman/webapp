from project import app

app.config['TESTING'] = True
app.config['DEBUG'] = False

if __name__ == "__main__":
    unittest.main()