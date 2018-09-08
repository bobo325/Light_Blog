From python:3.5

RUN mkdir -p /home/chenbo/Light_Blog

WORKDIR /home/chenbo/Light_Blog

ADD light_blog /home/chenbo/Light_Blog/light_blog
ADD celery_runner.py /home/chenbo/Light_Blog/celery_runner.py
ADD fa /home/chenbo/Light_Blog/fa
ADD fake_data.py /home/chenbo/Light_Blog/fake_data.py
ADD manage.py /home/chenbo/Light_Blog/manage.py
ADD requirements.txt /home/chenbo/Light_Blog/requirements.txt
ADD README.md /home/chenbo/Light_Blog/README.md

RUN pip install -i https://mirrors.ustc.edu.cn/pypi/web/simple/ -r /home/chenbo/Light_Blog/requirements.txt

VOLUME /home/chenbo/Light_Blog/temp/

EXPOSE 80 5000 

CMD python manage.py runserver --host 0.0.0.0 --port 5000
