import json
from pyfingerprint.pyfingerprint import PyFingerprint

# Function to delete all fingerprint templates from sensor
def delete_all_fingerprint_templates():
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
        if not f.verifyPassword():
            raise ValueError('The given fingerprint sensor password is wrong!')

        for i in range(f.getTemplateCount()):
            if f.deleteTemplate(i):
                print(f'Fingerprint template at position {i} deleted successfully!')
            else:
                print(f'Failed to delete the fingerprint template at position {i}.')
    
    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))


# Function to clear the JSON file containing Aadhaar IDs and corresponding fingerprint templates
def clear_fdb():
    try:
        # Open the file in write mode ('w') to clear its contents
        with open('fingerprint.fdb', 'w') as file:
            file.truncate(0)  # Truncate the file to remove all data
        print('Data cleared successfully from fingerprint.fdb!')
    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))


# Main function
def main():
    # Delete all fingerprint templates from the sensor
    delete_all_fingerprint_templates()

    # Clear the JSON file
    clear_fdb()


if __name__ == "__main__":
    main()
