import discord
from discord.ext import commands
from discord.ext.commands import Context
from botsettings import *
from theancient import logger

import time
from datetime import datetime
import pytz

class Timezones(commands.Cog, name="timezones"):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot
  
  def gettz(self, tzlist):
    times = {}
    now = datetime.now(pytz.utc)
    for tz in tzlist:
      timezone = pytz.timezone(tz)
      time = datetime.fromtimestamp(now.timestamp(), timezone)
      tzname = time.tzname()
      time = time.strftime('%d-%b %I:%M%p')
      times[tz] = ( f"{time}", f"{tzname}" )
    return times

  def get_timezones(self, tzlist):
    timesheet = "```ansi\n"
    times = self.gettz(tzlist)
    for tz in times:
      localtime = times[tz]
      timesheet += f"\u001b[1;30m{tz: <21}{localtime[1]:>4}\u001b[0m: "
      timesheet += f"\u001b[1;32m{localtime[0]: >15}\u001b[0m\n"
    timesheet += "```"
    return timesheet

  @commands.Cog.listener()
  async def on_ready(self):
    self.log = logger
    self.log.info(f"{__name__} ready")
  
  @discord.app_commands.command(name="timezones",
                    description="Show the current time across "
                                "timezones of interest",
                   )
  async def timezones(self, interaction: discord.Interaction) -> None:
    timesheet = self.get_timezones(tzlist())
    await interaction.response.send_message(timesheet, ephemeral=True)

async def setup(bot) -> None:
  await bot.add_cog(Timezones(bot))
