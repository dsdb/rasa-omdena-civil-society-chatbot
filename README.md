# Omdena Civil Society Chatbot

This repository contains the source code for a Rasa Chatbot that provides information about Omdena's collaboration with Civil Society Partners. The chatbot can answer queries related to these partnerships and provide details about the organizations Omdena has collaborated with.

## Getting Started

### Installation

- Clone this repository:

   ```bash
   git https://github.com/dsdb/rasa-omdena-civil-society-chatbot.git
   cd rasa-omdena-civil-society-chatbot

- Install the required dependencies:
  pip install -r requirements.txt

- Train the Rasa model:
  rasa train

- Start the Rasa Action server in a separate terminal:
  rasa run actions


**Features**
The chatbot can answer queries about Omdena's Civil Society Partnerships.
It fetches the list of partners from a text file (actions/civil_society_partners.txt) and provides information about them.
The chatbot uses both rule-based and story-based interactions to respond to user queries.

**Contributing**
Contributions are welcome! 

**License**
This project is licensed under the MIT License.
