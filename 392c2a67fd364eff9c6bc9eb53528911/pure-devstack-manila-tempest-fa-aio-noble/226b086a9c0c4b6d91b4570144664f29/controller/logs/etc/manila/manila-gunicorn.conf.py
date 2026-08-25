# Manila gunicorn configuration for devstack
# Matches uWSGI settings: 4 workers, 10s timeout
bind = "192.168.1.121:18786"
workers = 4
timeout = 10
proc_name = "manila-api"
