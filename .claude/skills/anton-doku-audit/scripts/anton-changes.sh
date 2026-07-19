#!/usr/bin/env bash
# Zeigt das Audit-Fenster: welche Anton-Commits seit dem letzten Doku-Audit
# gelandet sind, plus den kuratierten [Unreleased]-Abschnitt des Anton-CHANGELOG.
#
# Aufruf:
#   scripts/anton-changes.sh                 # seit state/last-audited.sha
#   scripts/anton-changes.sh <ref>           # seit <ref> (SHA/Tag), ignoriert State
#   scripts/anton-changes.sh -n 25           # die letzten 25 Commits
#
# Ändert NICHTS und schreibt den State NICHT fort — das macht der Skill bewusst
# erst, nachdem das Audit abgeschlossen und committet ist.

set -euo pipefail

ANTON="${ANTON_REPO:-$HOME/Sites/anton.test}"
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STATE="$SKILL_DIR/state/last-audited.sha"

if [ ! -d "$ANTON/.git" ]; then
  echo "FEHLER: Anton-Repo nicht unter '$ANTON' gefunden. ANTON_REPO=… setzen." >&2
  exit 1
fi

RANGE=""
if [ "${1:-}" = "-n" ]; then
  COUNT="${2:?-n braucht eine Zahl}"
  RANGE="-n $COUNT"
  DESC="die letzten $COUNT Commits"
elif [ -n "${1:-}" ]; then
  RANGE="${1}..HEAD"
  DESC="seit ${1}"
else
  if [ ! -f "$STATE" ]; then
    echo "FEHLER: kein State unter $STATE und kein Ref angegeben." >&2
    exit 1
  fi
  LAST="$(tr -d '[:space:]' < "$STATE")"
  RANGE="${LAST}..HEAD"
  DESC="seit zuletzt auditiertem Commit ${LAST:0:9}"
fi

echo "================================================================"
echo " Anton-Doku-Audit-Fenster — $DESC"
echo " Anton HEAD: $(git -C "$ANTON" rev-parse --short HEAD)"
echo "================================================================"
echo
echo "### Commits (kompakt) ###"
# shellcheck disable=SC2086
git -C "$ANTON" log --oneline $RANGE || true
echo
echo "### Commits (voller Text + Datei-Stat) ###"
# shellcheck disable=SC2086
git -C "$ANTON" log --stat $RANGE || true
echo
echo "================================================================"
echo " CHANGELOG.md — Abschnitt [Unreleased] (kuratierte Destillation)"
echo "================================================================"
awk '/^## \[Unreleased\]/{f=1;next} /^## \[/{if(f)exit} f' "$ANTON/CHANGELOG.md" || true
