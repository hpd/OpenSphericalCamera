"""
Extensions to the Open Spherical Camera API specific to the Gear 360 camera (2017).

Usage:
At the top of your Python script, use

  from osc.gear360_2017 import Gear360_2017

After you import the library, you can use the commands like this:

  gear360 = Gear360_2017()
  gear360.state()
  gear360.info()

  # Capture image
  response = gear360.takePicture()

  # Wait for the stitching to finish
  gear360.waitForProcessing(response['id'])

  # Copy image to computer
  gear360.getLatestImage()

  gear360.closeSession()
"""

import osc

class Gear360_2017(osc.OpenSphericalCamera):

    # Instance variables / methods
    def __init__(self, ip_base="192.168.43.1", httpPort=80):
        self.sid = None
        self.fingerprint = None
        self._api = None

        self._ip = ip_base
        self._httpPort = httpPort
        self._httpUpdatesPort = httpPort

        # Try to start a session
        self.startSession()

        # Use 'info' command to retrieve more information
        self._info = self.info()
        if self._info:
            self._api = self._info['api']
            self._httpPort = self._info['endpoints']['httpPort']
            self._httpUpdatesPort = self._info['endpoints']['httpUpdatePort']

    def latestFileUri(self):
        x = self.listImages(1)
        if 'results' in x:
            if 'entries' in x['results']:
                if len(x['results']['entries']) == 1:
                    if 'uri' in x['results']['entries'][0]:
                        return x['results']['entries'][0]['uri']
        return None

