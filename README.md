# README: Setting Up and Accessing MySQL with Docker and Flask

This guide explains the steps to set up a MySQL database inside a Docker container, create a table, insert sample data, and use a Flask application to access and display the data.

## Step-by-Step Explanation

### Step 1: Run a MySQL Docker Container
```bash
docker run -itd --name os1 -e MYSQL_ROOT_PASSWORD=redhat -e MYSQL_DATABASE=db -e MYSQL_USER=faizan -e MYSQL_PASSWORD=redhat mysql
```
- **docker run**: Run a new container.
- **-itd**: Start the container in interactive mode (-i), attach a terminal (-t), and run in detached mode (-d).
- **--name os1**: Assign the name `os1` to the container.
- **-e MYSQL_ROOT_PASSWORD=redhat**: Set the root password for MySQL as `redhat`.
- **-e MYSQL_DATABASE=db**: Create a database named `db` inside MySQL.
- **-e MYSQL_USER=faizan**: Create a MySQL user named `faizan`.
- **-e MYSQL_PASSWORD=redhat**: Set the password for user `faizan` as `redhat`.
- **mysql**: Use the official MySQL image.

### Step 2: Access the Container
```bash
docker exec -it os1 bash
```
- **docker exec**: Run a command inside a running container.
- **-it os1 bash**: Open an interactive bash shell in the `os1` container.

### Step 3: Access MySQL
```bash
mysql -u faizan -p redhat
```
- **mysql**: Launch the MySQL client.
- **-u faizan**: Log in as user `faizan`.
- **-p redhat**: Provide the password `redhat` for user `faizan`.

### Step 4: Create a Table and Insert Data
```sql
show databases;
use db;
create table students (id int(5), name char(200), city char(10));
insert into students values (1, "faizan","pune");
```
- **show databases;**: List all available databases.
- **use db;**: Switch to the `db` database.
- **create table students (...);**: Create a table named `students` with columns `id`, `name`, and `city`.
- **insert into students values (...);**: Insert a row with values `1`, `"faizan"`, and `"pune"` into the `students` table.

### Step 5: Exit the Container
```bash
exit
```
- Exit the MySQL client and the container shell.


## Step 6 : Inspect Container for IP Address
```bash
docker inspect os1
```
- **Retrieves the container details, including its IP address. This IP will be used in the Python application.

## Step 7: Modify the Python Application

```bash
vim app.py
```
-- **Opens the app.py file in the Vim editor.
-- **Updates the IP address in the application to match the MySQL container's IP.


### Step 8: Build a Flask Application Docker Image
```bash
docker build -t mypyos1 .
```
- **docker build**: Build a Docker image.
- **-t mypyos1**: Tag the image as `mypyos1`.
- **.**: Use the `Dockerfile` in the current directory to build the image.

### Step 9: Run the Flask Application
```bash
docker run -it mypos1
```
- **docker run**: Start a container from the `mypos1` image.
- **-it**: Run in interactive mode with a terminal attached.

### Step 10: Access the Flask Application
Open a web browser and navigate to:
```
http://<container_ip>:5000/data
```
Replace `<container_ip>` with the IP address of the container.

This will display the data fetched from the `students` table in the MySQL database.

---

## Required Files

### Dockerfile
Ensure the `Dockerfile` includes the necessary instructions to set up Flask and connect to the MySQL database.

### Flask Application Code (app.py)
The Flask app should connect to the MySQL database and define a route `/data` to fetch and display the `students` table data.

---

## Example Output
When you access `http://<container_ip>:5000/data`, you should see:
```json
[
    {
        "id": 1,
        "name": "faizan",
        "city": "pune"
    }
]

