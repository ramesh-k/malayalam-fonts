import os
import re

root_dir = 'fonts'
output_file = 'fonts.css'

# Match relative url(...) values, ignoring absolute and data URLs
url_pattern = re.compile(r'url\((?![a-z]+:|/)([^)]+)\)')

with open(output_file, 'w', encoding='utf-8') as outfile:
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            full_path = os.path.join(subdir, file)
            if file == 'main.css' and os.path.abspath(full_path) != os.path.abspath(output_file):
                with open(full_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()

                    # Fix relative URLs in url(...) statements
                    def fix_url(match):
                        original_url = match.group(1).strip('\'"')
                        asset_abs_path = os.path.normpath(os.path.join(subdir, original_url))
                        asset_rel_path = os.path.normpath(asset_abs_path).replace(os.sep, '/')
                        return f"url('{asset_rel_path}')"

                    fixed_content = url_pattern.sub(fix_url, content)
                    outfile.write(fixed_content)
                    outfile.write('\n\n')

print(f"✅ Combined CSS files into: {output_file}")
