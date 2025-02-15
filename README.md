---

# Discord Bot: SAMP Status Activity Presence Bot

## Description
This Discord bot retrieves and displays information about a San Andreas Multiplayer (SAMP) server from a specified URL using web scraping techniques. It fetches details such as server status, IP address, game name, mode, version, players online, location, and last update time.

## Features
- **Server Information**: Fetches detailed information about a SAMP server.
- **Dynamic Command Handling**: Loads commands dynamically from the `./commands` directory.
- **Activity Update**: Sets bot activity to display the number of players currently online on the server.
- **Error Handling**: Gracefully handles errors during server information retrieval.

## Technologies Used
- **Python**: Programming language used to build the bot.
- **Discord.py**: Python library for interacting with the Discord API.
- **Requests**: HTTP library for making requests to the server.
- **Beautiful Soup**: Library for parsing HTML and XML documents.

## Usage
1 **Bot Activity**
   - Updates bot activity to display the number of players online on the server.

## Setup
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Make An/Add Your server to https://www.gs4u.net/en/samp/ and copy the website link such seems to be like 
4. Configure `config.py` with your Discord bot token and server info URL.
5. Run the bot using `python main.py`.

## Commands
- **serverinfo**: Fetches detailed information about the SAMP server.

## Directory Structure
- `main.py`: Main entry point for the Discord bot.
- `config.py`: Configuration file for bot token and server info URL.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your proposed changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---
