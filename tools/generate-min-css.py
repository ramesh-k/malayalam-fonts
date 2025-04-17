import os
import re

root_dir = 'fonts'
minified_output = 'fonts.css'

# Match relative url(...) values, ignoring absolute and data URLs
url_pattern = re.compile(r'url\((?![a-z]+:|/)([^)]+)\)')

combined_content = ""

# Step 1: Combine and fix URLs
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        full_path = os.path.join(subdir, file)
        if file == 'main.css':
            with open(full_path, 'r', encoding='utf-8') as infile:
                content = infile.read()

                # Fix relative URLs in url(...) statements
                def fix_url(match):
                    original_url = match.group(1).strip('\'"')
                    asset_abs_path = os.path.normpath(os.path.join(subdir, original_url))
                    asset_rel_path = os.path.normpath(asset_abs_path).replace(os.sep, '/')
                    return f"url('{asset_rel_path}')"

                fixed_content = url_pattern.sub(fix_url, content)
                combined_content += fixed_content + '\n\n'

# Step 2: Minify content
# Remove comments
minified_content = re.sub(r'/\*[^*]*\*+(?:[^/*][^*]*\*+)*/', '', combined_content)
# Remove spaces around symbols
minified_content = re.sub(r'\s*([{}:;,])\s*', r'\1', minified_content)
# Remove unnecessary semicolons and whitespace
minified_content = re.sub(r';+\}', '}', minified_content)
minified_content = re.sub(r'\s+', ' ', minified_content)
minified_content = minified_content.strip()

# Step 3: Save to .min.css
with open(minified_output, 'w', encoding='utf-8') as outfile:
    outfile.write(minified_content)

print(f"✅ Minified CSS saved as: {minified_output}")
