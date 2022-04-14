#Global variables

globalvar Team1Ready 0
globalvar Team2Ready 1
globalvar GameMode 2
globalvar ScoreModified 3
globalvar TournamentMode 4
globalvar MapInfoLogged 12
globalvar InfoDrawn 14
globalvar MatchDelayAmount 15
globalvar AllowDCResume 16
globalvar FirstRoundDone 17
globalvar DVaRestore 19
globalvar UltCharges 20
globalvar Positions 21
globalvar ShouldRestore 22
globalvar Heroes 23
globalvar Cooldowns1 24
globalvar Cooldowns2 25


#Player variables

playervar IsUlting 0
playervar ReadyCD 1
playervar AddTimeCD 2
playervar HeroList 5


#Subroutine names

subroutine LogMapGamemodeInfo 0
subroutine LogHybridInfo 1
subroutine PlayerDCInfoTeam1 2
subroutine PlayerDCInfoTeam2 3
subroutine PlayerDCDvaTeam1 4
subroutine PlayerDCDvaTeam2 5
subroutine CreateSpectatorHUD 6


rule "Remove Assembling Heroes":
    @Condition isAssemblingHeroes() == true
    
    setMatchTime(0)
    wait(5)
    setMatchTime(50)


rule "Help HUD":
    @Condition isGameInProgress() == false
    @Condition InfoDrawn == false
    
    TournamentMode = createWorkshopSetting(bool, "OverStat", "Tournament Mode", false, 1)
    AllowDCResume = createWorkshopSetting(bool, "OverStat", "Allow Disconnect Resume", true, 2)
    MatchDelayAmount = createWorkshopSetting(int[15:600], "OverStat", "Match Delay Timer", 60, 3)
    Team1Ready = "Not Ready"
    Team2Ready = "Not Ready"
    hudSubheader(getAllPlayers(), "Press {0} + {1}: Ready / Unready".format(buttonString(Button.INTERACT), buttonString(Button.CROUCH)), HudPosition.RIGHT, 22, Color.AQUA, HudReeval.VISIBILITY_AND_STRING, SpecVisibility.NEVER)
    hudSubheader(getAllPlayers(), "Press {0}: Add extra {1} seconds to setup".format(buttonString(Button.ULTIMATE), MatchDelayAmount), HudPosition.RIGHT, 23, Color.WHITE, HudReeval.VISIBILITY_AND_STRING, SpecVisibility.NEVER)
    hudSubheader(getAllPlayers(), "Press {0}: Teleport (works only in Defense, in spawn)".format(buttonString(Button.MELEE)), HudPosition.RIGHT, 25, Color.ORANGE, HudReeval.VISIBILITY_AND_STRING, SpecVisibility.NEVER)
    hudSubheader(getAllPlayers(), "Hold {0}: Change hero (works only in Defense)".format(buttonString(Button.RELOAD)), HudPosition.RIGHT, 26, Color.YELLOW, HudReeval.VISIBILITY_AND_STRING, SpecVisibility.NEVER)
    hudHeader(getAllPlayers(), "{0} is {1}".format(Team.1, Team1Ready), HudPosition.TOP, 20, Color.GREEN if Team1Ready == "Ready" else Color.RED, HudReeval.VISIBILITY_STRING_AND_COLOR, SpecVisibility.ALWAYS)
    hudHeader(getAllPlayers(), "{0} is {1}".format(Team.2, Team2Ready), HudPosition.TOP, 21, Color.GREEN if Team2Ready == "Ready" else Color.RED, HudReeval.VISIBILITY_STRING_AND_COLOR, SpecVisibility.ALWAYS)
    InfoDrawn = true


rule "Game in Progress: Remove HUD, Reset variables":
    @Condition InfoDrawn == true
    @Condition isGameInProgress() == true
    
    Team1Ready = "Not Ready"
    Team2Ready = "Not Ready"
    destroyAllHudTexts()
    CreateSpectatorHUD()
    InfoDrawn = false


def CreateSpectatorHUD():
    @Name "Spectator HUD"
    
    if createWorkshopSetting(bool, "OverStat", "Enable Spectator Overlay", true, 0):
        #team 1
        hudSubtext(null, "Dmg Dealt - Dmg Taken - Final Blows - Deaths - Heals Dealt - Ults Used", HudPosition.LEFT, 0, Color.RED, HudReeval.VISIBILITY_AND_STRING, SpecVisibility.ALWAYS)
        hudSubtext(null, "{0}   {1} - {2}".format(heroIcon(getPlayersInSlot(0, Team.1).getCurrentHero()), ceil(getPlayersInSlot(0, Team.1).getStatistic(Stat.BARRIER_DAMAGE_DEALT) + getPlayersInSlot(0, Team.1).getStatistic(Stat.HERO_DAMAGE_DEALT)), "{0} - {1} - {2}".format(ceil(getPlayersInSlot(0, Team.1).getStatistic(Stat.DAMAGE_TAKEN)), getPlayersInSlot(0, Team.1).getStatistic(Stat.FINAL_BLOWS), "{0} - {1} - {2}".format(getPlayersInSlot(0, Team.1).getStatistic(Stat.DEATHS), ceil(getPlayersInSlot(0, Team.1).getStatistic(Stat.HEALING_DEALT)), "{0}  {1} {2}".format(getPlayersInSlot(0, Team.1).getStatistic(Stat.ULTIMATES_USED), abilityIconString(getPlayersInSlot(0, Team.1).getCurrentHero(), Button.ABILITY_2) if getPlayersInSlot(0, Team.1).getAbilityCooldown(Button.ABILITY_2) == 0 else "", abilityIconString(getPlayersInSlot(0, Team.1).getCurrentHero(), Button.ABILITY_1) if getPlayersInSlot(0, Team.1).getAbilityCooldown(Button.ABILITY_1) == 0 else "")))), HudPosition.LEFT, 1, Color.WHITE, HudReeval.VISIBILITY_AND_STRING, SpecVisibility.ALWAYS)
        hudSubtext(null, "{0}   {1} - {2}".format(heroIcon(getPlayersInSlot(1, Team.1).getCurrentHero()), ceil(getPlayersInSlot(1, Team.1).getStatistic(Stat.BARRIER_DAMAGE_DEALT) + getPlayersInSlot(1, Team.1).getStatistic(Stat.HERO_DAMAGE_DEALT)), "{0} - {1} - {2}".format(ceil(getPlayersInSlot(1, Team.1).getStatistic(Stat.DAMAGE_TAKEN)), getPlayersInSlot(1, Team.1).getStatistic(Stat.FINAL_BLOWS), "{0} - {1} - {2}".format(getPlayersInSlot(1, Team.1).getStatistic(Stat.DEATHS), ceil(getPlayersInSlot(1, Team.1).getStatistic(Stat.HEALING_DEALT)), "{0}  {1} {2}".format(getPlayersInSlot(1, Team.1).getStatistic(Stat.ULTIMATES_USED), abilityIconString(getPlayersInSlot(1, Team.1).getCurrentHero(), Button.ABILITY_2) if getPlayersInSlot(1, Team.1).getAbilityCooldown(Button.ABILITY_2) == 0 else "", abilityIconString(getPlayersInSlot(1, Team.1).getCurrentHero(), Button.ABILITY_1) if getPlayersInSlot(1, Team.1).getAbilityCooldown(Button.ABILITY_1) == 0 else "")))), HudPosition.LEFT, 2, Color.WHITE, HudReeval.VISIBILITY_AND_STRING, SpecVisibility.ALWAYS)
        hudSubtext(null, "{0}   {1} - {2}".format(heroIcon(getPlayersInSlot(2, Team.1).getCurrentHero()), ceil(getPlayersInSlot(2, Team.1).getStatistic(Stat.BARRIER_DAMAGE_DEALT) + getPlayersInSlot(2, Team.1).getStatistic(Stat.HERO_DAMAGE_DEALT)), "{0} - {1} - {2}".format(ceil(getPlayersInSlot(2, Team.1).getStatistic(Stat.DAMAGE_TAKEN)), getPlayersInSlot(2, Team.1).getStatistic(Stat.FINAL_BLOWS), "{0} - {1} - {2}".format(getPlayersInSlot(2, Team.1).getStatistic(Stat.DEATHS), ceil(getPlayersInSlot(2, Team.1).getStatistic(Stat.HEALING_DEALT)), "{0}  {1} {2}".format(getPlayersInSlot(2, Team.1).getStatistic(Stat.ULTIMATES_USED), abilityIconString(getPlayersInSlot(2, Team.1).getCurrentHero(), Button.ABILITY_2) if getPlayersInSlot(2, Team.1).getAbilityCooldown(Button.ABILITY_2) == 0 else "", abilityIconString(getPlayersInSlot(2, Team.1).getCurrentHero(), Button.ABILITY_1) if getPlayersInSlot(2, Team.1).getAbilityCooldown(Button.ABILITY_1) == 0 else "")))), HudPosition.LEFT, 3, Color.WHITE, HudReeval.VISIBILITY_AND_STRING, SpecVisibility.ALWAYS)
        hudSubtext(null, "{0}   {1} - {2}".format(heroIcon(getPlayersInSlot(3, Team.1).getCurrentHero()), ceil(getPlayersInSlot(3, Team.1).getStatistic(Stat.BARRIER_DAMAGE_DEALT) + getPlayersInSlot(3, Team.1).getStatistic(Stat.HERO_DAMAGE_DEALT)), "{0} - {1} - {2}".format(ceil(getPlayersInSlot(3, Team.1).getStatistic(Stat.DAMAGE_TAKEN)), getPlayersInSlot(3, Team.1).getStatistic(Stat.FINAL_BLOWS), "{0} - {1} - {2}".format(getPlayersInSlot(3, Team.1).getStatistic(Stat.DEATHS), ceil(getPlayersInSlot(3, Team.1).getStatistic(Stat.HEALING_DEALT)), "{0}  {1} {2}".format(getPlayersInSlot(3, Team.1).getStatistic(Stat.ULTIMATES_USED), abilityIconString(getPlayersInSlot(3, Team.1).getCurrentHero(), Button.ABILITY_2) if getPlayersInSlot(3, Team.1).getAbilityCooldown(Button.ABILITY_2) == 0 else "", abilityIconString(getPlayersInSlot(3, Team.1).getCurrentHero(), Button.ABILITY_1) if getPlayersInSlot(3, Team.1).getAbilityCooldown(Button.ABILITY_1) == 0 else "")))), HudPosition.LEFT, 4, Color.WHITE, HudReeval.VISIBILITY_AND_STRING, SpecVisibility.ALWAYS)
        hudSubtext(null, "{0}   {1} - {2}".format(heroIcon(getPlayersInSlot(4, Team.1).getCurrentHero()), ceil(getPlayersInSlot(4, Team.1).getStatistic(Stat.BARRIER_DAMAGE_DEALT) + getPlayersInSlot(4, Team.1).getStatistic(Stat.HERO_DAMAGE_DEALT)), "{0} - {1} - {2}".format(ceil(getPlayersInSlot(4, Team.1).getStatistic(Stat.DAMAGE_TAKEN)), getPlayersInSlot(4, Team.1).getStatistic(Stat.FINAL_BLOWS), "{0} - {1} - {2}".format(getPlayersInSlot(4, Team.1).getStatistic(Stat.DEATHS), ceil(getPlayersInSlot(4, Team.1).getStatistic(Stat.HEALING_DEALT)), "{0}  {1} {2}".format(getPlayersInSlot(4, Team.1).getStatistic(Stat.ULTIMATES_USED), abilityIconString(getPlayersInSlot(4, Team.1).getCurrentHero(), Button.ABILITY_2) if getPlayersInSlot(4, Team.1).getAbilityCooldown(Button.ABILITY_2) == 0 else "", abilityIconString(getPlayersInSlot(4, Team.1).getCurrentHero(), Button.ABILITY_1) if getPlayersInSlot(4, Team.1).getAbilityCooldown(Button.ABILITY_1) == 0 else "")))), HudPosition.LEFT, 5, Color.WHITE, HudReeval.VISIBILITY_AND_STRING, SpecVisibility.ALWAYS)
        hudSubtext(null, "{0}   {1} - {2}".format(heroIcon(getPlayersInSlot(5, Team.1).getCurrentHero()), ceil(getPlayersInSlot(5, Team.1).getStatistic(Stat.BARRIER_DAMAGE_DEALT) + getPlayersInSlot(5, Team.1).getStatistic(Stat.HERO_DAMAGE_DEALT)), "{0} - {1} - {2}".format(ceil(getPlayersInSlot(5, Team.1).getStatistic(Stat.DAMAGE_TAKEN)), getPlayersInSlot(5, Team.1).getStatistic(Stat.FINAL_BLOWS), "{0} - {1} - {2}".format(getPlayersInSlot(5, Team.1).getStatistic(Stat.DEATHS), ceil(getPlayersInSlot(5, Team.1).getStatistic(Stat.HEALING_DEALT)), "{0}  {1} {2}".format(getPlayersInSlot(5, Team.1).getStatistic(Stat.ULTIMATES_USED), abilityIconString(getPlayersInSlot(5, Team.1).getCurrentHero(), Button.ABILITY_2) if getPlayersInSlot(5, Team.1).getAbilityCooldown(Button.ABILITY_2) == 0 else "", abilityIconString(getPlayersInSlot(5, Team.1).getCurrentHero(), Button.ABILITY_1) if getPlayersInSlot(5, Team.1).getAbilityCooldown(Button.ABILITY_1) == 0 else "")))), HudPosition.LEFT, 6, Color.WHITE, HudReeval.VISIBILITY_AND_STRING, SpecVisibility.ALWAYS)
        #team 2
        hudSubtext(null, "Dmg Dealt - Dmg Taken - Final Blows - Deaths - Heals Dealt - Ults Used", HudPosition.RIGHT, -6, Color.RED, HudReeval.VISIBILITY_AND_STRING, SpecVisibility.ALWAYS)
        hudSubtext(null, "{0}  {1} - {2}".format("{0} {1}".format(abilityIconString(getPlayersInSlot(0, Team.2).getCurrentHero(), Button.ABILITY_1) if getPlayersInSlot(0, Team.2).getAbilityCooldown(Button.ABILITY_1) == 0 else "", abilityIconString(getPlayersInSlot(0, Team.2).getCurrentHero(), Button.ABILITY_2) if getPlayersInSlot(0, Team.2).getAbilityCooldown(Button.ABILITY_2) == 0 else ""), ceil(getPlayersInSlot(0, Team.2).getStatistic(Stat.BARRIER_DAMAGE_DEALT) + getPlayersInSlot(0, Team.2).getStatistic(Stat.HERO_DAMAGE_DEALT)), "{0} - {1} - {2}".format(ceil(getPlayersInSlot(0, Team.2).getStatistic(Stat.DAMAGE_TAKEN)), getPlayersInSlot(0, Team.2).getStatistic(Stat.FINAL_BLOWS), "{0} - {1} - {2}".format(getPlayersInSlot(0, Team.2).getStatistic(Stat.DEATHS), ceil(getPlayersInSlot(0, Team.2).getStatistic(Stat.HEALING_DEALT)), "{0}   {1}".format(getPlayersInSlot(0, Team.2).getStatistic(Stat.ULTIMATES_USED), heroIcon(getPlayersInSlot(0, Team.2).getCurrentHero()))))), HudPosition.RIGHT, -5, Color.WHITE, HudReeval.VISIBILITY_AND_STRING, SpecVisibility.ALWAYS)
        hudSubtext(null, "{0}  {1} - {2}".format("{0} {1}".format(abilityIconString(getPlayersInSlot(1, Team.2).getCurrentHero(), Button.ABILITY_1) if getPlayersInSlot(1, Team.2).getAbilityCooldown(Button.ABILITY_1) == 0 else "", abilityIconString(getPlayersInSlot(1, Team.2).getCurrentHero(), Button.ABILITY_2) if getPlayersInSlot(1, Team.2).getAbilityCooldown(Button.ABILITY_2) == 0 else ""), ceil(getPlayersInSlot(1, Team.2).getStatistic(Stat.BARRIER_DAMAGE_DEALT) + getPlayersInSlot(1, Team.2).getStatistic(Stat.HERO_DAMAGE_DEALT)), "{0} - {1} - {2}".format(ceil(getPlayersInSlot(1, Team.2).getStatistic(Stat.DAMAGE_TAKEN)), getPlayersInSlot(1, Team.2).getStatistic(Stat.FINAL_BLOWS), "{0} - {1} - {2}".format(getPlayersInSlot(1, Team.2).getStatistic(Stat.DEATHS), ceil(getPlayersInSlot(1, Team.2).getStatistic(Stat.HEALING_DEALT)), "{0}   {1}".format(getPlayersInSlot(1, Team.2).getStatistic(Stat.ULTIMATES_USED), heroIcon(getPlayersInSlot(1, Team.2).getCurrentHero()))))), HudPosition.RIGHT, -4, Color.WHITE, HudReeval.VISIBILITY_AND_STRING, SpecVisibility.ALWAYS)
        hudSubtext(null, "{0}  {1} - {2}".format("{0} {1}".format(abilityIconString(getPlayersInSlot(2, Team.2).getCurrentHero(), Button.ABILITY_1) if getPlayersInSlot(2, Team.2).getAbilityCooldown(Button.ABILITY_1) == 0 else "", abilityIconString(getPlayersInSlot(2, Team.2).getCurrentHero(), Button.ABILITY_2) if getPlayersInSlot(2, Team.2).getAbilityCooldown(Button.ABILITY_2) == 0 else ""), ceil(getPlayersInSlot(2, Team.2).getStatistic(Stat.BARRIER_DAMAGE_DEALT) + getPlayersInSlot(2, Team.2).getStatistic(Stat.HERO_DAMAGE_DEALT)), "{0} - {1} - {2}".format(ceil(getPlayersInSlot(2, Team.2).getStatistic(Stat.DAMAGE_TAKEN)), getPlayersInSlot(2, Team.2).getStatistic(Stat.FINAL_BLOWS), "{0} - {1} - {2}".format(getPlayersInSlot(2, Team.2).getStatistic(Stat.DEATHS), ceil(getPlayersInSlot(2, Team.2).getStatistic(Stat.HEALING_DEALT)), "{0}   {1}".format(getPlayersInSlot(2, Team.2).getStatistic(Stat.ULTIMATES_USED), heroIcon(getPlayersInSlot(2, Team.2).getCurrentHero()))))), HudPosition.RIGHT, -3, Color.WHITE, HudReeval.VISIBILITY_AND_STRING, SpecVisibility.ALWAYS)
        hudSubtext(null, "{0}  {1} - {2}".format("{0} {1}".format(abilityIconString(getPlayersInSlot(3, Team.2).getCurrentHero(), Button.ABILITY_1) if getPlayersInSlot(3, Team.2).getAbilityCooldown(Button.ABILITY_1) == 0 else "", abilityIconString(getPlayersInSlot(3, Team.2).getCurrentHero(), Button.ABILITY_2) if getPlayersInSlot(3, Team.2).getAbilityCooldown(Button.ABILITY_2) == 0 else ""), ceil(getPlayersInSlot(3, Team.2).getStatistic(Stat.BARRIER_DAMAGE_DEALT) + getPlayersInSlot(3, Team.2).getStatistic(Stat.HERO_DAMAGE_DEALT)), "{0} - {1} - {2}".format(ceil(getPlayersInSlot(3, Team.2).getStatistic(Stat.DAMAGE_TAKEN)), getPlayersInSlot(3, Team.2).getStatistic(Stat.FINAL_BLOWS), "{0} - {1} - {2}".format(getPlayersInSlot(3, Team.2).getStatistic(Stat.DEATHS), ceil(getPlayersInSlot(3, Team.2).getStatistic(Stat.HEALING_DEALT)), "{0}   {1}".format(getPlayersInSlot(3, Team.2).getStatistic(Stat.ULTIMATES_USED), heroIcon(getPlayersInSlot(3, Team.2).getCurrentHero()))))), HudPosition.RIGHT, -2, Color.WHITE, HudReeval.VISIBILITY_AND_STRING, SpecVisibility.ALWAYS)
        hudSubtext(null, "{0}  {1} - {2}".format("{0} {1}".format(abilityIconString(getPlayersInSlot(4, Team.2).getCurrentHero(), Button.ABILITY_1) if getPlayersInSlot(4, Team.2).getAbilityCooldown(Button.ABILITY_1) == 0 else "", abilityIconString(getPlayersInSlot(4, Team.2).getCurrentHero(), Button.ABILITY_2) if getPlayersInSlot(4, Team.2).getAbilityCooldown(Button.ABILITY_2) == 0 else ""), ceil(getPlayersInSlot(4, Team.2).getStatistic(Stat.BARRIER_DAMAGE_DEALT) + getPlayersInSlot(4, Team.2).getStatistic(Stat.HERO_DAMAGE_DEALT)), "{0} - {1} - {2}".format(ceil(getPlayersInSlot(4, Team.2).getStatistic(Stat.DAMAGE_TAKEN)), getPlayersInSlot(4, Team.2).getStatistic(Stat.FINAL_BLOWS), "{0} - {1} - {2}".format(getPlayersInSlot(4, Team.2).getStatistic(Stat.DEATHS), ceil(getPlayersInSlot(4, Team.2).getStatistic(Stat.HEALING_DEALT)), "{0}   {1}".format(getPlayersInSlot(4, Team.2).getStatistic(Stat.ULTIMATES_USED), heroIcon(getPlayersInSlot(4, Team.2).getCurrentHero()))))), HudPosition.RIGHT, -1, Color.WHITE, HudReeval.VISIBILITY_AND_STRING, SpecVisibility.ALWAYS)
        hudSubtext(null, "{0}  {1} - {2}".format("{0} {1}".format(abilityIconString(getPlayersInSlot(5, Team.2).getCurrentHero(), Button.ABILITY_1) if getPlayersInSlot(5, Team.2).getAbilityCooldown(Button.ABILITY_1) == 0 else "", abilityIconString(getPlayersInSlot(5, Team.2).getCurrentHero(), Button.ABILITY_2) if getPlayersInSlot(5, Team.2).getAbilityCooldown(Button.ABILITY_2) == 0 else ""), ceil(getPlayersInSlot(5, Team.2).getStatistic(Stat.BARRIER_DAMAGE_DEALT) + getPlayersInSlot(5, Team.2).getStatistic(Stat.HERO_DAMAGE_DEALT)), "{0} - {1} - {2}".format(ceil(getPlayersInSlot(5, Team.2).getStatistic(Stat.DAMAGE_TAKEN)), getPlayersInSlot(5, Team.2).getStatistic(Stat.FINAL_BLOWS), "{0} - {1} - {2}".format(getPlayersInSlot(5, Team.2).getStatistic(Stat.DEATHS), ceil(getPlayersInSlot(5, Team.2).getStatistic(Stat.HEALING_DEALT)), "{0}   {1}".format(getPlayersInSlot(5, Team.2).getStatistic(Stat.ULTIMATES_USED), heroIcon(getPlayersInSlot(5, Team.2).getCurrentHero()))))), HudPosition.RIGHT, 0, Color.WHITE, HudReeval.VISIBILITY_AND_STRING, SpecVisibility.ALWAYS)


rule "Both Teams Ready: Match starts in 5 sec, Remove HUD, Reset variables":
    @Condition isGameInProgress() == false
    @Condition getMatchTime() > 5
    @Condition Team1Ready == "Ready"
    @Condition Team2Ready == "Ready"
    
    setMatchTime(5)
    wait(1)


rule "Ultimate: +Ns match time while in setup":
    @Event eachPlayer
    @Condition isGameInProgress() == false
    @Condition getMatchTime() >= 1
    @Condition eventPlayer.getCurrentHero() == true
    @Condition eventPlayer.isHoldingButton(Button.ULTIMATE) == true
    @Condition eventPlayer.isHoldingButton(Button.INTERACT) == false
    @Condition eventPlayer.AddTimeCD == 0
    
    eventPlayer.AddTimeCD = 1
    chase(eventPlayer.AddTimeCD, 0, duration=1, ChaseReeval.DESTINATION_AND_DURATION)
    setMatchTime(getMatchTime() + MatchDelayAmount)
    smallMessage(getAllPlayers(), l"{0} {1}".format(eventPlayer, "added {0} seconds".format(MatchDelayAmount)))
    if eventPlayer.getTeam() == Team.1:
        Team1Ready = "Not Ready"
    else:
        Team2Ready = "Not Ready"


rule "Crouch + Interact: Ready/Unready":
    @Event eachPlayer
    @Condition isGameInProgress() == false
    @Condition eventPlayer.getCurrentHero() == true
    @Condition eventPlayer.isHoldingButton(Button.CROUCH) == true
    @Condition eventPlayer.isHoldingButton(Button.INTERACT) == true
    @Condition eventPlayer.ReadyCD == 0
    
    eventPlayer.ReadyCD = 1
    chase(eventPlayer.ReadyCD, 0, duration=1, ChaseReeval.DESTINATION_AND_DURATION)
    if eventPlayer.getTeam() == Team.1:
        if Team1Ready == "Not Ready":
            Team1Ready = "Ready"
            smallMessage(getAllPlayers(), l"{0} {1}".format(eventPlayer, "readied their team"))
        else:
            Team1Ready = "Not Ready"
            smallMessage(getAllPlayers(), l"{0} {1}".format(eventPlayer, "unreadied their team"))
    elif eventPlayer.getTeam() == Team.2:
        if Team2Ready == "Not Ready":
            Team2Ready = "Ready"
            smallMessage(getAllPlayers(), l"{0} {1}".format(eventPlayer, "readied their team"))
        else:
            Team2Ready = "Not Ready"
            smallMessage(getAllPlayers(), l"{0} {1}".format(eventPlayer, "unreadied their team"))


rule "First attack done":
    @Condition isMatchBetweenRounds() == true
    @Condition isTeamOnOffense(Team.2) == true
    @Condition ScoreModified == 0
    
    wait(15)
    FirstRoundDone = true


rule "Set Team Scores":
    @Condition ScoreModified == 0
    @Condition FirstRoundDone == true
    @Condition TournamentMode == false
    
    ScoreModified = 1
    if GameMode == 1:
        setTeamScore(Team.2, 3)
    elif GameMode == 2:
        setTeamScore(Team.2, 2)


rule "Set Game Mode":
    @Condition GameMode == 0
    
    if getCurrentGamemode() == Gamemode.ESCORT or getCurrentGamemode() == Gamemode.HYBRID:
        GameMode = 1
    elif getCurrentGamemode() == Gamemode.ASSAULT:
        GameMode = 2
    elif getCurrentGamemode() == Gamemode.CONTROL:
        GameMode = 3


rule "Defense Map Change Hero":
    @Event eachPlayer
    @Condition isInSetup() == true
    @Condition eventPlayer.isHoldingButton(Button.RELOAD) == true
    @Condition isTeamOnDefense(eventPlayer.getTeam()) == true
    @Condition eventPlayer.hasSpawned() == true
    @Condition eventPlayer.isAlive() == true
    @Condition eventPlayer.getCurrentHero() == true
    @Condition getMatchTime() >= 1
    
    wait(0.2, Wait.ABORT_WHEN_FALSE)
    smallMessage(eventPlayer, "keep holding reload to change hero")
    wait(0.7, Wait.ABORT_WHEN_FALSE)
    eventPlayer.HeroList = getAllHeroes()
    eventPlayer.HeroList.remove(eventPlayer.getCurrentHero())
    eventPlayer.setAllowedHeroes(eventPlayer.HeroList)
    wait(0.1)
    eventPlayer.setAllowedHeroes(getAllHeroes())


rule "Defense Map Teleport":
    @Event eachPlayer
    @Condition isInSetup() == true
    @Condition eventPlayer.isHoldingButton(Button.MELEE) == true
    @Condition isTeamOnDefense(eventPlayer.getTeam()) == true
    @Condition eventPlayer.isInSpawnRoom() == true
    @Condition eventPlayer.hasSpawned() == true
    @Condition eventPlayer.isAlive() == true
    @Condition eventPlayer.getCurrentHero() == true
    
    if getCurrentMap() == Map.BLIZZ_WORLD:
        eventPlayer.teleport(vect(-8.171, 3.824, 65.861))
    elif getCurrentMap() == Map.EICHENWALDE:
        eventPlayer.teleport(vect(13.226, 12.981, -83.655))
    elif getCurrentMap() == Map.HOLLYWOOD:
        eventPlayer.teleport(vect(-19.248, 8.007, -9.802))
    elif getCurrentMap() == Map.KINGS_ROW:
        eventPlayer.teleport(vect(-37.185, 10.346, -15.058))
    elif getCurrentMap() == Map.NUMBANI:
        eventPlayer.teleport(vect(93.044, 5.53, -22.723))
    elif getCurrentMap() == Map.HANAMURA:
        eventPlayer.teleport(vect(13.079, 1.346, -24.267))
    elif getCurrentMap() == Map.HORIZON_LUNAR_COLONY:
        eventPlayer.teleport(vect(42.356, 15.84, -79.798))
    elif getCurrentMap() == Map.PARIS:
        eventPlayer.teleport(vect(-40.379, 16.5, -14.259))
    elif getCurrentMap() == Map.TEMPLE_OF_ANUBIS:
        eventPlayer.teleport(vect(-23.909, 3.312, 46.94))
    elif getCurrentMap() == Map.VOLSKAYA:
        eventPlayer.teleport(vect(-35.545, -1.433, 73.561))
    elif getCurrentMap() == Map.DORADO:
        eventPlayer.teleport(vect(57.088, 9.241, -16.884))
    elif getCurrentMap() == Map.HAVANA:
        eventPlayer.teleport(vect(-18.059, 9.184, -70.117))
    elif getCurrentMap() == Map.JUNKERTOWN:
        eventPlayer.teleport(vect(-28.382, 14.223, -68.289))
    elif getCurrentMap() == Map.RIALTO:
        eventPlayer.teleport(vect(55.603, 2.452, -44.947))
    elif getCurrentMap() == Map.ROUTE66:
        eventPlayer.teleport(vect(33.662, 10.325, -5.514))
    elif getCurrentMap() == Map.WATCHPOINT_GIBRALTAR:
        eventPlayer.teleport(vect(32.488, 4.692, -71.941))


rule "DC Value Tracking - Team 1":
    @Event eachPlayer
    @Team 1
    @Condition isGameInProgress() == true
    @Condition eventPlayer.hasSpawned() == true
    @Condition AllowDCResume == true
    
    wait(1)
    PlayerDCInfoTeam1()
    if RULE_CONDITION:
        goto RULE_START


def PlayerDCInfoTeam1():
    @Name "DC Value Tracking - Team 1 Subroutine"
    
    if eventPlayer.hasSpawned():
        if ShouldRestore[0 + eventPlayer.getSlot()] >= 0:
            if eventPlayer.isAlive():
                UltCharges[0 + eventPlayer.getSlot()] = eventPlayer.getUltCharge()
                Heroes[0 + eventPlayer.getSlot()] = eventPlayer.getCurrentHero()
                Positions[0 + eventPlayer.getSlot()] = eventPlayer.getPosition()
                Cooldowns1[0 + eventPlayer.getSlot()] = eventPlayer.getAbilityCooldown(Button.ABILITY_1)
                Cooldowns2[0 + eventPlayer.getSlot()] = eventPlayer.getAbilityCooldown(Button.ABILITY_2)
                DVaRestore[0 + eventPlayer.getSlot()] = (eventPlayer.getUltCharge() if eventPlayer.getMaxHealth() > 200 else DVaRestore[0 + eventPlayer.getSlot()]) if eventPlayer.getCurrentHero() == Hero.DVA else -1
                ShouldRestore[0 + eventPlayer.getSlot()] = eventPlayer.getNormalizedHealth()
            else:
                ShouldRestore[0 + eventPlayer.getSlot()] = 0


rule "DC Value Tracking - Team 2":
    @Event eachPlayer
    @Team 2
    @Condition isGameInProgress() == true
    @Condition eventPlayer.hasSpawned() == true
    @Condition AllowDCResume == true
    
    wait(1)
    PlayerDCInfoTeam2()
    if RULE_CONDITION:
        goto RULE_START


def PlayerDCInfoTeam2():
    @Name "DC Value Tracking - Team 2 Subroutine"
    
    if eventPlayer.hasSpawned():
        if ShouldRestore[6 + eventPlayer.getSlot()] >= 0:
            if eventPlayer.isAlive():
                UltCharges[6 + eventPlayer.getSlot()] = eventPlayer.getUltCharge()
                Heroes[6 + eventPlayer.getSlot()] = eventPlayer.getCurrentHero()
                Positions[6 + eventPlayer.getSlot()] = eventPlayer.getPosition()
                Cooldowns1[6 + eventPlayer.getSlot()] = eventPlayer.getAbilityCooldown(Button.ABILITY_1)
                Cooldowns2[6 + eventPlayer.getSlot()] = eventPlayer.getAbilityCooldown(Button.ABILITY_2)
                DVaRestore[6 + eventPlayer.getSlot()] = eventPlayer.getMaxHealth()
                DVaRestore[6 + eventPlayer.getSlot()] = (eventPlayer.getUltCharge() if eventPlayer.getMaxHealth() > 200 else DVaRestore[6 + eventPlayer.getSlot()]) if eventPlayer.getCurrentHero() == Hero.DVA else -1
                ShouldRestore[6 + eventPlayer.getSlot()] = eventPlayer.getNormalizedHealth()
            else:
                ShouldRestore[6 + eventPlayer.getSlot()] = 0


rule "Player Reconnected - Team 1":
    @Event playerJoined
    @Team 1
    @Condition isGameInProgress() == true
    @Condition AllowDCResume == true
    
    waitUntil(eventPlayer.hasSpawned(), 10)
    wait(0.1)
    if eventPlayer.getCurrentHero() == Heroes[0 + eventPlayer.getSlot()]:
        eventPlayer.setUltCharge(UltCharges[0 + eventPlayer.getSlot()])
        if ShouldRestore[0 + eventPlayer.getSlot()] > 0:
            ShouldRestore[0 + eventPlayer.getSlot()] = 0 - (ShouldRestore[0 + eventPlayer.getSlot()])
            eventPlayer.startForcingPosition(Positions[0 + eventPlayer.getSlot()], false)
            wait(0.1)
            eventPlayer.stopForcingPosition()
            PlayerDCDvaTeam1()
            eventPlayer.setHealth((0 - (ShouldRestore[0 + eventPlayer.getSlot()])) * eventPlayer.getMaxHealth())
            eventPlayer.setAbilityCooldown(Button.ABILITY_1, Cooldowns1[0 + eventPlayer.getSlot()])
            eventPlayer.setAbilityCooldown(Button.ABILITY_2, Cooldowns2[0 + eventPlayer.getSlot()])
            ShouldRestore[0 + eventPlayer.getSlot()] = 0 - (ShouldRestore[0 + eventPlayer.getSlot()])


rule "Player Reconnected - Team 2":
    @Event playerJoined
    @Team 2
    @Condition isGameInProgress() == true
    @Condition AllowDCResume == true
    
    waitUntil(eventPlayer.hasSpawned(), 10)
    wait(0.1)
    if eventPlayer.getCurrentHero() == Heroes[6 + eventPlayer.getSlot()]:
        eventPlayer.setUltCharge(UltCharges[6 + eventPlayer.getSlot()])
        if ShouldRestore[6 + eventPlayer.getSlot()] > 0:
            ShouldRestore[6 + eventPlayer.getSlot()] = 0 - (ShouldRestore[6 + eventPlayer.getSlot()])
            eventPlayer.startForcingPosition(Positions[6 + eventPlayer.getSlot()], false)
            wait(0.1)
            eventPlayer.stopForcingPosition()
            PlayerDCDvaTeam2()
            eventPlayer.setHealth((0 - (ShouldRestore[6 + eventPlayer.getSlot()])) * eventPlayer.getMaxHealth())
            eventPlayer.setAbilityCooldown(Button.ABILITY_1, Cooldowns1[6 + eventPlayer.getSlot()])
            eventPlayer.setAbilityCooldown(Button.ABILITY_2, Cooldowns2[6 + eventPlayer.getSlot()])
            ShouldRestore[6 + eventPlayer.getSlot()] = 0 - (ShouldRestore[6 + eventPlayer.getSlot()])


def PlayerDCDvaTeam1():
    @Name "Player Reconnected - Team 1 DVa"
    
    if eventPlayer.getCurrentHero() == Hero.DVA:
        if DVaRestore[0 + eventPlayer.getSlot()] >= 0:
            eventPlayer.setUltCharge(DVaRestore[0 + eventPlayer.getSlot()])
            wait(0.1)
            damage(eventPlayer, null, 1000)
            wait(1.6)
            eventPlayer.setUltCharge(UltCharges[0 + eventPlayer.getSlot()])


def PlayerDCDvaTeam2():
    @Name "Player Reconnected - Team 2 DVa"
    
    if eventPlayer.getCurrentHero() == Hero.DVA:
        if DVaRestore[6 + eventPlayer.getSlot()] >= 0:
            eventPlayer.setUltCharge(DVaRestore[6 + eventPlayer.getSlot()])
            wait(0.1)
            damage(eventPlayer, null, 1000)
            wait(1.6)
            eventPlayer.setUltCharge(UltCharges[6 + eventPlayer.getSlot()])


rule "Reset Map Info":
    @Condition isGameInProgress() == false
    @Condition MapInfoLogged == true
    
    MapInfoLogged = false


rule "Log Map Info":
    @Condition isGameInProgress() == true
    @Condition MapInfoLogged == false
    
    MapInfoLogged = true
    printLog("{0},{1},{2}".format(getCurrentMap(), getPlayersInSlot(0, Team.1).getTeam(), "{0},{1}".format(getPlayersInSlot(0, Team.2).getTeam(), getCurrentObjective())))
    printLog("{0},{1},{2}".format("{0},{1},{2}".format(getPlayersInSlot(0, Team.1), getPlayersInSlot(1, Team.1), getPlayersInSlot(2, Team.1)), "{0},{1},{2}".format("{0},{1},{2}".format(getPlayersInSlot(3, Team.1), getPlayersInSlot(4, Team.1), getPlayersInSlot(5, Team.1)), getPlayersInSlot(0, Team.2), getPlayersInSlot(1, Team.2)), "{0},{1}".format("{0},{1},{2}".format(getPlayersInSlot(2, Team.2), getPlayersInSlot(3, Team.2), getPlayersInSlot(4, Team.2)), getPlayersInSlot(5, Team.2))))


rule "Global Logging - Ongoing":
    @Condition isGameInProgress() == true
    @Condition MapInfoLogged == true
    @Condition isMatchBetweenRounds() == false
    
    wait(1)
    LogMapGamemodeInfo()
    if RULE_CONDITION:
        goto RULE_START


def LogMapGamemodeInfo():
    @Name "Global Logging - Subroutine"
    
    if getCurrentGamemode() == Gamemode.CONTROL:
        #time, team 1 percentage, team 2 percentage
        printLog("{0},{1},{2}".format(getTotalTimeElapsed(), getControlScorePercentage(Team.1), getControlScorePercentage(Team.2)))
    elif getCurrentGamemode() == Gamemode.ESCORT:
        #time, team 1 attacking (else is team 2), payload progress percentage
        printLog("{0},{1},{2}".format(getTotalTimeElapsed(), isTeamOnOffense(Team.1), getPayloadProgressPercentage()))
    elif getCurrentGamemode() == Gamemode.ASSAULT:
        #time, team 1 attacking (else is team 2), point capture percentage
        printLog("{0},{1},{2}".format(getTotalTimeElapsed(), isTeamOnOffense(Team.1), getCapturePercentage()))
    elif getCurrentGamemode() == Gamemode.HYBRID:
        if isTeamOnOffense(Team.1) == true:
            LogHybridInfo()
        else:
            if teamScore(Team.2) >= 1:
                #time, team 1 attacking (else is team 2), payload progress percentage
                printLog("{0},{1},{2}".format(getTotalTimeElapsed(), isTeamOnOffense(Team.1), getPayloadProgressPercentage()))
            else:
                #time, team 1 attacking (else is team 2), point capture percentage
                printLog("{0},{1},{2}".format(getTotalTimeElapsed(), isTeamOnOffense(Team.1), getCapturePercentage()))


def LogHybridInfo():
    @Name "Global Logging - Subroutine 2"
    
    if teamScore(Team.1) >= 1:
        #time, team 1 attacking (else is team 2), payload progress percentage
        printLog("{0},{1},{2}".format(getTotalTimeElapsed(), isTeamOnOffense(Team.1), getPayloadProgressPercentage()))
    else:
        #time, team 1 attacking (else is team 2), point capture percentage
        printLog("{0},{1},{2}".format(getTotalTimeElapsed(), isTeamOnOffense(Team.1), getCapturePercentage()))


rule "Player Logging - Ongoing":
    @Event eachPlayer
    @Condition isGameInProgress() == true
    @Condition MapInfoLogged == true
    @Condition isMatchBetweenRounds() == false
    
    printLog("{0},{1},{2}".format(getTotalTimeElapsed(), eventPlayer, "{0},{1},{2}".format(eventPlayer.getCurrentHero(), eventPlayer.getStatistic(Stat.HERO_DAMAGE_DEALT), "{0},{1},{2}".format(eventPlayer.getStatistic(Stat.BARRIER_DAMAGE_DEALT), eventPlayer.getStatistic(Stat.DAMAGE_BLOCKED), "{0},{1},{2}".format(eventPlayer.getStatistic(Stat.DAMAGE_TAKEN), eventPlayer.getStatistic(Stat.DEATHS), "{0},{1},{2}".format(eventPlayer.getStatistic(Stat.ELIMINATIONS), eventPlayer.getStatistic(Stat.FINAL_BLOWS), "{0},{1},{2}".format(eventPlayer.getStatistic(Stat.ENVIRONMENTAL_DEATHS), eventPlayer.getStatistic(Stat.ENVIRONMENTAL_KILLS), "{0},{1},{2}".format(eventPlayer.getStatistic(Stat.HEALING_DEALT), eventPlayer.getStatistic(Stat.OBJECTIVE_KILLS), "{0},{1},{2}".format(eventPlayer.getStatistic(Stat.SOLO_KILLS), eventPlayer.getStatistic(Stat.ULTIMATES_EARNED), "{0},{1},{2}".format(eventPlayer.getStatistic(Stat.ULTIMATES_USED), eventPlayer.getHeroStatistic(getAllHeroes(), HeroStat.HEALING_RECEIVED), "{0},{1},{2}".format(eventPlayer.getUltCharge(), eventPlayer.getPlayerClosestToReticle(Team.ALL), "{0},{1},{2}".format(eventPlayer.getPosition(), eventPlayer.getTeam(), "{0},{1},{2}".format(eventPlayer.getAbilityCooldown(Button.ABILITY_1), eventPlayer.getAbilityCooldown(Button.ABILITY_2), eventPlayer.getMaxHealth())))))))))))))
    wait(1)
    #(do at end)
    if isGameInProgress():
        goto RULE_START


rule "Log Event - FB":
    @Event playerDealtFinalBlow
    @Condition isGameInProgress() == true
    
    printLog("{0},FinalBlow,{1},{2}".format(getTotalTimeElapsed(), eventPlayer, "{0},{1}".format(victim, eventAbility)))


rule "Log Event - PD":
    @Event playerDied
    @Condition isGameInProgress() == true
    @Condition (eventWasEnvironment or attacker == eventPlayer) == true
    
    printLog("{0},Suicide,{1}".format(getTotalTimeElapsed(), eventPlayer))


rule "Log Event - Resurrect":
    @Event eachPlayer
    @Condition isGameInProgress() == true
    @Condition eventPlayer.hasStatusEffect(Status.PHASED_OUT) == true
    @Condition eventPlayer.isInSpawnRoom() == false
    @Condition teamHasHero(Hero.MERCY, eventPlayer.getTeam()) == true
    @Condition getPlayersOnHero(Hero.MERCY, eventPlayer.getTeam())[0].getAbilityCooldown(Button.ABILITY_2) >= 5
    
    printLog("{0},Resurrected,{1}".format(getTotalTimeElapsed(), eventPlayer))


rule "Log Event - Echo Duplicate Start":
    @Event eachPlayer
    @Condition isGameInProgress() == true
    @Condition eventPlayer.getCurrentHero() == Hero.ECHO
    @Condition eventPlayer.isDuplicatingAHero() == true
    @Condition eventPlayer.IsUlting == false
    
    printLog("{0},DuplicatingStart,{1},{2}".format(getTotalTimeElapsed(), eventPlayer, eventPlayer.getHeroOfDuplication()))
    eventPlayer.IsUlting = true


rule "Log Event - Echo Duplicate End":
    @Event eachPlayer
    @Condition isGameInProgress() == true
    @Condition eventPlayer.getCurrentHero() == Hero.ECHO
    @Condition eventPlayer.isDuplicatingAHero() == false
    @Condition eventPlayer.IsUlting == true
    
    printLog("{0},DuplicatingEnd,{1}".format(getTotalTimeElapsed(), eventPlayer))
    eventPlayer.IsUlting = false


