#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

MARK_BEGIN='# >>> torturette >>>'
MARK_END='# <<< torturette <<<'
ALIAS_LINE="alias torturette='make -C \"$REPO_ROOT\" -f .src/Makefile all'"
SCRIPT_MARKER='# torturette-managed'

# Preferred path: drop an executable straight into a directory already on
# PATH. A shell resolves an unhashed command name by searching PATH fresh,
# so this works in the very same terminal that ran `make` - no new shell,
# no sourcing the rc file. The rc-file alias below is only a fallback for
# the rare case where neither candidate directory is on PATH.
BIN_DIR=""
for d in "$HOME/.local/bin" "$HOME/bin"; do
	case ":$PATH:" in
		*":$d:"*)
			mkdir -p "$d" 2>/dev/null || true
			if [ -w "$d" ]; then
				BIN_DIR="$d"
				break
			fi
			;;
	esac
done

if [ -n "$BIN_DIR" ]; then
	cat > "$BIN_DIR/torturette" <<SCRIPT_EOF
#!/usr/bin/env bash
$SCRIPT_MARKER
exec make -C "$REPO_ROOT" -f .src/Makefile all "\$@"
SCRIPT_EOF
	chmod +x "$BIN_DIR/torturette"
else
	for rc in "$HOME/.bashrc" "$HOME/.zshrc"; do
		if [ -f "$rc" ] && ! grep -qF "$MARK_BEGIN" "$rc"; then
			{
				echo "$MARK_BEGIN"
				echo "$ALIAS_LINE"
				echo "$MARK_END"
			} >> "$rc"
		fi
	done
fi

mkdir -p "$REPO_ROOT/docs"
mv "$REPO_ROOT/.src/RTFM.en.md" "$REPO_ROOT/docs/RTFM.en.md"
mv "$REPO_ROOT/.src/RTFM.es.md" "$REPO_ROOT/docs/RTFM.es.md"

cat > "$REPO_ROOT/.uninstall" <<UNINSTALL_EOF
#!/usr/bin/env bash
set -euo pipefail

UROOT="\$(cd "\$(dirname "\${BASH_SOURCE[0]}")" && pwd)"
cd "\$UROOT"

for d in "\$HOME/.local/bin" "\$HOME/bin"; do
	f="\$d/torturette"
	if [ -f "\$f" ] && grep -qF '$SCRIPT_MARKER' "\$f" 2>/dev/null; then
		rm -f "\$f"
	fi
done

for rc in "\$HOME/.bashrc" "\$HOME/.zshrc"; do
	if [ -f "\$rc" ] && grep -qF '$MARK_BEGIN' "\$rc"; then
		sed -i.bak "/^$MARK_BEGIN\$/,/^$MARK_END\$/d" "\$rc"
	fi
done

[ -f "\$UROOT/docs/RTFM.en.md" ] && mv "\$UROOT/docs/RTFM.en.md" "\$UROOT/.src/RTFM.en.md"
[ -f "\$UROOT/docs/RTFM.es.md" ] && mv "\$UROOT/docs/RTFM.es.md" "\$UROOT/.src/RTFM.es.md"
rmdir "\$UROOT/docs" 2>/dev/null || true

cp "\$UROOT/.src/.backup/Makefile" "\$UROOT/Makefile"
cp "\$UROOT/.src/.backup/README.md" "\$UROOT/README.md"
cp "\$UROOT/.src/.backup/bootstrap_install.sh" "\$UROOT/.src/bootstrap_install.sh"
chmod +x "\$UROOT/.src/bootstrap_install.sh"

rm -f "\$UROOT/.uninstall"

echo "Goodbye."
UNINSTALL_EOF
chmod +x "$REPO_ROOT/.uninstall"

echo "open ./docs"

rm -f "$REPO_ROOT/Makefile"
rm -f "$REPO_ROOT/README.md"
rm -f "$REPO_ROOT/.src/bootstrap_install.sh"
