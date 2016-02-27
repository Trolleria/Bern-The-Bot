"""
    Credentials to connect on Whatsapp Servers.
    (phone number, whatsapp key)

    To extract key use the yowsup-cli (using a python venv with yowsup installed):

    > yowsup-cli registration -C <CountryCode> -r sms -p <Phone Number with Country Code>
    ex.:
    yowsup-cli registration -C 55 -r sms -p 554899998888

    Then whatsapp will send a key via sms to the phone.
    Get that key then run:

    > yowsup-cli registration -C 55 -R <sms-key> -p 554899998888

"""
auth = ("85255054213", "Asv9BBPYIRFx+hwcNFC7fhQ9RCQ=")

# If filter_groups is True, the bot only stays
# at groups that there is at least one admin on it.
# Otherwise will leave instantly if added.
filter_groups = False
admins = ["XXXXXXXXXXXX", ]


# Bing API for image search
bing_api = "K3I+DyWqUnD0IwIr5Ova90At38gkoFeVadH1rJhWliE"

# Path to download the media requests
# (audio recordings, printscreens, media and youtube videos)
media_storage_path = "berntmp/"

# Session shelve db path
session_db_path = "berntmp/sessions.db"


# Logging configuration.
# By default only logs the command messages.
# If logging_level set to logging.DEBUG, yowsup will log every protocoll message exchange with server.
import logging

log_format = '_%(filename)s_\t[%(levelname)s][%(asctime)-15s] %(message)s'
logging_level = logging.INFO
