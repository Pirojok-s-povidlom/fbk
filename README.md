# fbk

This is a test uwsgi+nginx application.

Past this form below to browsers address bar and follow:
```data:text/html,<form action=http://localhost:8080/ method=post><input name=message></form>```

Past the message in the form and press Return

To get all posted entries use the common GET request to http://localhost:8080/

To disable GET requests uncomment script ```fbk/nginx/prestart.sh```
