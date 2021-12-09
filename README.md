# Spotify ETL Data Pipeline

---

## Table of Contents

1. [Introduction](#introduction)
2. [Technology](#Tech)
3. [Architecture](#Architecture)
4. [Improvements](#Improvements)
5. [Refrences](#Refrences)

---

## Intoduction <a name="Introduction"></a>

This is a tool that gathers data from selected Spotify plalists and uploads it to a data lake in AWS S3 for analysis.

---

## Technology <a name="Tech"></a>

The technology that was used for this includes :

* [Amazon Web Services (AWS)](https://aws.amazon.com/)
  * Used to Create the Data Pipeline
* [Python](https://www.python.org/)
  * Used as the Primary Development Language
* [Spotipy](https://spotipy.readthedocs.io/)
  * Used to Access the Spotify API
* [Terraform](https://www.terraform.io/)
  * Used to Create the Infrastructure as Code

---

## Architecture <a name="Architecture"></a>

![Architecture Diagram](/Images/Architecture_Diagram.PNG)

The terraform scripts are used to:

* Create a Lambda function
* Set IAM policies/Roles
* Create a CloudWatch alarm
  
---

## Improvements <a name="Improvements"></a>

* Analysis Capabilities
  * Add Live Analysis
  * Improve Visualizations
* Code Quality
  * Terraform File Formatting

---

## Refrences <a name="Refrences"></a>

* [Youtube Project Reference Link](https://www.youtube.com/watch?v=iYpoKQZP3EU)
* [Youtube Terraform Reference Link](https://www.youtube.com/watch?v=vwn77cUarTs&list=PL8HowI-L-3_9bkocmR3JahQ4Y-Pbqs2Nt)
* [Spotify API Examples](https://betterprogramming.pub/how-to-extract-any-artists-data-using-spotify-s-api-python-and-spotipy-4c079401bc37)