#!/usr/bin/env bash

# Short GPLv3 header that will be auto-added
HEADER="# This file is licensed under the GNU General Public License v3.0 (GPLv3).
# See the LICENSE file or https://www.gnu.org/licenses/ for details.
"

HOOK_FILE=".git/hooks/pre-commit"

mkdir -p .git/hooks

cat > "$HOOK_FILE" << 'EOF'
#!/usr/bin/env bash
echo "Adding headers"

HEADER_LINE="This file is licensed under the GNU General Public License v3.0 (GPLv3)."

read -r -d '' HEADER << EOH
# This file is licensed under the GNU General Public License v3.0 (GPLv3).
# See the LICENSE file or https://www.gnu.org/licenses/ for details.

EOH

# Get staged files
FILES=$(git diff --cached --name-only --diff-filter=ACM)

for f in $FILES; do

    # Skip removed or non-existent files
    [ -f "$f" ] || continue

    # Detect binary files — skip them
    if file "$f" | grep -qi "binary"; then
        echo "Skipping binary file: $f"
        continue
    fi

    # Check if file already contains the header
    if grep -qF "$HEADER_LINE" "$f"; then
        continue
    fi

    echo "➕ Adding GPLv3 header to: $f"

    # Prepend the header to the file
    tmpfile=$(mktemp)
    printf "%s" "$HEADER" > "$tmpfile"
    cat "$f" >> "$tmpfile"
    mv "$tmpfile" "$f"

    # Re-add the modified file to staging
    git add "$f"
done

exit 0
EOF

chmod +x "$HOOK_FILE"

echo "✔ Pre-commit hook installed."
echo "✔ Missing GPLv3 headers will now be added automatically."

