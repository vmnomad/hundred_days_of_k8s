# 100daysofk8s.io web site

The web site was created primarily for learning purpose to familiarise myself with a process of building the web server from the scratch.

Another important goal of this web site is to promote containers orchestration.

The web app is created using Django framework. 

There are few simple tests to validate that all pages are available.

To learn CI/CD process I used CircleCI that does the following:
1. On every commit Githab will use webhook to notify CircleCI that code was updated
2. CircleCI will use the configuration provided in .circleci/config.yml file to:
  * Build the app using Dockerfile
  * Run Django tests
  * Push the updated code to AWS EC2 instance provided that tests were completed successfully
  * Stop and Delete running container
  * Build and Start a new container running updated code

The web server is built using Nginx as a reverse proxy server that serves requests via Gunicorn. 

Initial docker container was build using generic Python image, however, it turned out to be huge - 1.4GB for a very small and simple web site. To reduce image footprint the image was replaced with Alpine Python version which brought image size to 300MB.

I am pretty sure it could have been done better given that it was my first experience with pretty much all products used here, so feel free to leave a comment/suggestion on how to improve it. 