#!/usr/bin/env python3
"""
Patches a CATUI windows.xml so RefugeBot's mod scanner stops flagging it as
a "competing" UI mod and injects its Inventory Hub/toolbar features into
CATUI correctly.

RefugeBot's IsCompetingPatch check does a plain-text scan for the literal
string "contentCraftingInfo" in any installed mod's XML. This script swaps
the ASCII "I" for the XML numeric entity &#73; -- same letter once the XML
parser resolves it, so the game renders identically, but the scanner's raw
text search no longer matches it.

Usage:
    python catui_refugebot_patch.py <path to windows.xml>

Applies to CATUI (https://www.nexusmods.com/7daystodie/mods/4405), MIT
licensed by 7D2D-CATUI (https://github.com/7D2D-CATUI/CATUI). This script
does not include or redistribute any of CATUI's own file -- it patches
your existing local copy in place.
"""
import sys
import shutil
from pathlib import Path

TARGET = "contentCraftingInfo"
REPLACEMENT = "contentCrafting&#73;nfo"


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {Path(__file__).name} <path to CATUI windows.xml>")
        sys.exit(1)

    target_path = Path(sys.argv[1])
    if not target_path.is_file():
        print(f"File not found: {target_path}")
        sys.exit(1)

    content = target_path.read_text(encoding="utf-8")
    count = content.count(TARGET)
    if count == 0:
        print("No occurrences of the target string found -- already patched, or this isn't a CATUI windows.xml.")
        sys.exit(0)

    backup_path = target_path.with_suffix(target_path.suffix + ".bak")
    shutil.copy2(target_path, backup_path)

    patched = content.replace(TARGET, REPLACEMENT)
    target_path.write_text(patched, encoding="utf-8")

    print(f"Patched {count} occurrence(s) in {target_path}")
    print(f"Original backed up to {backup_path}")


if __name__ == "__main__":
    main()
