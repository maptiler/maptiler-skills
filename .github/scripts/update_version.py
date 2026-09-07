#!/usr/bin/env python3
import sys
import re
import argparse

# Mapping of library names to their URL/dependency packages for global updates
URL_IDENTIFIERS = {
    "maptiler sdk js": "maptiler-sdk-js",
    "maptiler client js": "maptiler-client-js",
    "geocoding control": "geocoding-control",
    "marker layout": "marker-layout",
    "elevation profile": "elevation-profile",
    "leaflet maptiler sdk": "leaflet-maptilersdk",
    "ar control": "ar-control",
    "map%tiler weather js": "maptiler-weather-js",
    "maptiler 3d plugin": "maptiler-3d",
    "maptiler geosplats sdk": "geosplats",
    "maptiler android (kotlin)": "maptiler-sdk-kotlin",
    "maptiler ios (swift)": "maptiler-sdk-ios",
}

def main():
    parser = argparse.ArgumentParser(description="Update library version in versions.md")
    parser.add_argument("--file", default="skills/references/versions.md", help="Path to the markdown file")
    parser.add_argument("--identifier", required=True, help="Library name or template variable identifier")
    parser.add_argument("--version", required=True, help="New version to set")
    parser.add_argument("--clean-v", action="store_true", help="Remove leading 'v' from the version string")

    args = parser.parse_args()

    file_path = args.file
    identifier = args.identifier
    new_version = args.version

    if args.clean_v and new_version.startswith('v'):
        new_version = new_version[1:]

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}", file=sys.stderr)
        sys.exit(1)

    lines = content.splitlines()
    updated = False
    old_version = None
    matched_library_name = None

    new_lines = []
    for line in lines:
        # Match table rows
        if line.strip().startswith('|') and line.strip().endswith('|'):
            parts = line.split('|')
            if len(parts) >= 4:
                col1 = parts[1].strip().strip('`').strip() # e.g., {{site.versions.sdk}}
                col2 = parts[2].strip().strip('*').strip() # e.g., MapTiler SDK JS
                col3 = parts[3].strip() # e.g., `v4.0.2` or 1.3.1
                
                # Normalizing for matching
                norm_id = identifier.strip().lower()
                if norm_id in ("client-js", "client_js"):
                    norm_id = "client"
                
                col1_clean = col1.lower()
                col1_var = col1.replace('{{', '').replace('}}', '').strip().lower() # site.versions.sdk
                col1_short = col1_var.split('.')[-1] if '.' in col1_var else col1_var # sdk
                
                col2_clean = col2.lower()
                
                match = False
                if (norm_id == col1_clean or 
                    norm_id == col1_var or 
                    norm_id == col1_short or 
                    norm_id == col2_clean or
                    norm_id == col2_clean.replace('**', '').strip()):
                    match = True

                if match:
                    # Found the target library row!
                    # Extract old version
                    old_version = col3.strip('`').strip()
                    matched_library_name = col2
                    
                    has_backticks = col3.startswith('`') and col3.endswith('`')
                    wrapped_version = f"`{new_version}`" if has_backticks else new_version
                    
                    parts[3] = f" {wrapped_version} "
                    line = '|'.join(parts)
                    updated = True

        new_lines.append(line)

    if not updated:
        print(f"Warning: Identifier '{identifier}' not found in versions table. No update performed.")
        sys.exit(0)


    # Reconstruct updated markdown content
    updated_content = '\n'.join(new_lines) + '\n'

    # If we found an old version and there's a mapped package identifier, update CDN and dependencies
    if old_version and matched_library_name:
        norm_lib_name = matched_library_name.lower().replace('**', '').strip()
        package_id = URL_IDENTIFIERS.get(norm_lib_name)
        if package_id:
            print(f"Mapped library '{matched_library_name}' to package ID '{package_id}'")
            # Build search and replace patterns to update URLs and other occurrences
            # 1. URL pattern: package_id/v1.2.3/ -> package_id/v2.3.4/ or package_id/1.2.3/ -> package_id/2.3.4/
            # We want to match /package_id/old_version/
            url_old = f"/{package_id}/{old_version}/"
            url_new = f"/{package_id}/{new_version}/"
            
            # 2. Dependency pattern (Maven/Gradle): package_id:old_version -> package_id:new_version
            dep_old = f"{package_id}:{old_version}"
            dep_new = f"{package_id}:{new_version}"
            
            # 3. npm/CDN tag pattern: package_id@old_version -> package_id@new_version
            npm_old = f"{package_id}@{old_version}"
            npm_new = f"{package_id}@{new_version}"

            # Replace occurrences in the updated_content
            replacements = []
            if url_old in updated_content:
                updated_content = updated_content.replace(url_old, url_new)
                replacements.append(f"URLs ({url_old} -> {url_new})")
            if dep_old in updated_content:
                updated_content = updated_content.replace(dep_old, dep_new)
                replacements.append(f"Dependencies ({dep_old} -> {dep_new})")
            if npm_old in updated_content:
                updated_content = updated_content.replace(npm_old, npm_new)
                replacements.append(f"CDN references ({npm_old} -> {npm_new})")
                
            if replacements:
                print(f"Also updated in file: {', '.join(replacements)}")

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"Successfully updated '{matched_library_name}' to version '{new_version}' in {file_path}")
    except Exception as e:
        print(f"Error writing file {file_path}: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
