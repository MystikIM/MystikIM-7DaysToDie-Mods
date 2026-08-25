# CATUI_ProjectZ_fit

A small compatibility patch that fits [Project Z](https://7dtdprojectz.com/)'s wider UI panels into [CATUI](https://www.nexusmods.com/7daystodie/mods/4405)'s rebuilt layout, without editing either mod directly.

Built to replace the official `ZZZ_CATUI_ProjectZ_compatible` patch, which is outdated and reintroduces a real crash (see below).

## The problem

Project Z removes and completely redefines several shared vanilla windows (`craftingInfoPanel`, `windowBackpack`) to fit its own wider layout — Project Z's panels are ~816px wide vs. vanilla's ~603px. CATUI *also* rebuilds those same windows, but its rebuild is hardcoded to vanilla's narrower dimensions. Run both mods together with nothing bridging them and CATUI's rebuild ends up positioned/sized for a panel that's no longer there — search tabs, ingredients list, and stat panel all render in the wrong place, overlapping Project Z's wider `itemActions` column.

This mod patches *on top of both*, repositioning CATUI's rebuilt elements to match Project Z's actual dimensions. It has to load after `ZZZ_CATUI` alphabetically, since it references CATUI's own rebuilt element names (`CATUI_quality_item`, `CATUI_ingredients`, the `stat` tab CATUI inserts) — that's why the folder is prefixed `ZZZ_` too.

## What's fixed

- `craftingInfoPanel`'s preview box, search tabs (ingredients/description/stats), and crafting queue cell sizes are repositioned/resized to fit Project Z's wider panel instead of vanilla's.

## What's intentionally *not* included

The old `ZZZ_CATUI_ProjectZ_compatible` patch also re-added a `recipeCraftCountControl` (the craft-quantity stepper) directly inside CATUI's rebuilt `preview` box. That's the actual cause of a `NullReferenceException` in `XUiC_IngredientEntry.Init()` that crashes every crafting window the moment CATUI removes and rebuilds `preview` — deliberately left out here. The real fix for that control lives in Project Z's own `windows.xml` instead: relocate it into the `itemActions` grid (which CATUI never touches), matching where vanilla puts it in the first place.

## What's *not* fixed here

`windowBackpack`'s inventory grid uses a custom `<backpack_item_stack>` element (not vanilla/CATUI's `<item_stack>`), which is almost certainly tied to Project Z's own custom grid controller for binding/populating slots. An earlier attempt to swap that element type to match CATUI's expectations broke the binding entirely — the grid rendered with zero items. If you want to try fixing 135-slot-style backpack mods stacked on top of Project Z, don't touch the element type; look at `cell_width`/`cell_height`/`transform_scale` on the grid instead.

## Installing

This is UI-only content, resolved client-side — install on **both** server and client, same as CATUI itself.

1. Extract into `7 Days to Die Dedicated Server/Mods/` (server) **and** `7 Days To Die/Mods/` (client).
2. Load order matters: `Project Z` → `ZZZ_CATUI` → `ZZZ_CATUI_ProjectZ_fit` (alphabetical folder order handles this automatically as long as none of the names are renamed).
3. Restart the server for the server-side install to take effect (XML patches load once at boot).

## Requirements

- [Project Z](https://7dtdprojectz.com/) 3.1.2
- [CATUI](https://www.nexusmods.com/7daystodie/mods/4405) 3.0.13, pure/unmodified — this patch assumes stock CATUI, not a version with other local edits.
