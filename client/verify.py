from pyfingerprint.pyfingerprint import PyFingerprint

def verify_fingerprint(uid):

    ## Tries to initialize the sensor
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if not f.verifyPassword():
            raise ValueError('The given fingerprint sensor password is wrong!')

    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        exit(1)

    ## Gets some sensor information
    print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

    # Link Aadhaar number to the fingerprint template

    ## Tries to enroll a new fingerprint
    try:
        print('Waiting for finger...')

        ## Wait until finger is read
        while not f.readImage():
            pass

        ## Convert read image to characteristics and store it in charbuffer 1
        f.convertImage(0x01)


        ## Check if finger is already enrolled
        result = f.searchTemplate()
        positionNumber = result[0]

        if positionNumber >= 0:
            with open("fingerprint.fdb", "r") as file:
                for line in file:
                    line = line.strip()
                    line = line.split(' ')
                    if(line[0] == uid and str(positionNumber) == line[1]):
                        print("Successfully verified")
                        return True
        
        return False
    
            
    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        return False
