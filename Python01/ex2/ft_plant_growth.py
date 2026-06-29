# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jangonza <jangonza@student.42urduliz.com>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/29 16:30:42 by jangonza          #+#    #+#              #
#    Updated: 2026/06/29 16:30:44 by jangonza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

plant1 = {
  "Name": "Rose",
  "Height": 25.0,
  "Age": 30
}
plant2 = {
  "Name": "Sunflower",
  "Height": 80,
  "Age": 45
}
plant3 = {
  "Name": "Cactus",
  "Height": 15,
  "Age": 120
}
def grow(plant):
	plant1['Height'] = round((float(plant1['Height']) + 0.8), 1)
def age(plant):
	plant1['Age'] = int(plant1['Age']) + 1
def show(plant):
	print(f"{plant['Name']}: {plant['Height']}cm, {plant['Age']} days old")
def main():
	print("=== Garden Plant Growth ===")
	show(plant1)
	initial_height = plant1['Height']
	for day in range(1, 8):
		print(f"=== Day {day} ===")
		grow(plant1)
		age(plant1)
		show(plant1)
		day = int(day) + 1
	final_height = round((float(plant1['Height']) - float(initial_height)), 1)
	print(f"Growth this week: {final_height}cm")
if __name__ == "__main__":
    main()
