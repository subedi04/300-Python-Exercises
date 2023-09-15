'''
Write A Python Program To Generate OTP 
On User Request And Send Code To Mobile Number
'''
import random

def generate_otp():
    """Generate a 6-digit OTP."""
    return str(random.randint(100000, 999999))

def send_sms(mobile_number, otp):
    """Mock method to simulate sending an OTP to a mobile number."""
    print(f"OTP sent to {mobile_number}: {otp}")

def main():
    mobile_number = input("Enter your mobile number: ")
    otp = generate_otp()
    send_sms(mobile_number, otp)
    # In a real-world scenario, you'd use an actual SMS gateway API to send the OTP.

main()
