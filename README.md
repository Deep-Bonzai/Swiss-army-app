###Head to the profile pages
[Bill Bunkum Profile](https://billbunkum.github.io/ "Bill Bunkum main")

[Kelly Wright Profile](http://www.kellyinnovation.com/ "Kelly Wright main")

#Multi-function tool
*a flask app*

## Swiss-army-app does?
1. Links to developers' profile sites
2. Simple calculator tool
3. Word counter tool
4. Github user's repo search
5. **API** request tool for generating *random users*

### Basic Setup for development
*On local machine
+ `mkvirtualenv -p python3 swiss-army-app`
+ `pip install -r requirements.txt`

*Run the flask app
+ `python run.py`


#How to...set Flask  up

###1. set up git repo/file structure
    $ mkdir <project name>
    $ pushd <project name> 
    $ git init

+ create a new repo in GitHub; clone the *url* or *ssh link*
    $ git remote add origin <cloned url>
    // make first add/commit/push
    $ git add .
    $ git commit -m "initial commit"
    $ git push origin master

###2. set up virtual environment


###3. requirements.txt


###4. w/in run.py
    from app import app
    app.run(debug=True)

###5. running/debugging a Flask project

1. `$ python run.py`

