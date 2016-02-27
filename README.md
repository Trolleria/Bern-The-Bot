# Bern The What'sapp Bot
A small python seed to create a Whatsapp Bot, with regex-callback routes (just like a web framework).  
(practical extension of the examples on https://github.com/tgalal/yowsup)

# Installation
1. Install the image handling system dependencies on ```bash opt/system-requirements.sh```
2. Create a virtualenv and install the requirements  ```pip install -r opt/requirements.pip```
3. Follow the instructions on ```src/config.py``` to get the whatsapp credentials.  
4. Then just run the server with  ```python src/server.py```  

To create your own views, check the ```src/router.py```, and the ```src/view/basic_views.py``` for a simple example.

