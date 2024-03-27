import cv2
from pyzbar.pyzbar import decode
from screeninfo import get_monitors

not_xml_printed = False

def maximize_window(window_name):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

def get_screen_size():
    for m in get_monitors():
        return m.width, m.height

def detect_qr_codes():
    global not_xml_printed  # Define not_xml_printed as global within the function
    url = 'http://192.168.5.47:8080/video'
    cap = cv2.VideoCapture(url)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Get screen size
    screen_width, screen_height = get_screen_size()

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            decoded_objects = decode(frame)
            for obj in decoded_objects:
                cv2.rectangle(frame, obj.rect, (0, 255, 0), 2)
                qr_data = obj.data.decode('utf-8')
                with open("xml_data.txt", "w") as f:
                    f.write(qr_data)
                cv2.destroyAllWindows()  # Close the window when XML data is printed
                not_xml_printed = True  # Update not_xml_printed
                return

            # Resize the frame to fit the screen
            resized_frame = cv2.resize(frame, (screen_width, screen_height))

            cv2.imshow('Frame', resized_frame)
            maximize_window('Frame')

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    while True:
        detect_qr_codes()
        if not_xml_printed:
            break
        else:
            print("Not XML")
