## E-Learning Platform
This is a project for CSE327. We are building a e-learning web app where educators can upload their content and learners can learn. The demo web interface for the project is like this -

<<<<<<< HEAD
![ui](demo_ui.jpg)
=======
![ui](https://github.com/siam923/CSE327/blob/master/demo_ui.JPG?raw=true)
>>>>>>> 2e4060cbe393253f30762fda87020b3985fff910

The project will be built with django as backend framework and bootstrap, react as frontend.

### To collaborate
* Fork the project
* create your own branch
* perform pull request

### Requirements
* Django
* pillow
* django-braces==1.13.0
* django-embed-video==1.1.2
> For generating graph diagram e.g uml 
* django-extensions
* pydotplus  -> includes pyparsing


#### Conver dot file to png
Run the following command as your choose:
```
$ python manage.py graph_models -a > dotfile.dot
$ python manage.py graph_models app1 app2 > fire_me.dot
$ python manage.py graph_models -a -I Foo,Bar > something.dot
$ python manage.py graph_models -a X Foo,Bar > nofoobar.dot
```

Now convert dot file to PNG. For this first install pydot, graphviz `pip install graphviz`. Now in python shell :
```
>>> import pydot
>>> (graph,) = pydot.graph_from_dot_file('dotfile.dot')
>>> graph.write_png('somefile.png')
```  

For frontend add your work in the __Frontend__ directory.
We will be using backend api endpoints to connect with the frontend. The EER model will be uploaded here soon.  
