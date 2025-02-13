## buzzline-05-Toba
## Project Overview

This project is a real-time data processing project that demonstrates the use of Apache Kafka and Python to stream, consume, and visualize sentiment data dynamically. The system ingests messages about various topics, analyzes sentiment, and visualizes the results to monitor trends over time.

## Insights used

- timestamp → Tracks when the message was received.
- category → Groups sentiment by topic.
- sentiment → Helps analyze trends and mood shifts.

## Installation

### Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/your-username/buzzline-05-toba.git
cd buzzline-05-toba

## Set Up Python Environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# Unix/MacOS
source .venv/bin/activate

## Start Kafka & Zookeeper

- zookeeper-server-start.sh config/zookeeper.properties
- kafka-server-start.sh config/server.properties

## Install Dependencies
pip install -r requirements.txt
pip install pandas matplotlib

## Running the Producer
python producer_case.py

## Running the Consumer
python consumers/consumer_Adeyemi.py

## Visualizing Data
python visualization.py

## License

This project is licensed under the MIT License as an example project. You are encouraged to fork, copy, explore, and modify the code as you like. See the LICENSE file for more.

