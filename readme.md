# PiCAM Code
There are two main codes here: (1) The camera daemon where the PiCAM definitions are stored and (2) The camera client that sends commands ("snap" and "close") to the daemon to control the camera operation

This was built this way because it minimizes the lag between two networked cameras (~50ms lag; unnoticeable with current measurement setup).

## Latest Updates:
- Fixed the individual client and server codes so that they save to the /opt/nfs/Pics folder
- THEN...Combined the individual client and server codes so that they all run the same python script. You run the daemon with a command line argument specifying the Camera_ID for that Pi (e.g. python picam_daemon.py -c 1)

## To Run:
- Start the daemon on both the server (IP=169.254.181.189) and the client machines (All others) by opening a terminal window and running "python picam_daemon.py -c <CAMERA_ID>"
- Start the PiCAM client on the server machine by opening a new terminal and running "python picam_client.py"
- Send a snap command and the pictures should show up in /opt/nfs/Pics (this location is defined in the daemon files)

## Active Bugs:
- Still haven't figured out why NTP isn't working
- Ran across a time when the socket stayed open for no reason. Rebooting the pi fixed it.
- Running the 'snap' command can still take some time when you have 4 cameras/Pis hooked up (up to 6.6 seconds to execute, but the images are all time-synchronized)

## Documentation Needed:
- Explanation for installing/setting up and working with the Network File Share (NFS) folder found in /opt/nfs
- Explanation for running the camera daemon and client
- Expanation for installing NTP from scratch