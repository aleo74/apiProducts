FROM python:3.10

ENV USERNAME=app
ENV WORKING_DIR=/home/app

WORKDIR ${WORKING_DIR}

COPY app app
COPY requirements.txt .
COPY main.py .
COPY .env .

RUN groupadd ${USERNAME} && \
    useradd -g ${USERNAME} ${USERNAME}

RUN chown -R ${USERNAME}:${USERNAME} ${WORKING_DIR}
RUN chmod -R u=rwx,g=rwx ${WORKING_DIR}

RUN pip install -r requirements.txt

ENV PORT 50001
EXPOSE 50001

CMD ["python", "-u", "main.py"]