##Web Infrastructure Design Project - README
This repository contains the solutions and diagrams for the Web Infrastructure Design project, which is part of the DevOps and SysAdmin curriculum. The project is divided into four tasks, each focusing on different aspects of web infrastructure design. Below, we provide an overview of each task and the contents of this repository.

***
**Task 0: Simple Web Stack**

Description
In this task, we designed a simple web stack that hosts a website accessible via www.foobar.com. The components included a single server, a web server (Nginx), an application server, application files (code base), a database (MySQL), and a domain name (foobar.com) configured with a www record pointing to the server's IP (8.8.8.8).

Explanation
We explained the roles of each component and identified potential issues, such as Single Point of Failure (SPOF), downtime during maintenance, and scalability limitations.

***
**Task 1: Distributed Web Infrastructure**

Description
In this task, we designed a more robust infrastructure that hosts www.foobar.com using three servers. The additional components included two servers, a load balancer (HAproxy), and a database (MySQL).

Explanation
We elaborated on the rationale for each addition, discussed the load balancer's distribution algorithm, Active-Active vs. Active-Passive setup, and the workings of a Primary-Replica (Master-Slave) database cluster. We also identified issues related to Single Points of Failure, security concerns, and the absence of monitoring.

***
**Task 2: Secured and Monitored Web Infrastructure**

Description
In this task, we enhanced the infrastructure to be secure, serve encrypted traffic, and be monitored. The additional components included firewalls, an SSL certificate for HTTPS, and monitoring clients.

Explanation
We explained the reasons behind these additions, the purpose of firewalls, the importance of serving traffic over HTTPS, and the role of monitoring. We also discussed potential issues related to SSL termination at the load balancer, having only one writable MySQL server, and identical server components.

***
Task 3: Scale Up (Advanced)

Description
The advanced task involved configuring a load balancer as a cluster with another one and splitting components (web server, application server, database) onto their own servers to scale up the infrastructure.

Explanation
We provided an overview of the changes made to scale up the infrastructure.

***
Conclusion
This project allowed us to explore various aspects of web infrastructure design, from basic configurations to more advanced scaling concepts. Each task builds upon the previous one, providing a comprehensive understanding of the topic.


Feel free to reach out if you have any questions or need further clarification on any of the tasks or concepts.

Author: Daniel Kwasi Dzrekey
Date: October 28, 2023

