# pip install adafruit-circuitpython-fingerprint
import adafruit_fingerprint as fp
import serial


usb = serial.Serial("/dev/ttyUSB0", baudrate=57600, timeout=1)
sensor = fp.Adafruit_Fingerprint(usb)


def search():
    print("Place finger on the sensor...", end=" ", flush=True)
    i = fp.NOFINGER
    while i == fp.NOFINGER:
        i = sensor.get_image()
    if i == fp.OK:
        print("Image taken")
    else:
        if i == fp.NOFINGER:
            print("No finger detected")
        elif i == fp.IMAGEFAIL:
            print("Imaging error")
        else:
            print("Other error")
        return i

    print("Templating...", end=" ", flush=True)
    i = sensor.image_2_tz(1)
    if i == fp.OK:
        print("Templated")
    else:
        if i == fp.IMAGEMESS:
            print("Image too messy")
        elif i == fp.FEATUREFAIL:
            print("Could not identify features")
        elif i == fp.INVALIDIMAGE:
            print("Image invalid")
        else:
            print("Other error")
        return i

    print("Searching...", end=" ", flush=True)
    i = sensor.finger_fast_search()
    if i == fp.OK:
        print("Found fingerprint!")
    else:
        if i == fp.NOTFOUND:
            print("No match found")
        else:
            print("Other error")
        return i

    return i


def enroll(id):
    for itr in range(2):
        print(f"Place finger on the sensor{" again"*itr}...", end=" ", flush=True)
        i = sensor.get_image()
        while i == fp.NOFINGER:
            i = sensor.get_image()
        if i == fp.OK:
            print("Image taken")
        else:
            if i == fp.IMAGEFAIL:
                print("Imaging error")
            else:
                print("Other error")
            return i

        print("Templating...", end=" ", flush=True)
        i = sensor.image_2_tz(itr+1)
        if i == fp.OK:
            print("Templated")
        else:
            if i == fp.IMAGEMESS:
                print("Image too messy")
            elif i == fp.FEATUREFAIL:
                print("Could not identify features")
            elif i == fp.INVALIDIMAGE:
                print("Image invalid")
            else:
                print("Other error")
            return i

        if itr == 0:
            print("Remove finger")
            while i != fp.NOFINGER:
                i = sensor.get_image()

    print("Creating model...", end=" ", flush=True)
    i = sensor.create_model()
    if i == fp.OK:
        print("Created")
    else:
        if i == fp.ENROLLMISMATCH:
            print("Prints did not match")
        else:
            print("Other error")
        return i

    print(f"Storing model #{id}...", end=" ", flush=True)
    i = sensor.store_model(id)
    if i == fp.OK:
        print("Stored")
    else:
        if i == fp.BADLOCATION:
            print("Bad storage location")
        elif i == fp.FLASHERR:
            print("Flash storage error")
        else:
            print("Other error")
        return i

    return i


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
