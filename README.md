Grappling Vault is a BJJ and grappling journal application built with FastAPI and MongoDB

Prerequisites:
- Docker installed on your system
- MongoDB database (You'll need to set up your own MongoDB instance)

Quick Start:
1. Pull the image: 
docker pull bpt1901/grapplingvault:latest

2. Create a docker-compose.yml file:
version: '3.8'

services:
  app:
    image: bpt1901/grapplingvault:latest
    ports:
      - "8000:8000"
    environment:
      - MONGODB_URI=mongodb://your_mongodb_host:27017  # Replace with your MongoDB connection string
      - DATABASE_NAME=your_database_name               # Replace with your database name
    restart: unless-stopped

3. Setup your MongoDB:
- Install MongoDB on your system or use cloud Atlas
- Create a new database
- Update MONGODB_URI and DATABASE_NAME in docker-compose.yml with your values

4. Start the application:
docker compose up -d

5. Access the application at:
http://localhost:8000

Environment Variables
You must configure these environment variables:

MONGODB_URI: Your MongoDB connection string
DATABASE_NAME: The name of your MongoDB database

Database Setup

Install MongoDB:

MongoDB Installation Guide
Or sign up for MongoDB Atlas


Create a new database for the application
Update your docker-compose.yml with the appropriate connection details

Troubleshooting
Common issues:

If you can't connect to MongoDB, verify your connection string and ensure MongoDB is running
If port 8000 is already in use, change the port mapping in docker-compose.yml
Make sure your MongoDB instance is accessible from the container

Support
For issues and feature requests, please open an issue on GitHub.

