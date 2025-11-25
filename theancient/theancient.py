import os
import logging
import time
from botsettings import *
import discord
from discord.ext import commands
from botcommands import commandlist

### Main log set up
# [1/5] Log Init
logger = logging.getLogger(__name__)
logger.setLevel(log_level())
# [2/5] Handler Init
handler = logging.StreamHandler()
# [3/5] Format Init
handler_formatter = logging.Formatter(
  "[{asctime}] [{levelname:<8}] {name}: {message}", "%Y-%m-%d %H:%M:%S", style="{"
)
# [4/5] Add Format to Handler
handler.setFormatter(handler_formatter)
# [5/5] Add Handler to Log
logger.addHandler(handler)

class TheAncient(commands.Bot):
  def __init__(self) -> None:
    super().__init__(command_prefix=f"{bot_trigger()}",
                     intents=bot_intents(),
                    )
    self.bot_invite = bot_invite()
    self.log = logger

  async def on_ready(self):
    self.log.info(f'"{self.user.name}", logged in and ready.')

  async def load_commands(self) -> None:
    self.log.info("Loading bot commands...")
    for botcmd in commandlist():
      try:
        await self.load_extension(f"botcommands.{botcmd}")
        self.log.info(f"Loaded bot command: '{botcmd}'")
      except Exception as e:
        exception = f"{type(e).__name__}: {e}"
        self.log.error(
          f"Error loading bot command: {botcmd}, {exception}"
        )
    await self.tree.sync()

  async def setup_hook(self) -> None:
    self.log.info(f"Environment: {bot_runenv()}, "
                  f"Trigger: {bot_trigger()}")
    self.log.info(f"Version: {release_version()}, "
                  f"Settings: {settings_version()}")
    if sync_onload():
      await self.load_commands()
 
def main():
  os.environ['TZ'] = 'UTC'
  if os.name != 'nt':
    time.tzset()
  thebot = TheAncient()
  thebot.run(discord_token())

if __name__ == '__main__':
  main()
