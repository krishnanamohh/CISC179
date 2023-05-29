from cisc179.ElectronicDevice import ElectronicDevice
import matplotlib.pyplot as plt
from PIL import Image

class Camera(ElectronicDevice):
    def __init__(self, power_source, manufacturer, resolution, zoom_range):
        super().__init__(power_source, manufacturer)
        self.resolution = resolution
        self.zoom_range = zoom_range

    def capture_photo(self):
        print("Taking a photo with the camera.")

    def record_video(self):
        print("Recording a video with the camera.")

    def display_info(self):
        info = []
        info.append("Camera Information:")
        info.append("Manufacturer: " + self.manufacturer)
        info.append("Resolution: " + self.resolution)
        info.append("Zoom Range: " + self.zoom_range)
        return info
    def save_photo(self, filename):

        print(f"Saving photo as {filename}.")


    def validate_resolution(self):

        if self.resolution.startswith("24 MP"):
            print("Resolution is valid.")
        else:
            print("Invalid resolution.")


    def generate_graph(self, resolutions, pixels):
        plt.plot(resolutions, pixels, 'ro-')
        plt.xlabel("Resolution")
        plt.ylabel("Pixels")
        plt.title("Camera Resolution vs Pixels")
        plt.show()

    #def launch_gui(self):
        # Code to create and run a GUI window
        #root = Tk()
        #label = Label(root, text="Camera GUI")
        #label.pack()
        #button = Button(root, text="Capture Photo", command=self.capture_photo)
        #button.pack()
        #root.mainloop()



    def get_info(self):
        return f"Camera Information: Manufacturer - {self.manufacturer}, Resolution - {self.resolution}, Zoom Range - {self.zoom_range}"

    def validate_image_data(filename, target_data):
        try:
            image = Image.open(filename)
            image_data = image.getdata()

            if image_data == target_data:
                return "Image data is valid."
            else:
                return "Image data is not valid."
        except IOError:
            return "Failed to open the image file."

    filename = "static/image/image2.jpg"
    target_data = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    validation_result = validate_image_data(filename, target_data)
    print("Validation Result: ", validation_result)


camera = Camera("Battery", "Nikon", "24 MP", "5x Optical Zoom")
camera.display_info()
camera.capture_photo()
camera.record_video()
camera.save_photo("photo.jpg")
camera.validate_resolution()
resolutions = ["HD", "Full HD", "4K"]
pixels = [2, 4, 8]
camera.generate_graph(resolutions, pixels)
