# PiCAM Code
There are two main codes here: (1) The camera daemon where the PiCAM definitions are stored and (2) The camera client that sends commands ("snap" and "close") to the daemon to control the camera operation

This was built this way because it minimizes the lag between two networked cameras (~50ms lag; unnoticeable with current measurement setup).

To Run:
1.) Start the daemon on both the server (IP=169.254.181.189) and the client machines (All others) by opening a terminal window and running "python CLIENT_picam_daemon.py -c <CAMERA_ID>" or "python SERVER_picam_daemon.py"
2.) Start the client on the server machine by opening a new terminal and running "python SERVER_picam_client.py"
3.) Send a snap command and the pictures should show up in /opt/nfs (this location is defined in the daemon files)


Active Bugs:
- Still haven't figured out why NTP isn't working
- Ran across a time when the socket stayed open for no reason. Rebooting the pi fixed it.

Documentation Needed:
- Explanation for installing/setting up and working with the Network File Share (NFS) folder found in /opt/nfs
- Explanation for running the camera daemon and client
- Expanation for installing NTP from scratch