from website import create_app #if __init__.py in a folder you can import the parent folder and it will run the .__init__ by default
app = create_app()
if __name__ == '__main__': #only if you run this file ddirectly it will run, even if you import it you can't (if name of the file is running is equal to this file)
    app.run(debug=True) #automatically rerun web server whenever it's updated 