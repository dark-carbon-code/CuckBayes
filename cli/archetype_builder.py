# cli/archetype_builder.py

def ask_yes_no(prompt):
    answer = input(f"{prompt} [y/N]: ").strip().lower()
    return answer == 'y'


def ask_choice(prompt, choices):
    print(f"\n{prompt}")
    for i, option in enumerate(choices, 1):
        print(f"  [{i}] {option}")
    while True:
        choice = input("Select an option: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(choices):
            return choices[int(choice) - 1]


def run_archetype_builder():
    print("\n🧬 Welcome to the CuckBayes Archetype Builder™")
    print("Answer honestly. Your digital dignity is already compromised.\n")

    traits = {}

    # Reddit & Meme Lore
    traits["subreddit"] = ask_choice("Which subreddit do you most identify with?", [
        "r/DeadBedrooms",
        "r/MaleLivingSpace",
        "r/Powerlifting",
        "r/SelfAwarewolves"
    ])

    traits["based_usage"] = ask_choice("How often do you use the word 'based' unironically?", [
        "Never", "Sometimes", "Only when watching Andrew Tate clips"
    ])

    # Interior Design
    traits["cuckchair_present"] = (
        ask_choice("What is the centerpiece of your living room?", [
            "OLED TV and GameCube",
            "Gaming chair + anime wall scroll",
            "A cuck chair (reserved, untouched)",
            "Ottoman squat rack"
        ]) == "A cuck chair (reserved, untouched)"
    )

    # Screen Time
    traits["uses_signal"] = (
        ask_choice("Which app sends you the most notifications?", [
            "Signal", "WhatsApp", "OnlyFans", "Discord mod pings"
        ]) == "Signal"
    )

    traits["deletes_chats"] = ask_yes_no("Do you regularly delete your chat history 'just in case'?")

    # Fitness & PEDs
    traits["lifting_status"] = ask_choice("Do you lift?", [
        "Yes, natural", "Yes, enhanced (trendies)", "I lift ideas in my head"
    ])

    traits["dry_scoops"] = (
        ask_choice("What’s your pre-workout ritual?", [
            "Screaming 'Let’s go!' at your reflection",
            "DM'ing your gym crush on Signal",
            "Dry scooping a suspicious white powder"
        ]) == "Dry scooping a suspicious white powder"
    )

    # Military Cosplay
    traits["camo_indoors"] = ask_yes_no("Have you ever worn camo indoors?")
    traits["tactical_role"] = ask_choice("Select your tactical role:", [
        "Support simp", "Emotional sniper", "Frontline Giga Chad"
    ])

    # Self-awareness
    traits["touched_grass"] = ask_choice("When was the last time you touched grass?", [
        "Today", "Last week", "What is grass"
    ])

    # 🔐 CYBERSECURITY ZONE 🔐
    traits["ics_alignment"] = ask_choice("How do you feel about industrial control systems (ICS) cybersecurity?", [
        "Essential national priority 🔐",
        "Cool, but I’m a cloud native ☁️",
        "ICS? Like air conditioners? 🌀"
    ])

    traits["malware_mood"] = ask_choice("Which malware makes you smile just hearing the name?", [
        "Stuxnet 😈",
        "Volt Typhoon ⚡🐉",
        "Mirai 🍜",
        "None, malware is cringe 🚫"
    ])

    traits["fav_adversary"] = ask_choice("Which adversary name do you brag about knowing?", [
        "APT28 (Fancy Bear) 🐻",
        "Sandworm 🪱",
        "Cobalt Spider 🕷️",
        "Charming Kitten 🐱",
        "I make up my own"
    ])

    traits["tool_belt"] = ask_choice("What’s in your cyber tool belt?", [
        "Sysmon", "Splunk", "Elastic", "Wireshark", "nmap", "CyberChef", "IDK what those are"
    ])

    traits["org_type"] = ask_choice("Where do you do your insane cyber?", [
        "National Lab 🧪",
        "Private Sector ‘Insane Cyber’ firm 💼💣",
        "Government 😎",
        "Freelance OpSec 🥷",
        "Just vibe on HackTheBox 🌐"
    ])

    # 🥩 Liver King Lore
    traits["eats_raw_liver"] = ask_yes_no(
        "Have you ever eaten raw liver 'for the ancestral gains'?"
    )

    traits["liverking_affiliation"] = ask_choice(
        "Which best describes your stance on Liver King?",
        [
            "He’s the Natty Messiah",
            "He lied, but I still pop desiccated organs",
            "He’s a roid clown in a loincloth",
            "I unironically bought Ancestral Supplements"
        ]
    )

    # 💉 Tren Universe
    traits["tren_usage"] = ask_choice(
        "Be honest. Have you ever used trenbolone (Tren)?",
        [
            "Yes, and I’d do it again",
            "No, but I research it daily",
            "I only microdose for vitality",
            "Absolutely not. I am natty king"
        ]
    )

    traits["tren_attitude"] = ask_choice(
        "What’s your take on guys who run Tren?",
        [
            "Legends of modern warfare",
            "Meme freaks with gyno",
            "Jealous I can't afford it",
            "They smell like ammonia and rage"
        ]
    )

    traits["has_gyno"] = ask_yes_no(
        "Do you occasionally check for gyno in the mirror?"
    )

    return traits
