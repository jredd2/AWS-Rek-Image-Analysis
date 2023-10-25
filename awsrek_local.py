import boto3
import tkinter as tk
from tkinter import filedialog

def detect_labels_local_file(photo):
    client = boto3.client('rekognition')
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
    return response['Labels']

def analyze_image():
    image_path = filedialog.askopenfilename()
    if not image_path:
        return

    labels = detect_labels_local_file(image_path)

    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Detected labels in " + image_path + "\n\n")
    for label in labels:
        result_text.insert(tk.END, label['Name'] + ' : ' + str(label['Confidence']) + "\n")
    result_text.config(state=tk.DISABLED)

# Create the main GUI window
root = tk.Tk()
root.title("Image Label Detection")

# Create and configure the GUI components
file_button = tk.Button(root, text="Select Image", command=analyze_image)
file_button.pack(pady=10)
result_text = tk.Text(root, height=10, width=50, state=tk.DISABLED)
result_text.pack()


# Start the GUI main loop
root.mainloop()
