# Google Cloud IoT setup [DEPRECATED]

## Requirements

- An active Google Cloud account
- Google cloud cli

## Instructions

Create topic
```
gcloud pubsub topics create clintelli-test-topic1 --project=PROJECT_ID
```

Create a subscription to the topic above
```
gcloud pubsub subscriptions create clintelli-test-sub1 --topic-project=PROJECT_ID --topic=clintelli-test-topic1 
```

if you want to avoid specifying each time the project with `--project` flag you can run the following
```
gcloud config set project PROJECT_ID
```

Create IoT registry
```
gcloud iot registries create clintelli-test-registry1 --region=europe-west1 --event-notification-config=topic=clintelli-test-topic1
```

Generate certificates
```
openssl req -x509 -newkey rsa:2048 -keyout clintelli-test-rsa_private.pem -nodes -out rsa_cert.pem -subj "/CN=unused"
openssl ecparam -genkey -name prime256v1 -noout -out clintelli-test-ec_private.pem
openssl ec -in clintelli-test-ec_private.pem -pubout -out clintelli-test-ec_public.pem
```

Store above certificates safely and use them to create a device
```
gcloud iot devices create 'clintelli-test' --region=europe-west1 --registry=clintelli-test-registry1 --public-key=path=./clintelli-test-ec_public.pem,type=es256
```