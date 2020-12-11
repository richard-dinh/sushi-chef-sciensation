#!/usr/bin/env python
import os
import sys
from ricecooker.utils import downloader, html_writer
from ricecooker.chefs import SushiChef
from ricecooker.classes import nodes, files, questions, licenses
from ricecooker.config import LOGGER              # Use LOGGER to print messages
from ricecooker.exceptions import raise_for_invalid_channel
from le_utils.constants import exercises, content_kinds, file_formats, format_presets, languages

import pandas
# Run constants
################################################################################
CHANNEL_ID = "f189d7c505644311a4e62d9f3259e31b"             # UUID of channel
CHANNEL_NAME = "Sciensation"                           # Name of Kolibri channel
CHANNEL_SOURCE_ID = "Sciensation"                              # Unique ID for content source
CHANNEL_DOMAIN = "sciensation.org"                         # Who is providing the content
CHANNEL_LANGUAGE = "es"                                     # Language of channel
CHANNEL_DESCRIPTION = 'Ciênsação started in 2015, with the support of UNESCO Brasil, as an initiative to promote hands-on experiments at public schools in Brazil. Since then, volunteers have developed, tested, photographed and repeatedly revised more than 100 experiments. These experiments were then translated to Portuguese, Spanish and English, and published online, so that teachers in all of Latin America can benefit from this work.'                                  # Description of the channel (optional)
CHANNEL_THUMBNAIL = None                                    # Local path or url to image file (optional)
CONTENT_ARCHIVE_VERSION = 1                                 # Increment this whenever you update downloaded content


# Additional constants
################################################################################
EN_XLSX = os.path.join('files', 'sciensation_en.xlsx')
ES_XLSX = os.path.join('files', 'sciensation_es.xlsx')
PT_XLSX = os.path.join('files', 'sciensation_pt.xlsx')

# The chef subclass
################################################################################
class SciensationChef(SushiChef):
    """
    This class converts content from the content source into the format required by Kolibri,
    then uploads the {channel_name} channel to Kolibri Studio.
    Your command line script should call the `main` method as the entry point,
    which performs the following steps:
      - Parse command line arguments and options (run `./sushichef.py -h` for details)
      - Call the `SushiChef.run` method which in turn calls `pre_run` (optional)
        and then the ricecooker function `uploadchannel` which in turn calls this
        class' `get_channel` method to get channel info, then `construct_channel`
        to build the contentnode tree.
    For more info, see https://ricecooker.readthedocs.io
    """
    channel_info = {
        'CHANNEL_ID': CHANNEL_ID,
        'CHANNEL_SOURCE_DOMAIN': CHANNEL_DOMAIN,
        'CHANNEL_SOURCE_ID': CHANNEL_SOURCE_ID,
        'CHANNEL_TITLE': CHANNEL_NAME,
        'CHANNEL_LANGUAGE': CHANNEL_LANGUAGE,
        'CHANNEL_THUMBNAIL': CHANNEL_THUMBNAIL,
        'CHANNEL_DESCRIPTION': CHANNEL_DESCRIPTION,
    }
    DATA_DIR = os.path.abspath('chefdata')
    DOWNLOADS_DIR = os.path.join(DATA_DIR, 'downloads')
    ARCHIVE_DIR = os.path.join(DOWNLOADS_DIR, 'archive_{}'.format(CONTENT_ARCHIVE_VERSION))

    # Your chef subclass can override/extend the following method:
    # get_channel: to create ChannelNode manually instead of using channel_info
    # pre_run: to perform preliminary tasks, e.g., crawling and scraping website
    # __init__: if need to customize functionality or add command line arguments
    def construct_channel(self, *args, **kwargs):
        """
        Creates ChannelNode and build topic tree
        Args:
          - args: arguments passed in on the command line
          - kwargs: extra options passed in as key="value" pairs on the command line
            For example, add the command line option   lang="fr"  and the value
            "fr" will be passed along to `construct_channel` as kwargs['lang'].
        Returns: ChannelNode
        """
        channel = self.get_channel(*args, **kwargs)  # Create ChannelNode from data in self.channel_info

        # TODO: Replace next line with chef code
        raise NotImplementedError("constuct_channel method not implemented yet...")

        return channel

def format_url(experiment_id, language_code):
    if language_code == 'en':
        return 'https://sciensation.org/hands-on_experiments/{}.html'.format(experiment_id)
    elif language_code == 'es':
        return 'https://ciensacion.org/experimentos_manos_en_la_masa/{}.html'.format(experiment_id)
    else:
        return 'https://ciensacao.org/experimento_mao_na_massa/{}.html'.format(experiment_id)

# CLI
################################################################################
if __name__ == '__main__':
    # This code runs when sushichef.py is called from the command line
    chef = SciensationChef()
    chef.main()