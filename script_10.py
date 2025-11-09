
# Create final ZIP file with FREE version

zip_filename = "voice-bridge-FREE.zip"

# Create zip file
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, os.path.dirname(base_dir))
            zipf.write(file_path, arcname)

print("\n" + "="*70)
print("🎉 VOICE BRIDGE - FREE VERSION READY!")
print("="*70)
print(f"✅ ZIP file created: {zip_filename}")
print("\n💰 NO PAYMENT REQUIRED!")
print("✅ NO Google Cloud")
print("✅ NO API Keys")
print("✅ NO Credit Card")
print("✅ 100% FREE Forever!")
print("="*70)

# List contents
with zipfile.ZipFile(zip_filename, 'r') as zipf:
    file_list = zipf.namelist()
    print(f"\n📦 Total files: {len(file_list)}")
    print("\n📁 Project structure:")
    for file in sorted(file_list):
        print(f"  {file}")

file_size = os.path.getsize(zip_filename)
print(f"\n📊 ZIP file size: {file_size:,} bytes ({file_size/1024:.2f} KB)")

print("\n" + "="*70)
print("🚀 QUICK START:")
print("="*70)
print("1. Extract the ZIP file")
print("2. cd voice-bridge-free")
print("3. pip install -r requirements.txt")
print("4. python app.py")
print("5. Visit http://localhost:5000")
print("="*70)
print("\n✨ Uses FREE libraries: SpeechRecognition, googletrans, gTTS")
print("💬 No payment ever! Enjoy breaking language barriers! 🌉")
print("="*70)
