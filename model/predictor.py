# model/predictor.py

def predict_character(traits: dict) -> dict:
    """
    Takes a trait dictionary and returns:
    - a character label: 'Cuckman' or 'Alphaman'
    - a probability score
    """

    score = 0
    max_score = 14  # Increased due to new cyber traits

    # 💺 Interior Design
    if traits.get("cuckchair_present"):
        score += 2  # huge cuck signal

    # 📱 Messaging & Surveillance
    if traits.get("uses_signal"):
        score += 1
    if traits.get("deletes_chats"):
        score += 1  # suspicious

    # 🧬 Fitness + PEDs
    lift_status = traits.get("lifting_status", "")
    if lift_status == "Yes, enhanced (trendies)":
        score -= 2
    elif lift_status == "I lift ideas in my head":
        score += 2
    elif lift_status == "Yes, natural":
        score -= 1

    if traits.get("dry_scoops"):
        score -= 1  # bonus alpha points for self-harm

    # 🪖 Tactical Role
    tactical = traits.get("tactical_role", "")
    if tactical == "Support simp":
        score += 2
    elif tactical == "Emotional sniper":
        score += 1
    elif tactical == "Frontline Giga Chad":
        score -= 2

    # 🌱 Self-awareness
    if traits.get("touched_grass") == "What is grass":
        score += 1

    # 🧠 Meme/Reddit bonus penalty
    subreddit = traits.get("subreddit", "")
    if subreddit == "r/DeadBedrooms":
        score += 2
    elif subreddit == "r/MaleLivingSpace":
        score += 1
    elif subreddit == "r/Powerlifting":
        score -= 1

    based = traits.get("based_usage", "")
    if based == "Only when watching Andrew Tate clips":
        score += 2
    elif based == "Sometimes":
        score += 1

    # 💻 CYBERSECURITY ZONE 🛡️
    if traits.get("ics_alignment") == "Essential national priority 🔐":
        score -= 2
    elif traits.get("ics_alignment") == "ICS? Like air conditioners? 🌀":
        score += 2

    if traits.get("malware_mood") in ["Stuxnet 😈", "Volt Typhoon ⚡🐉"]:
        score -= 1
    elif traits.get("malware_mood") == "None, malware is cringe 🚫":
        score += 1

    if traits.get("tool_belt") in ["Sysmon", "Splunk"]:
        score -= 1
    elif traits.get("tool_belt") in ["CyberChef", "IDK what those are"]:
        score += 1

    org_type = traits.get("org_type", "")
    if org_type == "Private Sector ‘Insane Cyber’ firm 💼💣":
        score -= 2
    elif org_type == "Just vibe on HackTheBox 🌐":
        score += 1
    
    # 🛏️ Cuck signals
    if traits.get("watches_from_closet"):
        score += 3

    if traits.get("denies_jealousy") == "Say you're totally fine with it":
        score += 2

    reddit = traits.get("cuck_reddit", "")
    if reddit in ["r/cuckold", "r/hotwife"]:
        score += 3
    elif reddit == "r/DeadBedrooms":
        score += 1

    # 🍖 LiverKing Alignment
    if traits.get("eats_raw_liver"):
        score -= 1  # slightly alpha, but questionable
    if traits.get("liverking_affiliation") == "Yes, I model my life after him":
        score += 2  # full cuck
    elif traits.get("liverking_affiliation") == "I think he's a psyop":
        score -= 1  # suspicious alpha tendency

    # 💉 Tren Behavior
    if traits.get("tren_usage"):
        score -= 2  # giga alpha risk
    if traits.get("tren_attitude") == "The only natty is the one you haven’t tested":
        score -= 1
    elif traits.get("tren_attitude") == "Tren is for cattle and influencers":
        score += 1

    if traits.get("has_gyno"):
        score += 1  # potential consequences of bad cycles = cuck tilt

    # Clamp score and map to probability
    final_score = max(-max_score, min(max_score, score))
    probability = 0.5 + (final_score / (2 * max_score))  # ~0.0 to 1.0

    label = "Cuckman" if final_score > 1 else "Alphaman"
    title = generate_archetype_title(traits, label)

    return {
        "label": label,
        "probability": round(probability, 2),
        "score": final_score,
        "max_score": max_score,
        "title": title
    }

def generate_archetype_title(traits: dict, label: str) -> str:
    if label == "Cuckman":
        if traits.get("cuckchair_present") and traits.get("uses_signal"):
            return "Signal-Based Softshell"
        elif traits.get("org_type") == "Just vibe on HackTheBox 🌐":
            return "Digital Doormat"
        elif traits.get("based_usage") == "Only when watching Andrew Tate clips":
            return "Tate-Adjacent Tragedy"
        else:
            return "Cuckchair Console Jockey"
    
    elif label == "Alphaman":
        if traits.get("ics_alignment") == "Essential national priority 🔐":
            if traits.get("tool_belt") == "Sysmon":
                return "ICS GigaChad"
            elif traits.get("tool_belt") == "Splunk":
                return "SIEM Slayer"
        if traits.get("malware_mood") == "Stuxnet 😈":
            return "Stuxnet Summoner"
        elif traits.get("malware_mood") == "Volt Typhoon ⚡🐉":
            return "Dragon Slayer"
        return "Command Line Apex Predator"

    return "Unlabeled Enigma"
