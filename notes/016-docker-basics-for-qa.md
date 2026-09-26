# Docker Basics for QA

## Why it matters
Docker packages an application together with everything it needs to run (code, dependencies, configuration) into a portable unit called a container. This eliminates the classic "works on my machine" problem and is essential for isolating test environments — e.g. spinning up a test database without installing it directly on the host machine.

## Core concepts

- **Image** — a template/blueprint for an application (e.g. "Postgres 16"). Doesn't run anything by itself.
- **Container** — a running instance created from an image. Multiple containers can be created from the same image.

Analogy: Image = a cake recipe. Container = the actual baked cake. You can make many cakes from the same recipe.

## Core commands

```bash
docker --version                    # check Docker is installed
docker pull image_name              # download an image
docker images                       # list downloaded images
docker run image_name               # create + start a container from an image
docker ps                           # list running containers
docker ps -a                        # list ALL containers, including stopped ones
docker stop container_name          # stop a running container
docker rm container_name            # remove a stopped container
docker logs container_name          # view a container's logs (useful for debugging)
docker exec -it container_name bash # run a command inside a running container
```

## Useful flags for `docker run`

```bash
docker run -d image_name                        # -d = detached, runs in background
docker run -p 8080:80 image_name                 # -p = port mapping (host:container)
docker run --name my_container image_name        # give it a memorable name
docker run -e VARIABLE=value image_name          # -e = set an environment variable
```

## Practical exercise: spinning up a test database

```bash
docker run -d --name test-postgres -e POSTGRES_PASSWORD=test123 -p 5432:5432 postgres:16
```

Connecting to it directly:
```bash
docker exec -it test-postgres psql -U postgres
```

From there, standard SQL applies exactly as covered in the SQL Basics notes:
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO users (name, email) VALUES ('Ioan Manolache', 'ioan@test.com');

SELECT * FROM users WHERE name LIKE '%Ioan%';
```

Cleaning up afterward (no trace left on the system):
```bash
docker stop test-postgres
docker rm test-postgres
```

## QA use case
Instead of installing a database directly on a laptop (messy, risks conflicting with other projects), a test database can be spun up in an isolated container, used for a test session, then removed completely — clean and repeatable every time.

## Docker Compose (concept only)
When multiple containers need to work together (e.g. an app + a database), a `docker-compose.yml` file can start them all at once:
```bash
docker-compose up
docker-compose down
```
