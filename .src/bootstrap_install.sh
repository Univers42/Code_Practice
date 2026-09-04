#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

MARK_BEGIN='# >>> torturette >>>'
MARK_END='# <<< torturette <<<'
ALIAS_LINE="alias torturette='make -C \"$REPO_ROOT\" -f .src/Makefile all'"

for rc in "$HOME/.bashrc" "$HOME/.zshrc"; do
	if [ -f "$rc" ] && ! grep -qF "$MARK_BEGIN" "$rc"; then
		{
			echo "$MARK_BEGIN"
			echo "$ALIAS_LINE"
			echo "$MARK_END"
		} >> "$rc"
	fi
done

mv "$REPO_ROOT/.src/RTFM.en.md" "$REPO_ROOT/RTFM.en.md"
mv "$REPO_ROOT/.src/RTFM.es.md" "$REPO_ROOT/RTFM.es.md"

cat > "$REPO_ROOT/.uninstall" <<UNINSTALL_EOF
#!/usr/bin/env bash
set -euo pipefail
for rc in "\$HOME/.bashrc" "\$HOME/.zshrc"; do
	if [ -f "\$rc" ] && grep -qF '$MARK_BEGIN' "\$rc"; then
		sed -i.bak "/^$MARK_BEGIN\$/,/^$MARK_END\$/d" "\$rc"
		echo "Removed the torturette alias from \$rc"
	fi
done
echo "Uninstalled. Open a new shell (or re-source your rc file) for it to take effect."
UNINSTALL_EOF
chmod +x "$REPO_ROOT/.uninstall"

echo "You have 15 minutes for entry on the exam"

rm -f "$REPO_ROOT/Makefile"
rm -f "$REPO_ROOT/.src/bootstrap_install.sh"
