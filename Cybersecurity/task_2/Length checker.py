
import struct, zlib , subprocess


orignal_path = "/home/thewildwest/Downloads/challenge.png"
fixed_path = "/home/thewildwest/code/fixed.png"

with open(orignal_path, "rb") as f:
    data = f.read()

#length change
newlength = 200
breakcode = False
while breakcode==False and newlength <= 450:

    #print(f"Correct length: {newlength:#010x}")

    patched_length = data[:20] + struct.pack(">i",newlength) + data[24:]
    with open(fixed_path, "wb") as f:
        f.write(patched_length)



    with open(fixed_path, "rb") as f:
        data_2 =f.read()



    # IHDR chunk data is at bytes 12-28 (after 8-byte signature + 4-byte length + 4-byte type)
    ihdr_data = data_2[12:29]  #4 (IHDR) + 13 (data) = offset 12 to 28
    chunk_type_and_data = data_2[12:29]  # 13 bytes of data

    correct_crc = zlib.crc32(chunk_type_and_data) & 0xFFFFFFFF
    #print(f"Correct CRC: {correct_crc:#010x}")


    # Patch: replace bytes 29-33 with correct CRC
    patched = data_2[:29] + struct.pack(">I", correct_crc) + data_2[33:]
    with open(fixed_path, "wb") as f:
        f.write(patched)


    result = subprocess.run(["pngcheck" , "-v" , fixed_path] , stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    match result.returncode:
        case 0:
            subprocess.run(["pngcheck" , "-v" , fixed_path] )
            breakcode = True
            break
                
    newlength += 1
    print(newlength)





"""
resultex = subprocess.run(["pngcheck" , "-v" , "/home/thewildwest/Downloads/test.png"] , stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
match resultex.returncode:
    case 0:
        print("done")
        subprocess.run(["pngcheck" , "-v" , "/home/thewildwest/Downloads/test.png"] )
"""