# easyFinder

## Description

A website that uses dlib library to identify people in images. The website is built using Flask and the face recognition is done using the face-recognition library and MongoDB is used as the database.

## Features

- Upload an image and identify the people in it
- Search for images of a missing person in a database of images
- Add images and details of a missing person to the database

## Installation

1. Clone the repository
2. Create a virtual environment using `python -m venv .venv`
3. Install the requirements using `pip install -r requirements.txt`
4. Run the app using `python app.py`

## Docker Installation

Image available at:
[rohana001/easy-finder](https://hub.docker.com/r/rohana001/easy-finder)

To run locally using Docker:

1. Pull the Docker image from the Docker Hub: `docker pull rohana001/easy-finder`
2. Run the container, specifying the desired port: `docker run -p <PORT>:5000 rohana001/easy-finder`
