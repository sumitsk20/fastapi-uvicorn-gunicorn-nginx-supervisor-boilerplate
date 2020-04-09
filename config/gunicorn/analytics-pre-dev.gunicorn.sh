#!/bin/bash   

# Project directory                               
PROJECTDIR=/webapps/demo-analytics-pre-dev 
# App instance module
ASGI_MODULE=src/server.asgi
# we will communicte using this unix socket                      
SOCKFILE=/webapps/demo-analytics-pre-dev/run/unicorn_pre_dev.sock

# the user to run as
USER=demo-analytics-pre-dev
# the group to run as                                            
GROUP=webapps

# Number of Workers
NUM_WORKERS=1

WORKER_CLASS=venv/lib/uvicorn.workers.UvicornWorker

TIMEOUT=300
GRACEFUL_TIMEOUT=120
# LOGFILE=/webapps/freadom/dev/log/dev-gunicorn.log
MAX_REQUESTS=50000
MAX_REQUEST_JITTER=4

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $PROJECTDIR
source venv/bin/activate

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec venv/bin/gunicorn ${ASGI_MODULE}:app \
    --worker-class $WORKER_CLASS \
    --workers $NUM_WORKERS \
    --timeout $TIMEOUT \
    --user=$USER \
    --group=$GROUP \
    --bind=unix:$SOCKFILE \
    # --log-level=debug \
    # --log-file=$LOGFILE \
    --max-requests=$MAX_REQUESTS \
    --graceful-timeout=$GRACEFUL_TIMEOUT
    --max-requests-jitter=$MAX_REQUEST_JITTER
