import time
import random
import sys

class Spaceship:
    def __init__(self, name):
        self.name = name
        self.crew = []
        self.resources = {
            'fuel': 100,
            'food': 100,
            'energy': 100,
            'repair_parts': 50
        }
        self.missions_completed = 0
        self.current_sector = None
        self.discovered_technologies = []

class CrewMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.skills = {
            'engineering': random.randint(1, 10),
            'navigation': random.randint(1, 10),
            'combat': random.randint(1, 10),
            'diplomacy': random.randint(1, 10)
        }
        self.health = 100
        self.morale = 80

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def validate_input(prompt, valid_options):
    while True:
        response = input(prompt).lower().strip()
        if response in valid_options:
            return response
        slow_print("Invalid option. Recalibrating systems...")

def generate_star_system():
    system_types = [
        'Habitable', 'Volcanic', 'Ice', 'Gas Giant', 
        'Binary Star', 'Neutron Star', 'Asteroid Belt'
    ]
    threat_levels = ['Low', 'Medium', 'High', 'Critical']
    resource_types = ['Rare Minerals', 'Energy Crystals', 'Alien Artifacts', 'Antimatter']
    
    return {
        'name': f'Sector-{random.randint(100, 999)}',
        'type': random.choice(system_types),
        'threat_level': random.choice(threat_levels),
        'primary_resource': random.choice(resource_types)
    }

def recruit_crew(spaceship):
    crew_roles = ['Navigator', 'Engineer', 'Scientist', 'Security', 'Diplomat']
    crew_count = random.randint(3, 6)
    
    slow_print(f"\n🚀 Recruiting {crew_count} crew members for {spaceship.name}")
    
    for _ in range(crew_count):
        name = f"Crew-{random.randint(100, 999)}"
        role = random.choice(crew_roles)
        crew_member = CrewMember(name, role)
        spaceship.crew.append(crew_member)
        slow_print(f"Recruited {name} as {role}")

def space_exploration_mission(spaceship):
    spaceship.current_sector = generate_star_system()
    slow_print(f"\n🌠 Entering {spaceship.current_sector['name']} - {spaceship.current_sector['type']} System")
    slow_print(f"Threat Level: {spaceship.current_sector['threat_level']}")
    slow_print(f"Primary Resource: {spaceship.current_sector['primary_resource']}")

    mission_choices = ['investigate', 'extract', 'avoid']
    mission = validate_input("Choose mission strategy: (investigate/extract/avoid): ", mission_choices)

    if mission == 'investigate':
        investigate_mission(spaceship)
    elif mission == 'extract':
        resource_extraction_mission(spaceship)
    else:
        avoid_mission(spaceship)

def investigate_mission(spaceship):
    investigation_outcomes = [
        'scientific_discovery', 'alien_encounter', 'system_malfunction', 'peaceful_exploration'
    ]
    outcome = random.choice(investigation_outcomes)

    if outcome == 'scientific_discovery':
        technology = random.choice(['Quantum Drive', 'Teleportation', 'Cloaking Technology'])
        spaceship.discovered_technologies.append(technology)
        slow_print(f"🔬 Breakthrough! Discovered {technology}")
        spaceship.missions_completed += 1

    elif outcome == 'alien_encounter':
        diplomacy_check = sum(crew.skills['diplomacy'] for crew in spaceship.crew) / len(spaceship.crew)
        if diplomacy_check > 6:
            slow_print("🤝 Successful diplomatic contact with alien civilization!")
            spaceship.resources['repair_parts'] += 30
        else:
            slow_print("⚠️ Tense alien encounter! Shields damaged.")
            spaceship.resources['repair_parts'] -= 20

    # Additional mission logic would follow similar patterns

def resource_extraction_mission(spaceship):
    pass  # Implement detailed resource extraction logic

def avoid_mission(spaceship):
    pass  # Implement consequences of avoiding a mission

def main_game_loop():
    slow_print("🌌 INTERSTELLAR ODYSSEY 🌌")
    ship_name = input("Name your spaceship: ")
    spaceship = Spaceship(ship_name)
    
    recruit_crew(spaceship)
    
    missions = 5
    while missions > 0:
        space_exploration_mission(spaceship)
        missions -= 1
    
    game_conclusion(spaceship)

def game_conclusion(spaceship):
    slow_print("\n🏆 MISSION REPORT 🏆")
    slow_print(f"Spaceship: {spaceship.name}")
    slow_print(f"Missions Completed: {spaceship.missions_completed}")
    slow_print(f"Discovered Technologies: {spaceship.discovered_technologies}")
    slow_print("Mission Status: " + ("Successful" if spaceship.missions_completed > 3 else "Incomplete"))

if __name__ == "__main__":
    main_game_loop()