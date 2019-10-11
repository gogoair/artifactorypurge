"""Post a message to slack."""
import logging

import slacker

from ..credentials import load_slack_credentials

LOG = logging.getLogger(__name__)


def post_slack_message(message=None, username=None, icon_emoji=None):
    """Format the message and post to the appropriate slack channel.

    Args:
        message (str): Message to post to slack
        channel (str): Desired channel. Must start with #

    """
    LOG.debug('Loading Slack Credentials')
    slack_credentials = load_slack_credentials()
    
    channel = slack_credentials['slack_channel']
    LOG.debug('Slack Channel: %s\nSlack Message: %s', channel, message)

    slack = slacker.Slacker(slack_credentials['api_token'])
    try:
        slack.chat.post_message(channel=channel, text=message, username=username, icon_emoji=icon_emoji)
        LOG.info('Message posted to %s', channel)
    except slacker.Error:
        LOG.info("error posted message to %s", channel)