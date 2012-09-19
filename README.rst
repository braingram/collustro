collustro :
    survey, explore, illuminate

"I want to see my program"

Use [python](http://python.org), [flask](http://flask.pocoo.org/), [d3](http://mbostock.github.com/d3/), and a hefty amount of glue to take stuff in python and visualize it in a web browser.

    import collustro
    # do lots of stuff, and leave locals() a complete mess
    collustro.explore(locals())

TODO
------

* server api (seperate ajax from regular calls)
* type conversion registration (defaults & plugins)
* template registration (defaults, home, local)
* more visualization plugins (modules, strings, simple things...)
* sort out what to do on errors (type conversion, missing template, etc...)
* make javascript chart templates more modular (standard header...)
* documentation (add docs to modules, describe project & structure, add tutorial here)
* automatically launch browser
