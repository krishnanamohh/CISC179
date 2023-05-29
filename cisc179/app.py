from flask import Flask, render_template, request
from cisc179.Camera import Camera
from cisc179.Laptop import Laptop
from cisc179.SmartPhone import Smartphone

app = Flask(__name__)

devices = {
    'camera': Camera("Battery", "Nikon", "24 MP", "5x Optical Zoom"),
    'smartphone': Smartphone("Battery", "Apple", "12 pro max"),
    'laptop': Laptop("AC power", "Dell", "Windows 10", 8, 15.6, "1920x1080")
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_device_info', methods=['POST'])
def get_device_info():
    selected_device = request.form['device']

    if selected_device == 'smartphone':
        device = devices['smartphone']
        return render_template('device_info.html', device_info=f"Smartphone Information: Manufacturer - {device.manufacturer}, Model - {device.model}")
    elif selected_device == 'laptop':
        device = devices['laptop']
        return render_template('device_info.html', device_info=f"Laptop Information: Manufacturer - {device.manufacturer}, Operating System - {device.operating_system}, RAM - {device.ram}")
    elif selected_device == 'camera':
        device = devices['camera']
        return render_template('device_info.html', device_info=f"Camera Information: Manufacturer - {device.manufacturer}, Resolution - {device.resolution}, Zoom Range - {device.zoom_range}")
    else:
        return "No device information available."


if __name__ == '__main__':
    app.run(port=5001)
