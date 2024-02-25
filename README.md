# Flask Data Analysis API
This Flask application serves as an API for analyzing user data related to orders and payments in an e-commerce store. The application includes endpoints for retrieving total spending by age, average spending in specific age ranges, and writing data to a MongoDB database.
<img src="https://www.donskytech.com/wp-content/uploads/2023/04/Flask-REST-API-Server-for-Sensors.png?ezimgfmt=ng:webp/ngcb1">
## Built With
- **Python:**
  <a href="https://www.python.org/" target="_blank">
    <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python" width="100">
  </a>
- **Flask:**
  <a href="https://flask.palletsprojects.com/" target="_blank">
    <img src="https://flask.palletsprojects.com/en/2.0.x/_images/flask-logo.png" alt="Flask" width="100">
  </a>

- **SQLite:**
  <a href="https://www.sqlite.org/" target="_blank">
    <img src="https://www.sqlite.org/images/sqlite370_banner.gif" alt="SQLite" width="100">
  </a>

- **MongoDB:**
  <a href="https://www.mongodb.com/" target="_blank">
    <img src="https://webassets.mongodb.com/_com_assets/cms/mongodb-logo-rgb-j6w271g1xn.jpg" alt="MongoDB" width="100">
  </a>
## Installation
#### Clone the *repository*
git clone https://github.com/IvonaSav/flask-app.git
#### Navigate to the *cloned directory*
cd flask-app

* Run the Flask application:
```bash
python app.py
```
The application will be accessible at http://127.0.0.1:5000

## API Endpoints

#### API Endpoint: Home

#### Welcome to the Flask API!
http://localhost:5000/

* ##### Description:
*Receive a welcome message upon accessing the Flask API. This endpoint does not require additional parameters and always returns the message "Welcome to the Flask API!".*

#### First Endpoint
```http
GET /total_spending_by_age/<int:user_id>
``` 

* ##### Description: 

*Retrieves the total spending for a specific user based on their user ID*

* ##### Response:

```json

{
  
  "age": 48,
 
  "email": "elizabeth_cruz@example.com",
  
  "name": "Elizabeth Cruz",
  
  "total_spending": 22778.98,
  
  "user_id": 123
  
}
``` 
#### Second Endpoint
```http
GET /total_spent/<int:user_id>
```

* ##### Description:

*Retrieves the average spending in a specific age range for a user based on their user ID.*

* ##### Response:

```json
{

  "average_spending": 2485.77

}
``` 

#### Third Endpoint
```http
POST /write_to_mongodb
```

* ##### Description:
  
*This API endpoint allows clients to submit user data that exceeds specific
amount of spending in JSON format, which is then inserted into a MongoDB
collection.*

* Request:
```json
{ "user_id": 1, "total_spending": 2000 }
```

* Response (POST):
```json
{
    "inserted_id": "65d3ad4f2520fdb88a4ca900",
    "message": "Data successfully inserted"
}
```
* Response(GET):
```json
{
    "messsage": "GET request successfully handled"
}
```

## Unit Tests

*To ensure the proper functionality of the Flask application, unit tests have been provided. Follow the steps below to run the unit tests:*

Open a terminal in the project directory and run the following command to install the necessary packages:
```bash
pip install requests
```

* Run the unit tests:
```bash
python test_flask_app.py
```
* The test_home_endpoint checks the home endpoint to ensure it returns a welcome message.

* The test_total_spending_by_age_endpoint and test_total_spent_endpoint check the total spending endpoints for specific user IDs.

* The test_write_to_mongodb_endpoint checks the write to MongoDB endpoint for both GET and POST requests.

* Review Test Results:
  
```bash
.....
----------------------------------------------------------------------
Ran 5 tests in 0.012s

OK
```
## Telegram integration

The Flask application integrates with Telegram to send notifications about average spending. The `send_telegram_message` function sends a message to the specified Telegram group when invoked.

```plaintext
Average spending for age range >47: 2485.77
  
