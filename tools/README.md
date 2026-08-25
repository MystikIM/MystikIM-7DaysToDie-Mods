# Tools

Standalone scripts, not mods — nothing here is installed as a `Mods/<name>` folder.

## `catui_refugebot_patch.py`

Patches your own local [CATUI](https://www.nexusmods.com/7daystodie/mods/4405) `windows.xml`
so RefugeBot's mod scanner stops flagging it as "competing" and injects its
Inventory Hub/toolbar features into CATUI correctly. Applies the same fix used
in `ZZZ_CATUI_ProjectZ_fit` (see that mod's README for the technical details)
directly to your own CATUI install.

```
python catui_refugebot_patch.py "path/to/ZZZ_CATUI/Config/XUi_InGame/windows.xml"
```

Backs up your original file first (`.bak`), then patches in place. Run it on
**both** your client and server copies of CATUI.

CATUI is MIT licensed by [7D2D-CATUI](https://github.com/7D2D-CATUI/CATUI) —
this script doesn't include or redistribute any of CATUI's own file, it just
patches the copy you already have.
