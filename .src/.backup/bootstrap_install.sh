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

UROOT="\$(cd "\$(dirname "\${BASH_SOURCE[0]}")" && pwd)"
cd "\$UROOT"

for rc in "\$HOME/.bashrc" "\$HOME/.zshrc"; do
	if [ -f "\$rc" ] && grep -qF '$MARK_BEGIN' "\$rc"; then
		sed -i.bak "/^$MARK_BEGIN\$/,/^$MARK_END\$/d" "\$rc"
		echo "Removed the torturette alias from \$rc"
	fi
done

[ -f "\$UROOT/RTFM.en.md" ] && mv "\$UROOT/RTFM.en.md" "\$UROOT/.src/RTFM.en.md"
[ -f "\$UROOT/RTFM.es.md" ] && mv "\$UROOT/RTFM.es.md" "\$UROOT/.src/RTFM.es.md"

cp "\$UROOT/.src/.backup/Makefile" "\$UROOT/Makefile"
cp "\$UROOT/.src/.backup/README.md" "\$UROOT/README.md"
cp "\$UROOT/.src/.backup/bootstrap_install.sh" "\$UROOT/.src/bootstrap_install.sh"
chmod +x "\$UROOT/.src/bootstrap_install.sh"

echo "Repo restored to its original state."
echo "Open a new shell (or re-source your rc file) for the alias removal to take effect."

rm -f "\$UROOT/.uninstall"
UNINSTALL_EOF
chmod +x "$REPO_ROOT/.uninstall"

echo "You have 15 minutes for entry on the exam"

rm -f "$REPO_ROOT/Makefile"
rm -f "$REPO_ROOT/README.md"
rm -f "$REPO_ROOT/.src/bootstrap_install.sh"
