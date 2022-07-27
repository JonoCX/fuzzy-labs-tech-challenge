# Fuzzy Labs Technical Challenge - Reverse Polish Notation

###### Usage

The program was written using Python 3.8 and the requirements can be installed into a virtual environment using the `requirements.txt` file. 

The unit testing suite used is `Pytest` (along with `pytest-cov`). To run the tests (after installing the requirements), execute the following: `pytest tests`; and to get the coverage run: `pytest --cov=calculator tests/`

###### _How would you implement an infix notation calculator, i.e., ordinary arithmetic expressions such as 1+2, on top of your RPN calculator?_

The calculator would change first by allowing the user to pass an argument at runtime (`--infix`) to switch the program into infix mode. Internally, an additional function would be implemented which converts the infix notation to postfix (RPN), passes the converted expression to the `_calculator` function, and propagates the results back to the user.

###### _How would you deploy your calculator as a service in a cloud environment?_

I would turn the calculator into a REST API using Flask, Docker, and AWS Lightsail (or something similar). This would include implementing a function which accepts incoming POST requests with the expression in the payload and that returns the result as a message. The app would be dockerized and hosted as a service on Lightsail, accepting requests on an exposed port. The app could be extended to include persistence of results (some form of database; AWS RDS is available automatically on Lightsail), as well as other functionality (such as the answer to the previous question, where the `--infix` argument would be part of the request payload.