Slack Handler
=============

This module provides a logging handler that takes a slack hook url as its first
argument. Logs sent to that handler are then buffered and passed to the slack
channel attached to that hook.


## Usage

Where hook_url is the slack generated url for your bot.

    import logging

    from slack_handler import SlackHandler

    logger = logging.getLogger(__name__)
    handler = SlackHandler('https://hooks.slack.com/services/12354blahblah/asd')

    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    logger.info('Yay!')

## Or with logging config

    import logging
    import logging.config

    import yaml


    with open('logging.yml', 'r') as stream:
        logging.config.dictConfig(yaml.load(stream))

    logger = getLogger(__name__)

    logger.info('We did it again!')
