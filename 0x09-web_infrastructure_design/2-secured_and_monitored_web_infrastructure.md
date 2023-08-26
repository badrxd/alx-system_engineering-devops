# 2-secured_and_monitored_web_infrastructure

## Specifics about this infrastructure `2-secured_and_monitored_web_infrastructure`

#### For every additional element, why you are adding it?
- we added firewalls to protect servers.
- we added ssl to secure connection between client and website.
- We added monitoring client to track the status of the servers.
#### What are firewalls for?
- The purpose of firewalls is to protect the serves by controlling and monitoring incoming and outgoing traffic, helping to prevent unauthorized access, cyberattacks, and data breaches.
#### Why is the traffic served over HTTPS?
- Traffic is served over HTTPS to ensure secure communication by encrypting data transmitted between clients and websites,
#### What monitoring is used for?
- Monitoring is used to observe and track systems, applications in real-time to ensure they perform well.
#### How the monitoring tool is collecting data?
- Monitoring tools collect data by regularly gathering information from servers, applications, using `Sumologic` software.
#### Explain what to do if you want to monitor your web server QPS?
- install any monitoring tools in each server , and link it with any data collector like `Sumologic` that give you the statistics about the giving information from monitoring tools
## Issues With This Infrastructure `2-secured_and_monitored_web_infrastructure`
#### Why terminating SSL at the load balancer level is an issue
- Terminating SSL at the load balancer level is an issue because there will be no connection security between the load balancer and the other servers
#### Why having only one MySQL server capable of accepting writes is an issue
- it is an issue ,if this database fails , we will not have any other source to get the data from it.
#### Why having servers with all the same components (database, web server and application server) might be a problem
- Having servers with all the same components (database, web server, application server) can be problematic because it lacks scalability and can lead to resource contention.

