bits = int(input("Enter the number of bits: "))
megabytes = bits / (8 * 1024 * 1024)
gigabytes = bits / (8 * 1024 * 1024 * 1024)
terabytes = bits / (8 * 1024 * 1024 * 1024 * 1024)

print(f"Bits: {bits}")
print(f"{megabytes:.4f} MB")
print(f"{gigabytes:.4f} GB")
print(f"{terabytes:.4f} TB")