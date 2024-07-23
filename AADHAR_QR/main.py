
"""
This marks the main file where the code execution starts.

Returns:
    json object: json object containing aadhar data
"""
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from control.aadhar_qr_parser import get_aadhaar_info_qr

# This is the Base Class Model that accepts aadhar qr data
class AadharQr(BaseModel):
    aadhaarqrdata: str

# Initializing FastAPI
app = FastAPI()

# Defining the post method
@app.post("/aadhaar/getaadhaarinfo/qrdata/")
async def get_aadhar_data(aadhar_data: AadharQr):
    """
    This function marks the start of code execution

    Args:
        aadhar_data (AadharQr): BaseModel that accepts Aadhar QR data

    Returns:
        json object: json object containing aadhar data
    """
    value = get_aadhaar_info_qr(aadhar_data.aadhaarqrdata)  # calling function
    return value  # returns json object

# Application starts on the mentioned port
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=9009, reload=True)
