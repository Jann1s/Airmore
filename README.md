# Airmore

Set up Rasp. Pi:

cs → GPIO8
mosi → GIPO10
miso → GIPO9 
clk → GPIO11
gnd → 
vin → 3V3
sda → GPIO2
scl → GPIO3

https://www.jameco.com/Jameco/workshop/circuitnotes/raspberry_pi_circuit_note_fig2.jpg

Intall dependencies:

Make sure the Pi has internet connection and type the following in the console: sudo apt-get install qt4-dev-tools. Also install git by typing this to the terminal: sudo apt-get install git. Now download the Lepton Module by typing the following to the console: git clone https://github.com/groupgets/LeptonModule.git. Go to the Module's directory and find the LeptonSDKEmb32PUB directory, once there, type 'make' in the terminal. Finally go back to the raspberry_pi directory and type qmake && make in the terminal.

Connect to the Pi:

Enable VNC, SSH, SPI and I2C services using raspi-config or graphical preferences interface (already enabled during groupwork). Connect Pi and laptop with ethernet cable. Find Pi IP address (using Advanced IP Scanner: https://advanced-ip-scanner.softonic.com/) and connect through VNC Viewer.

For more details on getting the Pi and the Flir camera working check this link: https://learn.sparkfun.com/tutorials/flir-lepton-hookup-guide.
