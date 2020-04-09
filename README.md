# FastApi Boilerplate

This is an example template on how you can structure your Fatsapi project. It includes deployment configuration for **Nginx**, **Gunicorn** and **Supervisor**.

## Quickstart

> **NOTE**: Install **Python >= 3.6** as most of project dependencies are not compatible below that version.

### 1. Clone Repository

```bash
$ git clone <project-git-url>
```

Change your directory to cloned repository usind 

``` bash
$ cd backend-demo-analytics
```

There is `setup.sh` script at root. You can execute it using `source ./setup.sh` and it will do all the work for you.


### 2. Setup and activate VirtualEnv

Inside your cloned repository directory, run following commands:

``` bash
$ python3 -m venv venv
```
``` bash
$ source venv/bin/activate
```
``` bash
$ pip install -r requirements.txt
```

### 3. Start the server

Once all dependencies are installed, you can start your server via terminal using `manage.py` script.

``` bash
$ python src/manage.py serve
```
and kill the server using `ctrl+c`.

> **Note:** Make sure you create a `.env` file outside `src` folder and change environment variables as per your requiremnts that are being used in `core.settings.py`.


## Behind the code.

Developed using [FastApi](https://fastapi.tiangolo.com/) & [Uvicorn](https://www.uvicorn.org/).
