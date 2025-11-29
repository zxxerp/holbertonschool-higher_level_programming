import json


def serialize_and_save_to_file(data, filename):
    """
    Takes a Python dictionary (data) and saves it to a file in JSON format.
    Cybersec Context: Like malware saving stolen credentials to a local file
    before exfiltrating them.
    """
    # 'w' mode means write. It will create the file or overwrite it.
    with open(filename, 'w') as f:
        # json.dump takes the object and the file handler
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Reads a JSON file and turns it back into a Python dictionary.
    Cybersec Context: Like a security tool reading a config file to set up
    firewall rules.
    """
    # 'r' mode means read.
    with open(filename, 'r') as f:
        # json.load reads the file and returns the Python object
        return json.load(f)
