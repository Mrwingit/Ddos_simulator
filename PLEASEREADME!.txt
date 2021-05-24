Hieu Mai

This was done in Oracle VM virtual box
Ubuntu 18 or higher is require!! 

I didn't install mininet the tradition way because it was having all sorted of 
problems such as missing overflow controlled, I wasn't able to ping anything, and 
also was messing with file located system on the vm. So I 
went with a different approach of installed!

step 1:
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo apt-get install git

step 2: 
git clone git://github.com/mininet/mininet
cd mininet
git checkout -b 2.2.0b3 (latest)
cd
~/mininet/util/install.sh -a
cd
sudo pip3 install scapy

step 3:
open terminal and type this command to run the customtopology file!
sudo mn --custom /home/Main/dataCenterTopology.py
and then type in mininet>dump to get the information for the next step
which is open another terminal and then type
sudo python3 ddos.py this will promp the user to input information.

this is for part C in the assignment which is similar to step 3. 
sudo mn --custom /home/progSolution/dataCenterTopologyPartC.py
sudo python3 ddos.py again to see a change.

system monitor is a useful tool to check the network graph.

p.s This was very hard! If python3 doesn't work try python2!