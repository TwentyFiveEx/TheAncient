import discord
from discord.ext import commands
from discord.ext.commands import Context
from botsettings import *
from theancient import logger

import time
import os
import secrets
import requests
from functools import lru_cache as lc

class Players(commands.Cog, name="players"):
  url = ""
  count = 0
  log = logger
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot
    self.url = "https://api.steampowered.com/ISteamUserStats" \
               "/GetNumberOfCurrentPlayers/v1/"
    self.log.debug(f"STEAM_API_TTL: {steam_apittl()}")

  @lc(maxsize=2)
  def get_current_lc(self, token, appid, ttl=None):
    self.log.debug(f"URL: {self.url}, TTL: {ttl}")
    del ttl
    current_players_header = { 'Client-ID': f'{token}' }
    current_players_params = { 'format': 'json',
                               'appid': f'{appid}' }
    try:
      current_players = requests.get(f"{self.url}",
                                     headers=current_players_header,
                                     params=current_players_params)
      current_players.raise_for_status()
    except requests.exceptions.HTTPError as err:
      self.log.error("HTTP Error", err)
      return None
    self.count = current_players.json()['response']['player_count']
    return self.count

  def ttl_hash(self, seconds=60):
    seconds = int(seconds)
    return round(time.time() / seconds)

  def get_current_players(self, token=steam_token(), appid=steam_appid()):
    return self.get_current_lc(token, 
                            appid,
                            ttl=self.ttl_hash(steam_apittl())
                            )

  def get_steamplayers(self, echo_whispers):
    players = int(self.get_current_players(steam_token(), steam_appid()))
    if players is None:
      return None
    else:
      ansistart = f"```ansi\n"
      ansiend = "```"
      # 31:red, 32:green, 33:yellow
      players_color = "31" if players <= 28 else "32" if players > 40 else "33" 
      # 0:normal, 1:Bold, 2:Underline
      players_format = "0" 
      players = f"\u001b[{players_format};{players_color}m{players}\u001b[0m"
      secret_saying = f"\u001b[1;30m{secrets.choice(echo_whispers)}\u001b[0m"
    self.log.debug(f"Players API cache: {self.get_current_lc.cache_info()}")
    return f"{ansistart}There are now, {players} players logged into " \
           f"Arkheron.\n{secret_saying}{ansiend}"

  @commands.Cog.listener()
  async def on_ready(self):
    self.log.info(f"{__name__} ready")
  
  @discord.app_commands.command(name="players",
                                description="Show the number of players "
                                            "with the game open",
                               )
  async def players(self, interaction: discord.Interaction) -> None:
    players = self.get_steamplayers(echo_whispers())
    self.log.info(f"Player count request by "
                  f"\"{interaction.user.display_name} ("
                  f"{interaction.user.name})\" "
                  f"on server "
                  f"\"{interaction.guild.name}\"")
    await interaction.response.send_message(players, ephemeral=True)

async def setup(bot) -> None:
  await bot.add_cog(Players(bot))
