# pip install adafruit-circuitpython-fingerprint
import adafruit_fingerprint as fp
import board
import busio


usb = busio.UART(board.TX, board.RX, baudrate=57600)
sensor = fp.Adafruit_Fingerprint(usb)


def search():
    print("Place finger on the sensor...", end=" ", flush=True)
    return_code = sensor.get_image()
    while return_code == fp.NOFINGER:
        return_code = sensor.get_image()

    if return_code == fp.OK:
        print("Image taken")
    else:
        if return_code == fp.NOFINGER:
            print("No finger detected")
        elif return_code == fp.IMAGEFAIL:
            print("Imaging error")
        else:
            print("Other error")
        return return_code

    print("Templating...", end=" ", flush=True)
    return_code = sensor.image_2_tz()

    if return_code == fp.OK:
        print("Templated")
    else:
        if return_code == fp.IMAGEMESS:
            print("Image too messy")
        elif return_code == fp.FEATUREFAIL:
            print("Could not identify features")
        elif return_code == fp.INVALIDIMAGE:
            print("Image invalid")
        else:
            print("Other error")
        return return_code

    print("Searching...", end=" ", flush=True)
    return_code = sensor.finger_fast_search()

    if return_code == fp.OK:
        print("Found fingerprint!")
    else:
        if return_code == fp.NOTFOUND:
            print("No match found")
        else:
            print("Other error")
        return return_code

    return return_code


def enroll(id):
    for i in range(2):
        print(f"Place finger on the sensor{" again"*i}...", end=" ", flush=True)
        return_code = sensor.get_image()
        while return_code == fp.NOFINGER:
            return_code = sensor.get_image()

        if return_code == fp.OK:
            print("Image taken")
        else:
            if return_code == fp.IMAGEFAIL:
                print("Imaging error")
            else:
                print("Other error")
            return return_code

        print("Templating...", end=" ", flush=True)
        return_code = sensor.image_2_tz(i+1)

        if return_code == fp.OK:
            print("Templated")
        else:
            if return_code == fp.IMAGEMESS:
                print("Image too messy")
            elif return_code == fp.FEATUREFAIL:
                print("Could not identify features")
            elif return_code == fp.INVALIDIMAGE:
                print("Image invalid")
            else:
                print("Other error")
            return return_code

        if i == 0:
            print("Remove finger")
            while return_code != fp.NOFINGER:
                return_code = sensor.get_image()

    print("Creating model...", end=" ", flush=True)
    return_code = sensor.create_model()

    if return_code == fp.OK:
        print("Created")
    else:
        if return_code == fp.ENROLLMISMATCH:
            print("Prints did not match")
        else:
            print("Other error")
        return return_code

    print(f"Storing model #{id}...", end=" ", flush=True)
    return_code = sensor.store_model(id)

    if return_code == fp.OK:
        print("Stored")
    else:
        if return_code == fp.BADLOCATION:
            print("Bad storage location")
        elif return_code == fp.FLASHERR:
            print("Flash storage error")
        else:
            print("Other error")
        return return_code

    return return_code


def get_id():
    i = -1
    while i not in range(sensor.library_size):
        i = int(input(f"Enter ID between 0-{sensor.library_size-1}: "))
    return i


while True:
    print("-"*40)
    if sensor.read_templates() != fp.OK:
        raise RuntimeError("Failed to read templates")
    print("Fingerprint templates:", sensor.templates)
    if sensor.count_templates() != fp.OK:
        raise RuntimeError("Failed to read templates")
    print(f"Number of templates in library: {sensor.template_count}/{sensor.library_size}")

    print("e - enroll print")
    print("s - search print")
    print("d - delete print")
    print("r - reset library")
    print("q - quit")
    inp = input("> ")

    if inp == "e":
        if enroll(get_id()) == fp.OK:
            print("Enrolled!")
        else:
            print("Failed to enroll")
    elif inp == "s":
        if search() == fp.OK:
            print(f"Detected #{sensor.finger_id} with confidence {sensor.confidence}")
        else:
            print("Finger not found")
    elif inp == "d":
        if (id:=get_id()) not in sensor.templates:
            print("ID not found")
        elif sensor.delete_model(id) == fp.OK:
            print("Deleted!")
        else:
            print("Failed to delete")
    elif inp == "r":
        if sensor.empty_library() == fp.OK:
            print("Library empty!")
        else:
            print("Failed to empty library")
    elif inp == "q":
        quit()
    else:
        print("Invalid input")
