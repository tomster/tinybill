to get started run:

 * ``python bootstrap.py`` (once only)
 * then ``bin/buildout`` (every time you change buildout.cfg)
 * then ``./bin/paster serve paste.ini`` to start the app
 * visit ``http://localhost:8080/`` to see the result
 
make changes to src/tinybill/main.py (you need to restart the paster process whenever you change code to see the changes take effect)