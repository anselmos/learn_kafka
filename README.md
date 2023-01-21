# Learn Apache Kafka

A project to learn how to use Apache Kafka.
Using Docker for convenience and applying python client.

# How to use it:

## Start Apache Kafka

To start the Apache Kafka broker with Zookeper using `docker-compose.yml` use:

```bash
docker-compose up -d
```

## Create new topic:

Create new topic for the broker by updating `create-topic.py` name of the topic (or using default `quickstart` ) and running it with:

```bash
pipenv run python create-topic.py
```

## Run Producer with topic name:

Update the `producer.py` with the same topic name (or use the default one) used in `create-topic.py` 

```bash
pipenv run python producer.py
```


## Run Consumer to view data from topics:

Update the `consume.py` with the same topic name (or use the default one) used in `create-topic.py`

```bash
pipevn run python consume.py
```

# Links

- https://developer.confluent.io/quickstart/kafka-docker/
- https://kafka-python.readthedocs.io/en/master/usage.html
- https://stackoverflow.com/questions/26021541/how-to-programmatically-create-a-topic-in-apache-kafka-using-python
- https://stackoverflow.com/a/55524560
