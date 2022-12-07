import json
import logging
import re

logger = logging.getLogger(__name__)

class wikiRules:
    def __init__(self):
        logger.setLevel(logging.INFO)

    def ruleDescriptorSeach(needle:str, haystack:str):
        if (re.search(needle, haystack, re.IGNORECASE)):
            return True
        else:
            return False