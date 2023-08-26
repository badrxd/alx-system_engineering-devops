# 1-distributed_web_infrastructure

## Specifics about this infrastructure `1-distributed_web_infrastructure`

#### What is a server?
- We add load balancer to redirect the request to server who is available or not in pressure
#### What distribution algorithm your load balancer is configured with and how it works?
- The load balancer HAProxy is configured with the Round Robin distribution algorithm. this algorithm pass each request gets assigned to each server one by one and the round goes on.
#### Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both ?
- In our case the load-balancer enabling Active-Passive, all the requset redirect the the first server, the difirance bitween them is the Active-Active setup make all servers in the server pool actively participate in handling incoming traffic, and Active-Passive setup, only one server (the "active" server) handles incoming traffic while the other servers (the "passive" servers) are on standby
#### How a database Primary-Replica (Master-Slave) cluster works?
- The database `Primary` handles write operations (inserts, updates, deletes) from applications and clients. the database `Replica` is a copy of the database `Primary` , is handle read operations (select queries) from applications and clients. and in case the database `Primary` fails the first database `Replica` become the new database `Primary`.
#### What is the difference between the Primary node and the Replica node in regard to the application?
- The database `Primary` handles write operations (inserts, updates, deletes) from applications and clients. the database `Replica` is a copy of the database `Primary` , is handle read operations (select queries) from applications and clients. and in case the database `Primary` fails the first database `Replica` become the new database `Primary`.

## Issues With This Infrastructure `1-distributed_web_infrastructure`
#### SPOF
- In this Infrastructure there is many SPOF : like the whole server or the web server or the app server or the database.
#### Security issues (no firewall, no HTTPS)
- the connection between the client and the server not secure by `HTTPS` just usinf `HTTP`, anyone can see the content of the request and response, plus the server are not protected from the cyberattacks becuse there is no firewall to do that.
#### No monitoring
- Because there is no monitoring software , we can 't know the status of each server
