def calculate_storage(filesize):
    block_size = 4096

    # Calculate full blocks
    full_blocks = filesize // block_size

    # Calculate remainder
    partial_block_remainder = filesize % block_size

    # Determine total storage needed
    if partial_block_remainder > 0:
        return (full_blocks + 1) * block_size  # Add a block for the remainder
    else:
        return full_blocks * block_size

# Test the function
print(calculate_storage(1))    # Output: 4096
print(calculate_storage(4096)) # Output: 4096
print(calculate_storage(4097)) # Output: 8192
print(calculate_storage(6000)) # Output: 8192
