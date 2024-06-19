# Project badge

![Project Badge](badge-url)

**Completion:** 100%

**Title:** RESTful API

**Level:** Novice

**By:** Javier Valenzani

**Weight:** 1

**Migrated to checker v2:** 

Your score will be updated as you progress.  
Manual QA review must be done (request it when you are done with the project)

## Introduction

In the evolving world of software development, understanding how to communicate and transfer data efficiently between systems is essential. This project delves into the domain of RESTful APIs, a cornerstone in the realm of web services. The Representational State Transfer (REST) architecture is a set of constraints that ensure a scalable, stateless, and cacheable communication system. This approach allows for the easy integration of web services, making them accessible to a wide range of applications.

## Learning Objectives

- **HTTP/HTTPS Basics:** Grasp the foundational principles of the web’s primary protocol, understanding how data transfer occurs, methods involved, and the difference between the secure and non-secure versions.
  
- **API Consumption with Command Line:** Hands-on experience in interacting with APIs using basic command-line tools, laying the groundwork for more advanced interactions.
  
- **API Consumption with Python:** Elevate your data fetching skills by leveraging Python’s capabilities, allowing for more advanced processing and data manipulation.
  
- **API Development with http.server:** Understand the basics of crafting an API from scratch using Python’s built-in modules, setting a solid foundation.
  
- **API Development with Flask:** Dive deeper into API development using the lightweight Flask framework, focusing on routing, data management, and scalability.
  
- **API Security & Authentication:** Address the crucial aspect of security, understanding how to protect data transfer and ensure only authorized access to resources.
  
- **API Standards & Documentation with OpenAPI:** Conclude with the importance of maintaining standardized documentation, ensuring that APIs are usable, understandable, and maintainable.

## Importance

In our interconnected digital age, RESTful APIs play a pivotal role in the integration of different systems. They serve as the middlemen, translating requests into understandable actions, fetching data, or triggering procedures. From social media platforms sharing data with advertisement agencies to complex industrial systems communicating with each other for automation, APIs are ubiquitous.

Developing a solid understanding of how to consume, develop, secure, and document these APIs equips you with a critical skill set. It’s a blend of understanding both the technical intricacies and the larger design picture, ensuring seamless and efficient communication in the digital world.

## REST API Conceptual Diagram


```sql
+-------+           +-------+           +---------+           +---------+
|       |  Request  |       |  Process  |         |  Fetch/   |         |
|       |   ----->  |       |  -------> |         |  Modify   |         |
|       |           |       |           |         |  -------> |         |
|       | <-----    |       | <-------  |         |           |         |
|       |  Response |       |  Return   |         |           |         |
+-------+           +-------+           +---------+           +---------+
  Client            Web Server           API Server           Database
```
AUTHOR : BAPTISTE POUQUEROU
# Tasks Overview

| Task Number | Task Title                                    | Description                                                                                                                                                                                                           |
|-------------|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0           | Basics of HTTP/HTTPS                          | Differentiate between HTTP and HTTPS, understand HTTP requests and responses, recognize common HTTP methods and status codes.                                                                                         |
| 1           | Consume data from an API using command line tools (curl) | Install and use curl to interact with HTTP APIs, construct and execute basic API requests, interpret API responses.                                                                                                     |
| 2           | Consuming and processing data from an API using Python | Use the requests library in Python to send HTTP requests, parse and manipulate JSON data, convert data to CSV format.                                                                                                  |
| 3           | Develop a simple API using Python with the `http.server` module | Set up a basic web server using Python's http.server module, handle HTTP requests (GET, POST), serve JSON data in response to specific endpoints.                                                                       |
| 4           | Develop a Simple API using Python with Flask   | Set up a Flask application to define routes, handle HTTP requests (GET, POST), serve JSON data, implement basic authentication, and handle role-based access control using JWT tokens.                              |
| 5           | API Security and Authentication Techniques     | Understand API security concepts, implement basic authentication using Flask-HTTPAuth, set up token-based authentication with JWT using Flask-JWT-Extended, differentiate between authentication and authorization.   |
| 6           | API Standards and Documentation using OpenAPI  | Create an OpenAPI specification for an API using Swagger Editor, integrate OpenAPI with Flask using Flask-RESTx, generate and serve live API documentation with Swagger UI.                                           |

AUTHOR : BAPTISTE POUQUEROU