# 0-simple_web_stack

## Specifics about this infrastructure `0-simple_web_stack`

#### What is a server?
- Server is a computer it can be a a real or virtual computer that provides resources and data and services, to other computers, known as clients.
#### What is the role of the domain name?
- We access to website using ip , like this one `8.8.8.8`, this format it hard for human to remember it , that way they came with the idea to creat domain name that's will be easy to remember like this one `www.google.com`
#### What type of DNS record www is in www.foobar.com?
- This domain name use A record , you can check that using this website `www.foobar.com`, or this linux command `dig www.foobar.com`
#### What is the role of the web server?
- The role of web server is accept the http request and send back the static files or the error message to the clients
#### What is the role of the application server?
- Hosts and manages web applications, handling tasks like running code, managing resources,
#### What is the role of the database?
- The role of the database is using it to store data on it in organised way
#### What is the server using to communicate with the computer of the user requesting the website?
- The user use the internet to com with the website

## Issues With This Infrastructure `0-simple_web_stack`
#### SPOF
- In this Infrastructure there is many SPOF : like the whole server or the web server or the app server or the database
#### Downtime when maintenance needed (like deploying new code web server needs to be restarted)
- in this Infrastructure we have just one server if we want to do maintenance we need to turn off the server, and that will make the website unreachable to him
#### Cannot scale if too much incoming traffic
- in this Infrastructure it's not easy to be scaled everything in one server, we need to change the all the backend Infrastructure
