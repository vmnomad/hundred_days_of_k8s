# 100daysofk8s.io web site

The web site is build primarily for learning purpose to familiarise myself with a process of building the web server from the scratch.

Another important goal of this web site is to promote containers orchestration

The web app is created using Django framework. 

There are few simple tests to validate that all pages are available.

To learn CI/CD process I used CircleCI that does the following:
1. On every commit Githab will use webhook to notify CircleCI that code was updated
2. CircleCI will use the configuration provided in .circleci/config.yml file to:
  * Build the app using Dockerfile
  * Run Django tests
  * Push the updated code to AWS EC2 instance provided that tests were completed successfully


**The bot requires the following ENV variables for authentication:**

- CONSUMER_KEY
- CONSUMER_SECRET
- ACCESS_TOKEN
- ACCESS_TOKEN_SECRET

**Another ENV variable is required to set the keyword for tweets:**
- KEYWORD

**To run the bot in the container update the above mentioned variables in the dockerfile before building the image**
