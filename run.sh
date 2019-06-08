PROCESS=$(lsof -n -i4TCP:8000 | grep LISTEN | awk '{ print $2 }')
if [ -n "$PROCESS" ]
then
    kill $PROCESS   
fi;

python manage.py runserver 0.0.0.0:8000