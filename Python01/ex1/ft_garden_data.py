# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jangonza <jangonza@student.42urduliz.com>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/29 16:10:52 by jangonza          #+#    #+#              #
#    Updated: 2026/06/29 16:10:54 by jangonza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
plant1 = {
  "Name": "Rose",
  "Height": 25,
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
def show(plant):
	print(f"{plant['Name']}: {plant['Height']}cm, {plant['Age']} days old")
def main():
	print("=== Garden Plant Registry ===")
	show(plant1)
	show(plant2)
	show(plant3)
if __name__ == "__main__":
    main()
