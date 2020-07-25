OpenSphericalCamera Client
=

A Python library for interfacing with cameras that implement the [OpenSphericalCamera](https://developers.google.com/streetview/open-spherical-camera/) API

Supported Cameras
-

- [Ricoh Theta S](https://developers.theta360.com/en/)
- [Samsung Gear 360 (2017)](https://www.samsung.com/global/galaxy/gear-360/)
- Untested OSC cameras
	- [BublCam](http://www.bublcam.com/)
	- [Giroptic](http://us.360.tv/en/)
	- [360fly](https://360fly.com/)

Usage
-

Usage of the pure OSC API

```python
from osc.osc import *

# Initializing the class starts a session
camera = OpenSphericalCamera()
camera.state()
camera.info()

# Only need to call this if there was a problem
# when 'camera' was created
camera.startSession()

# Capture image
response = camera.takePicture()

# Wait for the stitching to finish
camera.waitForProcessing(response['id'])

# Copy image to computer
camera.getLatestImage()

# Close the session
camera.closeSession()
```

Usage of the Ricoh Theta S extended API

```python
from osc.theta import RicohThetaS

thetas = RicohThetaS()
thetas.state()
thetas.info()

# Capture image
thetas.setCaptureMode( 'image' )
response = thetas.takePicture()

# Wait for the stitching to finish
thetas.waitForProcessing(response['id'])

# Copy image to computer
thetas.getLatestImage()

# Stream the livePreview video to disk
# for 3 seconds
thetas.getLivePreview(timeLimitSeconds=3)

# Capture video
thetas.setCaptureMode( '_video' )
thetas.startCapture()
thetas.stopCapture()

# Copy video to computer
thetas.getLatestVideo()

# Close the session
thetas.closeSession()
```

Notes
-
The BublOscClient.js client is the only documentation I can find for the Bublcam custom commands. The client was not tested with actual hardware.

Requirements
-
The Python [Requests](http://docs.python-requests.org/en/master/) library is used to manage all calls to the OSC API.

Install requests with pip:
```
pip install requests
```

References
-

- [RICOH THETA API v2](https://developers.theta360.com/en/docs/v2/api_reference/)

- [RICOH THETA API v2 Overview](https://developers.theta360.com/en/docs/introduction/)

- [Ricoh Developer Forums](https://developers.theta360.com/en/forums/)

- [Unofficial and Unauthorized THETA S Hacking Guide.](https://codetricity.github.io/theta-s/index.html)

- [Github with experiments supporting the Ricoh Theta](https://github.com/codetricity/theta-s-api-tests)

- [Github site with links to a number of Ricoh related projects](https://github.com/theta360developers)

- [BublCam Javascript API tests](https://github.com/BublTechnology/ScarletTests)

- [BublCam OSC client](https://github.com/BublTechnology/osc-client)

- [Alternate OSC Python library](https://github.com/florianl/pyOSCapi)

- [Samsung Gear 360 (2016) OSC Python library](https://github.com/baardove/osc)

Thanks
------
Many thanks to Craig Oda, the author and maintainer of [Theta S API Tests](https://github.com/codetricity/theta-s-api-tests) repo.

Author
------
The original author of this library is:

- Haarm-Pieter Duiker

Testing
-

This library was tested with a Ricoh Theta S using Python 2.7 on OSX Yosemite, and a Samsung Gear 360 (2017) on macOS High Sierra.

License
-

Copyright (c) 2016 Haarm-Pieter Duiker

See the LICENSE file in this repo


