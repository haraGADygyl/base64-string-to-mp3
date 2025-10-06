import base64

# Your Base64 string
base64_string = "string"

# Remove the "data:audio/mp3;base64," prefix if it exists
base64_string = base64_string.replace("data:audio/wav;base64,", "")

# Decode the string back to binary data
binary_data = base64.b64decode(base64_string)

# The name of the new audio file you want to create
file_name = "output_audio.mp3"

# Write the binary data to a file
with open(file_name, 'wb') as f:
    f.write(binary_data)

print(f"Audio file '{file_name}' saved successfully.")
