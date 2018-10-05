# MindstormShoppingTeam5

This repo was created in association with the LEGO/IT Minds competetive case. It contains a simple CLI/python script that allows the user to access an aws endpoint.

## Getting Started

Simply clone the project or download the zip version. If you have python3 installed it should work without any issues. Remember to specify the url to your endpoint.

### Prerequisites

Python3 is the only prerequisite.

### Installing

No installing necessary, unless you lack python3.
Installation of python3: https://www.python.org/downloads/

## Running the tests

There are no tests on this system seeing as it was a short time period we just created it and left it.

### Break down into end to end tests

We manually tested by sending data to our endpoint. The endpoint would trigger an aws lambda function, which would find the correct LEGO box and move the correct answer through the pipeline. The pipeline in this case was an aws SQS. 

### And coding style tests

No tests

## Deployment

Don't use this for any deployment its just a simple script for the case.

## Built With

The CLI uses json and requests modules.

## Contributing

No contributions will be further made to this.

## Versioning

Version 1.0.0

## Authors

* **Andreas Becker Bertelsen** - *CLI work and aws* - [Andyandpandy](https://github.com/andyandpandy)

## License

This project is licensed under nil
## Acknowledgments

* Eske Hoy Nielsen, who created the Mindstorm part of the project to control the robot. Polling the aws SQS for the commands sent through the pipeline.
* Thomas Øther Rasmussen, who helped with the CLI work and aws with support and guidance as well as data structure. 
