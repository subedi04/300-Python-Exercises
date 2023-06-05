'''
Write A Python Program To Get Memory In Bytes Then Convert Bytes In To GB

1 GB = 1024 MB
1 GB = 1024 * 1024 * 1024 Bytes = 1,073,741,824 Bytes
1 Byte = 1/1,073,741,824 GB

'''

bytes  = float(input("Enter memory in Bytes : ")) # 2
# 1GB = 1073741824 Bytes

memory_in_gb = bytes/1073741824 # 1024 * 1024 * 1024
print("bytes converted to GB is : "+str(memory_in_gb))