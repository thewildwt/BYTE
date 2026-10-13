import struct, zlib

with open("/home/thewildwest/Downloads/challenge.png", "rb") as f:
    data = f.read()

# IHDR chunk data is at bytes 12-28 (after 8-byte signature + 4-byte length + 4-byte type)
ihdr_data = data[12:29]  # 4 (length) + 4 (IHDR) + 13 (data) = offset 12 to 28
chunk_type_and_data = data[12:29]  # just "IHDR" + 13 bytes of data

correct_crc = zlib.crc32(chunk_type_and_data) & 0xFFFFFFFF
print(f"Correct CRC: {correct_crc:#010x}")

# Patch: replace bytes 29-33 with correct CRC
patched = data[:29] + struct.pack(">I", correct_crc) + data[33:]
with open("fixed.png", "wb") as f:
    f.write(patched)