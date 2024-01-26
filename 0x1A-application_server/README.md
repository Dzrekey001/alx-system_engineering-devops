##Application Server Project

###Overview
This project focuses on setting up an application server in conjunction with Nginx to serve dynamic content for an Airbnb clone project. The application server setup involves using Gunicorn as the WSGI server to run Flask applications. Nginx is configured to proxy requests to the Gunicorn instances, enabling the serving of dynamic content and APIs.
***

###Project Tasks
0. Set up development with Python
Cloned the Airbnb clone v2 project onto web-01.
Configured Flask application to serve content from the route /airbnb-onepage/ on port 5000.
1. Set up production with Gunicorn
Installed Gunicorn and necessary libraries on web-01.
Configured Gunicorn to serve content from the same route as Task 0.
Verified Gunicorn functionality by binding it to localhost on port 5000.
2. Serve a page with Nginx
Configured Nginx to serve content from the route /airbnb-onepage/ both locally and on its public IP on port 80.
Configured Nginx to proxy requests to the Gunicorn process listening on port 5000.
3. Add a route with query parameters
Configured Nginx to proxy requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) to a Gunicorn instance listening on port 5001.
Enabled Nginx to serve this page both locally and on its public IP on port 80.
4. Serve your API
Cloned the Airbnb clone v3 project onto web-01.
Configured Nginx to route requests to the route /api/ to a Gunicorn instance listening on port 5002.
Enabled Nginx to serve this page both locally and on its public IP on port 80.
5. Serve your Airbnb clone
Cloned the Airbnb clone v4 project onto web-01.
Configured Gunicorn to serve content from web_dynamic/2-hbnb.py on port 5003.
Configured Nginx to serve the root route (/) to the Gunicorn instance and serve static assets properly.
6. Deploy it!
Wrote a systemd script to start a Gunicorn process serving content from web_dynamic/2-hbnb.py on port 5003.
Enabled the systemd service to start on boot.
7. No service interruption
Developed a Bash script to reload Gunicorn gracefully, allowing for updates without downtime.
