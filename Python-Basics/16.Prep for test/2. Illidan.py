warriors = int(input())
power_per_warrior = int(input())
boss_health = int(input())
warriors = warriors * power_per_warrior
if warriors >= boss_health:
    print(f"Illidan has been slain! You defeated him with {warriors - boss_health} points.")
elif boss_health > warriors:
    print(f"You are not prepared! You need {boss_health - warriors} more points.")