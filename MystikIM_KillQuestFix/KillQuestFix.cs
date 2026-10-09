using System;
using System.Reflection;
using HarmonyLib;

public class MystikIM_KillQuestFixAPI : IModApi
{
    public void InitMod(Mod _modInstance)
    {
        var harmony = new Harmony("com.mystikim.killquestfix");
        harmony.PatchAll(Assembly.GetExecutingAssembly());
        Log.Out("[MystikIM_KillQuestFix] loaded - EntityKill analytics null-guard active");
    }
}

// V 3.3 builds an analytics event whenever a quest phase advances or a quest closes. For an
// EntityKill objective that uses target_tags (all Project Z contracts, ChaoticBountyBoard),
// entityNames is never filled in, so entityNames.Clone() throws a NullReferenceException.
// That aborts AdvancePhase/CloseQuest (no reward) and, on respawn, QuestJournal.StartQuests
// (stuck on "Building environment..."). Giving it an empty array first makes the original
// method run normally; kill matching ignores entityNames when target_tags is set.
[HarmonyPatch(typeof(ObjectiveEntityKill), "InternalToParametersDictionary")]
public class Patch_ObjectiveEntityKill_InternalToParametersDictionary
{
    static readonly FieldInfo EntityNamesField = AccessTools.Field(typeof(ObjectiveEntityKill), "entityNames");

    static void Prefix(ObjectiveEntityKill __instance)
    {
        try
        {
            if (EntityNamesField != null && EntityNamesField.GetValue(__instance) == null)
            {
                EntityNamesField.SetValue(__instance, new string[0]);
            }
        }
        catch (Exception e)
        {
            Log.Warning("[MystikIM_KillQuestFix] guard failed: " + e.Message);
        }
    }
}
