
# Sentry to Zoho Cliq Webhook Forwarder

This project is a FastAPI application that receives error notifications from Sentry via webhooks and forwards them to a Zoho Cliq channel using Zoho Cliq’s webhook.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
  - [Requirements](#requirements)
  - [Configuration](#configuration)
  - [Docker Compose](#docker-compose)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Troubleshooting](#troubleshooting)

---

## Features

- **Webhook Forwarding**: Receives Sentry events via webhook and forwards them to Zoho Cliq.
- **Dockerized**: Runs as a Docker container, making it easy to deploy.
- **Environment-based Configuration**: Configurable using environment variables or JSON configuration.

## Setup

### Requirements

- Python 3.8+
- Docker and Docker Compose
- Accounts for [Sentry](https://sentry.io) and [Zoho Cliq](https://www.zoho.com/cliq/)

### Configuration

1. **Zoho Cliq Webhook URL**: Create a webhook URL in Zoho Cliq for a specific channel.
   
2. **Sentry Webhook**: In Sentry, configure a webhook integration pointing to the FastAPI app's `/sentry-webhook` endpoint.

3. **.env**: 

   Create a `.env` file in the root directory for environment-based configuration. Add your Zoho Cliq Webhook URL:

   ```plaintext
   ZOHO_CLIQ_WEBHOOK_URL="your_zoho_cliq_webhook_url_here"
   HOST_PORT=80          
   ```

### Docker Compose

1. **Dockerfile**: Builds the FastAPI app in a container.
   
2. **docker-compose.yml**: Defines the service and configuration.

Run the application using Docker Compose:

```bash
docker-compose up -d
```

This will start the FastAPI app on `http://localhost:80`.

## Usage

Once the application is running:

1. Set the Sentry webhook URL to `http://localhost:80/sentry-webhook` (or your server URL).
2. When Sentry sends an event, the FastAPI app will receive it and forward the message to Zoho Cliq.

## API Endpoints

### `POST /sentry-webhook`

Receives incoming webhooks from Sentry and forwards the details to Zoho Cliq.

### `GET /`

Basic endpoint to verify the server is running.

## Troubleshooting

- **Environment Variables**: Ensure `ZOHO_CLIQ_WEBHOOK_URL` is set in either `config.json` or `.env`.
- **Docker Logs**: Check container logs for errors:

  ```bash
  docker-compose logs -f
  ```

---

This setup allows for easy webhook forwarding from Sentry to Zoho Cliq, making it a convenient solution for alert notifications in your team channel.
