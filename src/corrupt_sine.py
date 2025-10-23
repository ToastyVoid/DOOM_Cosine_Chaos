#!/usr/bin/env python3
import re, math

print("=== MOVEMENT-SPECIFIC CHAOS INJECTOR ===")

with open('tables.c', 'r') as f:
    content = f.read()

# Strategy: Corrupt the SPECIFIC parts of tables that movement likely uses
# Movement typically uses angles around the player's current orientation

def corrupt_movement_zones(numbers, table_name):
    """Corrupt the parts of the table that movement calculations likely use"""
    corrupted = numbers.copy()
    table_size = len(numbers)
    
    # Movement typically uses current view angle ± 45 degrees
    # In DOOM's angle system, this is roughly the middle ranges
    
    if table_name in ['finesine', 'finecosine']:
        # Target the "forward movement" ranges (angles ~0, ~1024, ~2048, etc.)
        for center in [0, 1024, 2048, 3072, 4096, 5120, 6144, 7168]:
            for offset in range(-200, 201):  # ±200 angle units
                idx = (center + offset) % table_size
                if 0 <= idx < table_size:
                    # Apply heavy corruption to movement ranges
                    if center in [0, 2048, 4096, 6144]:  # Cardinal directions
                        corrupted[idx] = int(corrupted[idx] * 0.5 + math.sin(idx * 0.2) * 4000)
                    else:  # Diagonal directions  
                        corrupted[idx] = int(corrupted[idx] * 0.7 + math.cos(idx * 0.15) * 2000)
    
    elif table_name == 'finetangent':
        # Tangent is used for slopes and angles - corrupt it differently
        for i in range(len(corrupted)):
            if i % 512 < 256:  # Corrupt in chunks
                corrupted[i] = int(corrupted[i] * (0.6 + 0.4 * math.sin(i * 0.05)))
    
    return corrupted

# Apply movement-specific corruption
for table_name in ['finesine', 'finecosine']:
    print(f"Targeting movement zones in {table_name}...")
    pattern = rf'(fixed_t {table_name}\[5\*FINEANGLES/4\] = \{{)([^}}]+)(\}};)'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        preamble, numbers_str, postamble = match.groups()
        numbers = [int(x.strip()) for x in numbers_str.split(',') if x.strip()]
        
        print(f"  Found {len(numbers)} values, applying movement-specific chaos...")
        corrupted_numbers = corrupt_movement_zones(numbers, table_name)
        
        new_content = preamble + '\n    ' + ',\n    '.join(map(str, corrupted_numbers)) + '\n' + postamble
        content = content[:match.start()] + new_content + content[match.end():]
        print(f"  Movement chaos injected into {table_name}!")

# Also let's try corrupting the specific ranges that p_user.c likely uses
print("Targeting player movement angle ranges...")

# Write the file
with open('tables.c', 'w') as f:
    f.write(content)

print("=== MOVEMENT CHAOS INJECTED! ===")