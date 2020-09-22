# 42SP_API

## Installation

### With Docker Compose (Recommended)

Running the API server on a container is as simple as inputting `docker-compose up` on your favorite shell. The recommended version of `docker-compose` is 1.25, and you can deploy the application with the following commands. This process may take a while, so  grab a cup of tea and wait for its completion.

```
git clone git@github.com:42sp/full-time-selection-process-AdrianWR.git 42sp_api
cd 42sp_api
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