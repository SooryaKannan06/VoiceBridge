
# Recreate the project with free APIs
import os
import zipfile

project_name = "voice-bridge-free"
base_dir = project_name

# Create directories
directories = [
    f"{base_dir}",
    f"{base_dir}/static",
    f"{base_dir}/static/css",
    f"{base_dir}/static/js",
    f"{base_dir}/templates",
]

for directory in directories:
    os.makedirs(directory, exist_ok=True)

print("✅ Created directory structure for FREE version!")
