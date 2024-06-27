# Useful Stuffs' modified Raspberry Pi Wi-Fi portal
# For TravelNAS Project
# https://github.com/usefulstuffs/TravelNAS-Project
from flask import Flask,request
import subprocess

app = Flask(__name__)

wifi_device = "wlan1"

@app.route('/')
def index():
    result = subprocess.check_output(["nmcli", "--colors", "no", "-m", "multiline", "--get-value", "SSID", "dev", "wifi", "list", "ifname", wifi_device])
    ssids_list = result.decode().split('\n')
    dropdowndisplay = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>TravelNAS Wifi Control</title>
        </head>
        <body style="background-color:#04AA6D;">
            <h1 style="color:white;">TravelNAS Wifi Control</h1>
            <form action="/submit" method="post">
                <label for="ssid" style="color:white;">Choose a WiFi network:</label>
                <select name="ssid" id="ssid">
        """
    for ssid in ssids_list:
        only_ssid = ssid.removeprefix("SSID:")
        if len(only_ssid) > 0:
            dropdowndisplay += f"""
                    <option value="{only_ssid}">{only_ssid}</option>
            """
    dropdowndisplay += f"""
                </select>
                <p/>
                <label style="color:white;" for="password">Password: <input type="password" name="password"/></label>
                <p/>
                <input type="submit" style="background-color: #04AA6D;border: none;color: white;padding: 15px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 16px;" value="Connect">
            </form>
        </body>
        </html>
        """
    return dropdowndisplay


@app.route('/submit',methods=['POST'])
def submit():
    if request.method == 'POST':
        print(*list(request.form.keys()), sep = ", ")
        ssid = request.form['ssid']
        password = request.form['password']
        connection_command = ["nmcli", "--colors", "no", "device", "wifi", "connect", ssid, "ifname", wifi_device]
        if len(password) > 0:
          connection_command.append("password")
          connection_command.append(password)
        result = subprocess.run(connection_command, capture_output=True)
        if result.stderr:
            return """
                    <!DOCTYPE html>
        <html>
        <head>
            <title>TravelNAS Wifi Control</title>
        </head>
        <body style="background-color:#04AA6D;">
            <h1 style="color:white;">TravelNAS Wifi Control</h1>
            <p style="color:white;">Error: TravelNAS failed to connect to wifi network: <i>%s</i></p>
                    </body>
        </html>
            """ % result.stderr.decode()
        elif result.stdout:
            return """
                                <!DOCTYPE html>
        <html>
        <head>
            <title>TravelNAS Wifi Control</title>
        </head>
        <body style="background-color:#04AA6D;">
            <h1 style="color:white;">TravelNAS Wifi Control</h1>
            <p style="color:white;">TravelNAS successfully connected to Wifi network: <i>%s</i></p>
        </body>
        </html>
        """ % result.stdout.decode()
        return """
                            <!DOCTYPE html>
        <html>
        <head>
            <title>TravelNAS Wifi Control</title>
        </head>
        <body style="background-color:#04AA6D;">
            <h1 style="color:white;">TravelNAS Wifi Control</h1>
            <p style="color:white;">Error: TravelNAS failed to connect.</p>
        </body>
        </html>
        """


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
