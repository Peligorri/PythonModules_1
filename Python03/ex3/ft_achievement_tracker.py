
def main():
	achievements = set(["Crafting Genius", "World Savior", "Master explorer", "Collector Supreme", "Untouchable", "Boss Slayer", "Strategist", "Speed Runner", "Survivor", "Treasure Hunter", "Unstoppable", "Hidden Path Finder", "First Steps", "Sharp Mind"])
	player_alice = set(["Crafting Genius", "World Savior", "Master explorer", "Collector Supreme", "Untouchable", "Boss Slayer"])
	player_bob = set(["Crafting Genius", "Strategist", "World Savior", "Master explorer", "Unstoppable", "Collector Supreme", "Untouchable"])
	player_charlie = set(["Strategist", "Speed Runner", "Survivor", "Master explorer", "Treasure Hunter", "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind"])
	player_dylan = set(["Strategist", "Speed Runner", "Unstoppable", "Untouchable", "Boss Slayer"])

	print("=== Achievement Tracker System ===")
	print("")
	print(f"Player Alice: {player_alice}")
	print(f"Player Bob: {player_bob}")
	print(f"Player Charlie: {player_charlie}")
	print(f"Player Dylan: {player_dylan}")
	print("")
	print(f"All distinct achievements: {achievements}")
	print("")
	print(f"Common achievements: {player_bob & player_alice & player_dylan & player_charlie}")
	print("")
	print(f"Only Alice has: {player_alice - (player_bob | player_dylan | player_charlie)}")
	print(f"Only Bob has: {player_bob - (player_alice | player_dylan | player_charlie)}")
	print(f"Only Charlie has: {player_charlie - (player_bob | player_dylan | player_alice)}")
	print(f"Only Dylan has: {player_dylan - (player_bob | player_alice | player_charlie)}")
	print("")
	print(f"Alice is missing: {achievements - player_alice}")
	print(f"Bob is missing: {achievements - player_bob}")
	print(f"Charlie is missing: {achievements - player_charlie}")
	print(f"Dylan is missing: {achievements - player_dylan}")


if __name__ == "__main__":
    main()