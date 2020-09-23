# Students API

## Motivation

I started this project as part of a job interview. I didn't get the position, but as I liked so much to work with REST APIs, I decided to share what I did in this repository, so I hope it helps people facing this kind of situation. The problem was to develop an API to manage the database of students of a tech school, more specifically one school of the 42 network. Here are some hot takes that I'd like to discuss before moving on to the hot stuff:


1. The first remainder is that I don't think that the option for MongoDB was the best in this case. It was helpful because I learned a lot about NoSQL databses, but regarding the nature of the data, a typical SQL database, such as SQLite, would do a great job regarding this problem.
2. My test cases could be implemented in a more professional approach, separating unit tests and integration tests. I think that `pytest` is a fantastic tool to address these issues, but a simple test framework would do the job just as great and without so much work.
3. `Docker Compose` was super useful int this context, as I guarantee that my work could run on any machine. Abetter idea would be to deploy this application with a cloud service, such as Google Cloud Run, for example.

## Installation

### With Docker Compose

Running the API server on a container is as simple as inputting `docker-compose up` on your favorite shell. The recommended version of `docker-compose` is 1.25, and you can deploy the application with the following commands. This process may take a while, so  grab a cup of tea and wait for its completion.

```
git clone git@github.com:AdrianWR/StudentsAPI.git students_api
cd students_api
docker-compose up -d
```

## Getting Started

In this tutorial we are going to use `curl` as our command line inerface to handle HTTP requests to our API. If you don't have it installed on your system, you could use the following command line to install it on a Debian based distribuition, for example:

```
# apt install update && apt install -y curl
```

This API lets their users interact with 42 São Paulo cadets data, allowing the retrieval and input of information with HTTP requests. At first, let's just test the installation of our application by viewing it's home page request

```
$ curl http://localhost:3000
```

If everything works as expected, you should see a welcoming message from the API, and therefore we'd be ready to work real stuff in our database. At this point, our database is pretty empty... So let's get started populating it with some data.

### Insert student data

The main method for inserting data inside our database is by using the HTTP `POST` method. For instance, the API is built to receive data with the following structure:

```
{
  "name": <student-name>,
  "intra_id": <student-intra-id>,
  "projects": [
    "<project1>",
    "<project2>"
  ]
}
```

The first two fields are mandatory, while the `projects` field is optional. The request body must be sent with `application/json` content type. The following examples show how to insert two registers on the API database with `curl`.

```
$ curl -X POST -H 'Content-Type: application/json' -d '{"name": "Gustavo Belfort", "intra_id": "gus", "projects": ["42cursus_libft"]}' http://localhost:3000/students
$ curl -X POST -H 'Content-Type: application/json' -d '{"name": "Guilhemar Caixeta", "intra_id": "guiga"}' http://localhost:3000/students
```

### Get students information

To get all the students currently studying at 42 SP, we may call the HTTP `GET` method on the `/students` location on our web server. If you want a bit more of control on which student you are looking for, you may pass an URL query to filter students by the projects that they may be doing right now or already done. It's possible to look for some specific student by an `id`, right after the API path.

```
$ curl http://localhost:3000/students
$ curl http://localhost:3000/students?projects=42cursus_libft
$ curl http://localhost:3000/students/1
```

### Delete student data

It's possible to delete a student data with the `DELETE` HTTP method. To delete, it's required to know the student `id` and request to the server after the `/student` URL path. To delete the student with `intra_id: "guiga"`, it can be passed the folowing request.

```
$ curl -X DELETE http://localhost:3000/students/2
```

## Testing

The tests must be executed after the deployment of the application with `docker-compose`. To run a battery of tests, just run the following command at the project root directory.

```
pytest
```
