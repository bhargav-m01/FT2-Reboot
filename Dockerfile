FROM python:3.8.2
COPY . /reboot
WORKDIR /reboot
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]