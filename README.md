# Satellite Content Platform v1.0

License: MIT Software License

## Authors: 
+ Pedro Guzmán (pguzmanb498@ulacit.ed.cr)
+ Fabiana Solano (fsolanor812@ulacit.ed.cr)
+ Josué Gabuardi (jgabuardib449@ulacit.ed.cr)

## Description:
Satellite content platform is a web application that enables globally distributed 
content creator, to collaborate and publish multi-lingual articles. The platform 
provides two main modules:
+ **Content Factory:** Provides a simple workflow that allows creation, translation, 
revision and approval (publishing) of content
+ **Content Publishing Platform:** Provides website with all the indexed content and 
search engine optimizations that make published content easier to be indexed and found
by search engines such as *Google* or *Bing*. 

## Requirements

* Python 3
* MongoDB
* Npm
* Bower

## Steps to run application locally in *dev* environment

First you must clone the repository where you want to run the application with *GIT* :

```Bash
$ git clone https://github.com/OneTesseractInMultiverse/satellite-frontend.git
$ cd satellite-frontend
```

The we need to install the Python dependencies:

```Bash
$ pip install -r requirements.txt  
```

Now install *npm* dependencies

```Bash
$ npm install  
```

Now install *bower* dependencies

```Bash
$ bower install 
```

Now run grunt to compile the scripts

```Bash
$ grunt 
```

Finally run the application:

```Bash
$ python run.py 
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 205-566-392

```



