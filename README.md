# Analysis_Taxis_NY
Insight analysis over information from https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

# About me
Hello, everyone reading this, as of the realization of this project i'm a computer engineering student, in which i got interested in Data Anlsysis and Cibersecurity, i'll be developing some projects around those areas in future repositories, keep in mind i can make mistakes but i'll do my best to always deliver the best i can offer, and of course i'll be updating some of these projects if nedded, feel free to comment on my work so i can see if i can do something different any kind of critiscim is welcome, i'll be more than happy to keep developing my skills around that, so without further to do, Welcome everyone, let me introduce you to the next project you are about to read, the following was executed during my bootcamp of Data Analyst Jr. so like always feel free to use it modify it or add comments about it.

First of all lets talk about the tools i got to use during my development:

## Tools
* Python (Version 3.12.3)
* SQL (I normaly use the administration platform postgreSQL/PgAdmin, but feel free to use the one you prefer such as MySQL Workbench)
* Power BI (Mostly for the dashboard and insight presentation)

## Requirements (Necesary libraries to run the code)
* certifi==2024.2.2
* charset-normalizer==3.3.2
* colorama==0.4.6
* greenlet==3.0.3
* idna==3.7
* numpy==1.26.4
* pandas==2.2.2
* pandas-stubs==2.2.2.240514
* psycopg2==2.9.9
* pyarrow==16.1.0
* python-dateutil==2.9.0.post0
* python-dotenv==1.0.1
* pytz==2024.1
* requests==2.32.3
* six==1.16.0
* SQLAlchemy==2.0.30
* tqdm==4.66.4
* types-pytz==2024.1.0.20240417
* types-requests==2.32.0.20240523
* types-tqdm==4.66.0.20240417
* typing_extensions==4.12.0
* tzdata==2024.1
* urllib3==2.2.1

## Project Structure 
* Datawarehouse on SQL (Data storage)
* Pipeline on Python (Extract)
* Cleaning and enrichment of data (Transform)
* Load data from datalake to datawarehouse (Load)
* Data Analysis (I'm going to use a python notebook so i can leave my insights)
* Power BI Dashboard (Then i will add a drive link so you can get to see the dashboards created, for the data presentation)

## Aditional Resources 
https://github.com/DataTalksClub/data-engineering-zoomcamp

## Data Dictionary (Green Taxi Trips Data Dictionary)
https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_green.pdf

## Instructions of use 
* After you clone the repository, you have to create using postgreSQL a localhost, with a super user, passsword and port, you will run the file db_creation.ps1 
* Afterwards we got to run the generals file (both of them), keep in mind you have to create a .env file in which you will add the postgres host, user, password and port to use like so: "POSTGRES_HOST = localhost" and so on with the rest.
* Then we got to download the data from the website provided so we run the file raw_data_download.
* Afterwards we have to run the clean data script to get rid of all the unnecesary information we got from the download.
* Finally we grab the data from the clean data directory created into your files dump and we procced to upload the data.
* Once in pgAdmin we verify that the rows are actually created by simply counting the rows or showing the first 100 rows.
* We proceed to create a ODBC connection between our new DB, so we can use it on power BI.
* We create a new file on Power Bi, we select the option Obtain Data, we write ODBC and select that, we will be promptede with a drop down option panel, we select an instance that we created prior with Data origin ODBC, we used ODBC (16.0.0.0).
* Then we transform our data if necesary and preapare the dashboards for our report.