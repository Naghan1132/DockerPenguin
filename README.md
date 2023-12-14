# Penguin Race Prediction Docker

A Dockerized client-server application for predicting the race of penguins.


![Predictions](
https://private-user-images.githubusercontent.com/66120091/290568170-191c1142-8518-49f7-8d46-43ddf72b5172.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDI1NjgyNjUsIm5iZiI6MTcwMjU2Nzk2NSwicGF0aCI6Ii82NjEyMDA5MS8yOTA1NjgxNzAtMTkxYzExNDItODUxOC00OWY3LThkNDYtNDNkZGY3MmI1MTcyLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzEyMTQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMjE0VDE1MzI0NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTk4NGY1OGRmNmVjYjZhNDY2MzNiMWY5NGViZjk4NWQyYzJhYWZkOTZhZjlkZTVhNzRiNzUyMmMxN2M3MTVjMWYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.sbBsBATbYf1yGe4PpbEak-cAfUFc6NnRzczXt-HqAq4
)

## Overview

This project utilizes a client-server architecture for predicting the race of penguins. The server hosts the prediction model, while the client interacts with the server to make predictions.

## Prerequisites

Before getting started, make sure you have the following installed:

- Docker (docker-compose)

## Getting Started

To use this application, follow these steps:

### Installation

Clone the repository and build the Docker image:

```bash

git clone https://github.com/Naghan1132/DockerPenguin.git
cd DockerPenguin
docker-compose up
```

## Explore and make predictions

Go to : ```http://172.18.0.4:8501/```  to visit the app

