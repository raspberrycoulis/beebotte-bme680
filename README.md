# beebotte-bme680
## Using Pimoroni's BME680 breakout board with Beebotte.

This Python script is based on Beebotte's example to use a DHT11 temperature and humidity sensor on the Raspberry Pi and feed data to a dashboard. The example script can be found [here](https://beebotte.com/tutorials/monitor_humidity_and_temperature_with_raspberrypi) and requires a Beebotte account.

### Install the BME680 files

The installer script, created by [Pimoroni](https://shop.pimoroni.com), is simple:

    curl https://get.pimoroni.com/bme680 | bash

But full install instructions can be found [here](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-bme680-breakout).

### Install the Beebotte files

You'll need to install the relevant Beebotte files, which is done by:

    sudo pip install beebotte

### Clone and use my script

Simply clone this script by running:

    cd ~
    sudo git clone https://github.com/raspberrycoulis/beebotte-bme680.git

You'll need to make some changes first, specifically inserting your Channel Key (found via Beebotte) in the following place:

    ### Replace CHANNEL_KEY with that of your channel
    bbt = BBT(token = 'CHANNEL_KEY')

You can use your preferred text editor, but Nano works just fine:

    sudo nano beebotte-bme680.py

Be sure to save when exiting:

    ctrl + x
    y

Make the script executable:

    sudo chmod +x beebotte-bme680.py

And then finally test it by running:

    ./beebotte-bme680.py

If done correctly, you should see printouts in the command line of the temperature, pressure humidity and air quality readings. Stop the script by pressing `ctrl + c`.

## Making the script run automatically on boot

I followed the excellent guide found on [Raspberry Pi Spy](http://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/) to make my  `beebotte-bme680.py` script run on boot. To recap, this is what I did:

### 1. Create a Unit file

This is what will tell the Pi to run your script on boot:

    sudo nano /lib/systemd/system/beebotte-bme680.service

Then add the following text to your file (you may need to adjust the path for your `beebotte-bme680.py` script depending on where it is located (the part `/home/pi/github/beebotte-bme680/beebotte-bme680.py`):

    [Unit]
    Description=The BME680 Breakout Board via Beebotte service
    After=multi-user.target
    
    [Service]
    Type=idle
    ExecStart=/usr/bin/python /home/pi/github/beebotte-bme680/beebotte-bme680.py
    
    [Install]
    WantedBy=multi-user.target

Exit, `ctrl + x`, and save `y`to create the service unit file.

### 2. Set the relevant permissions

Make sure that the permissions are set correctly:

    sudo chmod 644 /lib/systemd/system/beebotte-bme680.service

### 3. Configure systemd

Make sure that systemd can use your newly created unit file:

    sudo systemctl daemon-reload
    sudo systemctl enable beebotte-bme680.service

Reboot the Pi to test via `sudo reboot`.

### 4. Check on the status of your service

Check that the service has started by running:

    sudo systemctl status beebotte-bme680.service

If done correctly, you should see that your `beebotte-bme680.py` script is now running!
