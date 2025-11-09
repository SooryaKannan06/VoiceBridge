
# Copy all template and static files from the original project
import shutil

# Copy templates directory
src_templates = "voice-bridge/templates"
dst_templates = f"{base_dir}/templates"

if os.path.exists(src_templates):
    for file in os.listdir(src_templates):
        shutil.copy2(os.path.join(src_templates, file), os.path.join(dst_templates, file))
    print(f"✅ Copied {len(os.listdir(dst_templates))} HTML templates")
else:
    print("⚠️  Original templates not found, will recreate")

# Copy static files
src_static_css = "voice-bridge/static/css"
dst_static_css = f"{base_dir}/static/css"

src_static_js = "voice-bridge/static/js"
dst_static_js = f"{base_dir}/static/js"

if os.path.exists(src_static_css):
    for file in os.listdir(src_static_css):
        shutil.copy2(os.path.join(src_static_css, file), os.path.join(dst_static_css, file))
    print(f"✅ Copied CSS files")

if os.path.exists(src_static_js):
    for file in os.listdir(src_static_js):
        shutil.copy2(os.path.join(src_static_js, file), os.path.join(dst_static_js, file))
    print(f"✅ Copied JavaScript files")

print("\n📁 FREE Version project structure complete!")
