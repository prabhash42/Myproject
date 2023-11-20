**Main Project - Getting Started**

This project involves a microservice that will interface with The Movie Database (TMDb) API to fetch and return filmography data, top-rated movies by year, and detailed movie information based on user queries. The microservice uses The Movie Database (TMDb) API and communicates through a RabbitMQ server. The main project runs from the files: main.py, and myFunctions.py

**Requirements**

Install RabbitMQ.
Install Python libraries: requests, pika.
Obtain an API key from TMDb here: https://www.themoviedb.org/settings/api

**Microservice - Set Up**
The microservice is implemented in the file: musicMicro.py.

This microservice is designed to take a movie title (string value) through a RabbitMQ server and returns the name(s) of the composer(s) and a URL to the movie's cast and crew page on TMDb.

**Microservice Communication**

This microservice uses a "Request-Reply" pattern within RabbitMQ.

**Requesting Data**

To request data from musicMicro.py, establish a connection to the RabbitMQ server and declare the appropriate queue.
![7](https://github.com/prabhash42/Myproject/assets/114190627/2b868971-03d8-4719-b7f5-58e47b676fef)
![8](https://github.com/prabhash42/Myproject/assets/114190627/7d142982-bbd8-4316-b4bd-f5dea4325a87)

To send a request message to this queue (Note: musicMicro.py is expecting to receive a string-type movie title).
![9](https://github.com/prabhash42/Myproject/assets/114190627/e01ee7eb-2d99-4c57-b605-e14515633708)

**Receiving Data**

musicMicro.py will return the requested data based on the message it was sent. To receive this data, define the consume attributes of the RabbitMQ server, set up a callback function, and start "consuming" data.
![4](https://github.com/prabhash42/Myproject/assets/114190627/ae05cfc9-d626-43c2-81be-7624b632ceac)
![5](https://github.com/prabhash42/Myproject/assets/114190627/8199c243-c7a0-4ef3-b05c-dbed45d1d0b3)
![6](https://github.com/prabhash42/Myproject/assets/114190627/580e16c4-0b59-4305-97a9-5d45b13d3436)

**Communication Example**

Here is an example of the full communication loop in action. The process involves sending a request from the client and receiving a response from the microservice.

![z](https://github.com/prabhash42/Myproject/assets/114190627/e7d4c7b6-8928-40fc-903c-06311f41fe6c)

**UML Sequence Diagram**

UML sequence diagram here that visually represents the request-reply pattern between the client (partnerProject.py) and the microservice (songMicro.py).
