import os
import discord

def release_version() -> str:
  ''' Returns the major.minor.patch bot code version
      Type: (str)
  '''
  return "v0.1.0"

def settings_version():
  ''' Returns the major.minor.patch settings version
     Type: (str)
  '''
  return "v0.1.0"

def log_level():
  ''' Returns from env var: ANCIENT_LOGLEVEL
     Defaults to: INFO
     Type: (str)
  ''' 
  return str(os.getenv('ANCIENT_LOGLEVEL', 'INFO').upper())

def bot_trigger():
  ''' Return the chat command trigger from env var: ANCIENT_TRIGGER
     Defaults to: '/'
     Type: (str) 
  '''
  return os.getenv('ANCIENT_TRIGGER', '/')

def bot_runenv():
  ''' Return the runtime environment level from env var: ANCIENT_ENV
     Defaults to: 'Production'
     Type: (str)
  '''
  return str(os.getenv('ANCIENT_ENV', 'Production'))

def discord_token():
  ''' Returns the Discord token used by the bot from env var: ANCIENT_TOKEN 
      Type: (str)
  '''
  return str(os.getenv('ANCIENT_TOKEN', "MUST_PROVIDE_VALID_DISCORD_TOKEN"))

def bot_invite():
  ''' Returns the invite URL for the bot from env var: ANCIENT_INSTALLURL
      Type: (str)
  '''
  return str(os.getenv('ANCIENT_INSTALLURL', "INSTALL_URL_MISSING"))

def steam_appid():
  ''' Returns the Steam APP id for player counts from env var: STEAM_APPID
      Type: (str)
  '''
  return str(os.getenv('STEAM_APPID', "3401450")) 

def steam_token():
  ''' Returns the Steam API Token from env var: STEAM_TOKEN
      Type: (str)
  '''
  return str(os.getenv('STEAM_TOKEN', "MUST_PROVIDE_VALID_STEAM_TOKEN"))

def steam_apittl():
  ''' Returns the ttl for caching steam api data for the bot from
      env var: STEAM_API_TTL
      Type: (str)
  '''
  return str(os.getenv('STEAM_API_TTL', '20'))

def quotesdb():
  ''' Returns the quotes API endpoint url
     Type: (str)
  '''
  return "https://quotes.alakhpc.com/quotes/1"

def tzlist():
  ''' Returns timezones of interest
     Type: (list)
  ''' 
  tzlist = [ 'America/Los_Angeles',
             'America/Phoenix',
             'US/Central',
             'US/Eastern',
             'Brazil/East',
             'Europe/London',
             'Europe/Paris',
             'Europe/Moscow',
             'Asia/Hong_Kong',
             'Asia/Seoul', 
             'Pacific/Auckland',
           ]
  return tzlist

def echo_whispers():
  ''' Returns responses influenced by The Ancient
     Type: (list)
  '''
  echo_whispers = [ 'Get to a beacon.',
                    'The tower calls to you.',
                    '(a sense of regret fills your mind) '
                      '\u001b[0;34mYou told them they '
                      'would be safe.\u001b[1;30m '
                      '(you shake your head and the feeling '
                      'subsides)',
                    '(you start to feel like you are floating) '
                      '\u001b[0;33mDark shadows '
                      'on the surface of the water.\u001b[1;30m '
                      '(the feeling fades away)',
                    '(you begin to feel an insatiable hunger) '
                      '\u001b[0;31mThe wind was '
                      'real. Untethered.\u001b[1;30m '
                      '(the feeling passes)',
                    '(you feel as though you are falling forward) '
                      '\u001b[0;32mThey are '
                      'in my way. They are all in my way.\u001b[1;30m '
                      ' (your balance returns to normal)',
                      '(you gain a sudden sense of resilience) '
                      '\u001b[0;32mThey stood at the fore. Ankle '
                      'deep in the mud.\u001b[1;30m '
                      '(the sense fades away)',
                    '(you feel as though the room is spinning, or you are) '
                      '\u001b[0;35mThe music drowns your imperfections '
                      'out.\u001b[1;30m '
                      '(your regain your balance)',
                    '\u001b[1;33mPacked with energy, exile. Packed '
                      'with energ... wait. How did I get here? '
                      'Where\'s the mine? Ohh, my. I guess that WAS '
                      ' good stuff..\u001b[1;30m',
                    '(you feel ready to collect some heads) '
                      '\u001b[0;33mBusy, busy, busy. '
                      'Clink, clink.\u001b[1;30m '
                      '(you blink and your thoughts return to normal)',
                    '(you suddenly remember searching for someone) '
                      '\u001b[0;36mFind her! Burn the witch.\u001b[1;30m '
                      '(you forget what you are doing and regain '
                      'your composure)',
                    '(a burning feeling swells within you) '
                      '\u001b[1;31mThe war won\'t '
                      'reach us. How could it?\u001b[1;30m '
                      '(the feeling quickly diminishes)',
                    '(anger overtakes your senses) '
                      '\u001b[1;35mSo freeing to let go. '
                      'Easy as letting out a sigh.\u001b[1;30m '
                      '(you blink and open your eyes, the feeling is gone)',
                  ]
  return echo_whispers

def bot_intents():
  ''' Returns Discord gateway features for the bot
      Type: (discord.Intents)
  '''
  intents = discord.Intents.default()
  intents.typing = False
  intents.presences = False
  intents.members = True
  intents.messages = True
  intents.message_content = True
  return intents

def sync_onload():
  ''' Returns whether to sync commands to Discord when
      add/update/delete a command. This is needed for now to ensure slash
      commands are in sync, but will be more dynamic later.
      Type: (bool)
  '''
  return True
