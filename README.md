# Whitelist-acserver-Discord

## Description
This project is a Discord bot that allows server administrators to manage a whitelist for an Assetto Corsa server. The bot uses the `!whitelist` command to add or remove players from the whitelist based on their Steam ID. The whitelist is saved in a text file called `whitelist.txt`.

## Requirements
- Python 3.x
- Libraries: discord.py, aiohttp
- A Discord server
- An Assetto Corsa server

## Installation
1. Clone this repository or download the source code.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Create a Discord bot by following [these instructions](https://discordpy.readthedocs.io/en/latest/discord.html).
4. Add the bot token and Assetto Corsa server information to the configuration file.
5. ...

## Usage
To run the bot, use the command `python whitelist.py`.

Once the bot is running, server user can use it on their Discord server with the following command:
- `!whitelist 'steamid'`: Adds or removes the player with the specified Steam ID from the Assetto Corsa server whitelist.

## Contributing
Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) before submitting a pull request. Remember to keep the credits to the original author.

## Credits
This project was created by russozl. Contributions are welcome as long as the credits are kept.

## License
This project is licensed under the MIT license. See the [LICENSE](LICENSE) file for more information
