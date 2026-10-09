# MystikIM Kill Quest Fix

Fixes a 7 Days to Die V 3.3 bug where kill contracts that use `target_tags` (all Project Z contracts, ChaoticBountyBoard bounties) throw a `NullReferenceException` when a phase finishes or a quest closes.

**Symptoms:** a finished contract pays no reward, and/or the game sticks on "Building environment..." after joining because the quest journal fails to reload.

**Cause:** V 3.3 logs an analytics event for these quests and calls `entityNames.Clone()`, but `entityNames` is only filled in for objectives that list entity names, never for tag-based ones.

**Fix:** a tiny Harmony patch gives the objective an empty list first so the original code runs normally. Kill matching is unchanged.

## Install
Copy this folder into your client's `Mods` folder (`%APPDATA%\7DaysToDie\Mods`). Needs to be on the **player's** PC; the server does not need it.
