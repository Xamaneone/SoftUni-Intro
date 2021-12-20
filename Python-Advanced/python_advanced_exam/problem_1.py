from collections import deque

def equal_or_below_zero(firework, explosion, firework_effects, exploding_powers):
    restart = False
    if firework <= 0:
        restart = True
        if explosion <= 0:
            return restart
        exploding_powers.append(explosion)
    elif explosion <= 0:
        restart = True
        firework_effects.appendleft(firework)
    return restart



def is_crossette(sum):
    if sum % 3 == 0 and sum % 5 == 0:
        return True
    return False

def is_palm(sum):
    if sum % 3 == 0 and sum % 5 != 0:
        return True
    return False

def is_willow(sum):
    if sum % 5 == 0 and sum % 3 != 0:
        return True
    return False

def job_is_done(crossetes, palms, willows):
    if crossetes >= 3 and palms >= 3 and willows >= 3:
        return True
    return False



firework_effects = deque(map(int, input().split(", ")))
exploding_powers = deque(map(int, input().split(", ")))


crossete_fireworks = 0
palm_fireworks = 0
willow_fireworks = 0


while firework_effects and exploding_powers:
    if job_is_done(crossete_fireworks, palm_fireworks, willow_fireworks):
        break
    firework = firework_effects.popleft()
    explosion = exploding_powers.pop()
    if equal_or_below_zero(firework, explosion, firework_effects, exploding_powers):
        continue
    sum_of_both = firework + explosion
    if is_crossette(sum_of_both):
        crossete_fireworks += 1
        continue
    if is_palm(sum_of_both):
        palm_fireworks += 1
        continue
    if is_willow(sum_of_both):
        willow_fireworks += 1
        continue
    firework -= 1
    firework_effects.append(firework)
    exploding_powers.append(explosion)

if job_is_done(crossete_fireworks, palm_fireworks, willow_fireworks):
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can’t make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
if exploding_powers:
    print(f"Explosive Power left: {', '.join(map(str, exploding_powers))}")
print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossete_fireworks}")

