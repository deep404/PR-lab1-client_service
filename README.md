# PR-lab1-dining_room

# PR-lab1-kitchen

> Network Programming Laboratory Work No1 [Client Service]
>
> FAF 192
>
> Moglan Mihai
> 

More detailed README will be added later!

#### Run

```bash
$ docker build -t client_service . # create kitchen image
$ # the docker network (pr_lab1) was created when running kitchen image
$ # now just run the client_service image on the same network as kitchen, dining and food_ordering 
$ docker run -d --net pr_lab1 --name client_service client_service # run docker container on created network
```

