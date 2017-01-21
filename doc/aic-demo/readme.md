# Description 

Minimal WebServer with Ajax content to return a value over http.

See the (source on GitHub)[https://github.com/RinusW/WiPy/tree/master/AiCWebserver].

This project has been the root source for the rest_server() 

Special thank to _Rinus_
 
# AiCWebserver

This is a simple webserver for the WiPy, aimed at control applications. The accompanian webpage consist of two input elements,
one of type range and one of type number. Changing either of them will generate an Ajax GET to the server who responds with the
value of the input element. That value is then imposed to the other element. The necessary javascript is in the header section
of the webpage.

A standard GET request to the server will result in the server sending the AiCwebpage.htm html file. This file should be located in the default directory. The html file uses HTML5 elements, so you need a modern browser to display the html in a correct way. Both Chrome and Firefox will do.

