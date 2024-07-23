# import json

# from pyaadhaar.decode import AadhaarSecureQr

# from control.json_creation import get_json_data

# #This function extract the aadhar data and returns the json object
# def get_aadhaar_info_qr(secured_qr_data):
#     try:
#         #Read the json structure from the file
#         json_data = json.load(open("./data/output.json"))
#         obj = AadhaarSecureQr(int(secured_qr_data))
#         output_json = get_json_data(json_data, obj)
#         return output_json
#     except Exception as e:
#         value = {
#             "status": "Failure",
#    	        "code": "1001",
#    	        "message": f"{e}"
#         }
#         return value


import os
import json
from pyaadhaar.decode import AadhaarSecureQr
# from control.decode1 import AadhaarSecureQr
from control.json_creation import get_json_data

def get_aadhaar_info_qr(secured_qr_data):
    try:
        output_file_path = "./data/output.json"
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        
        # Check if the file exists, if not create it with a default JSON structure
        if not os.path.exists(output_file_path):
            default_json_structure = {}  # Define your default JSON structure here
            with open(output_file_path, 'w') as f:
                json.dump(default_json_structure, f)

        # Read the JSON structure from the file
        with open(output_file_path, 'r') as f:
            json_data = json.load(f)
        
        print(f"JSON data read from file: {json_data}")  # Debugging information
        
        # Process the secured QR data
        obj = AadhaarSecureQr(int(secured_qr_data))
        
        print(f"Decoded Aadhaar data: {obj.decodeddata()}")  # Debugging information
        
        output_json = get_json_data(json_data, obj)
        
        print(f"Output JSON data: {output_json}")  # Debugging information
        
        return output_json
    except Exception as e:
        value = {
            "status": "Failure",
            "code": "1001",
            "message": str(e)
        }
        print(f"Error: {value}")  # Debugging information
        return value

