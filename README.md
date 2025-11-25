# The Ancient

The Ancient is a fan-made Discord bot for the Arkheron gaming community audience. [Arkheron](https://arkheron.com/) is a game currently in development by [Bonfire Studios](https://bonfirestudios.com/). This bot is not a product of Bonfire Studios.

The Ancient provides assistance in the areas of Arkheron game status, gameplay item information, and connecting player communities with the game. No additional resources or installation is required beyond a Steam API token and a Discord bot token.

The bot can be deployed as portable python3 code or as a (Docker) container instance.

The bot is currently designed as a monolithic endpoint, listening for incoming requests from Discord and acting on those requests. Multiple instances of the bot will result in multiple concurrent responses at this time. In the event this bot grows to a large enough request volume that multiple parallel instances are needed, the code should be converted to use sharding which is a simple exercise but [comes with many caveats](https://guide.pycord.dev/popular-topics/sharding).

## Quick Start
TODO: Expand on getting tokens  
TODO: Maybe expand on getting docker?  
You will need the following to do anything meaningful with the bot. 
- Discord Bot Token
- Steam API Token

Run the Docker container by passing env vars on the command line.
```
$ export ANCIENT_TOKEN="your_discord_bot_token"
$ export STEAM_TOKEN="your steam api token"
$ docker run -e "ANCIENT_TOKEN=${ANCIENT_TOKEN}" -e "STEAM_TOKEN=${STEAM_TOKEN}" --rm -it theburb/theancient:latest
```
If you are running Windows, you may need to put "winptr" in front of the docker  
run command: "winpty docker run ...".

Alternatively, you can pass your token secrets through an env file.
```
$ echo 'ANCIENT_TOKEN="your_discord_bot_token"' > env.file
$ echo 'STEAM_TOKEN="your steam api token"' >> env.file
$ docker run --env-file ./env.file --rm -it theburb/theancient:latest
```

Add the bot to a Discord server. For instance, with the bot installation URL  
found in the Discord developer interface. Example, where NNNN is the bot id  
associated with ANCIENT_TOKEN above.
* https://discord.com/oauth2/authorize?client_id=NNNN&permissions=0&integration_type=0&scope=bot+applications.commands

## Requirements
* Python =>3.13

Please be aware this code comes with zero guarantees that this code will work. I
tried to pick a generally acceptible, open, and simple python image for the 
container image but if you want something more robust, replace it with 
something else.

## Contributing
For contributing to the bot, please see the [development documentation](theancient/docs/devel.md).

## TODO
I have a lot of documentation gaps that I need to fill in. This includes documenting the code fully.  
I also have a lot to do in the space of adding tests to the code. I know, I know.. add tests while you code. Well, I didn't. It's fine. This started as a 2 line bash script so, here we are. There's a number of bits including finishing the setup.py binary builder and making sure that works properly, then swapping that in for the python ./foo.py launch method. Plenty to do. ALso I have some command modules cooking:
- Trivia
- Wiki lookups
- Bot-based Queue System
- Queue system metrics output (by region, activity, etc)
- Karma system for recognizing stellar teammates

## About the Author
I'm Burb. I'm located in Southwestern United States. I'm into hiking, gaming, tiny electronics, large scale system architecture, software development lifecycles, gardening, and being a friend to backyard birds.

If this code makes you happy consider contributing to it or sharing your own code creations with the world.

Thanks for checking things out and hey: Be well.
