# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jangonza <jangonza@student.42urduliz.com>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/29 14:58:49 by jangonza          #+#    #+#              #
#    Updated: 2026/06/29 14:58:52 by jangonza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	if seed_type == "tomato":
		print(f"{seed_type.capitalize()} seeds: {quantity} {unit} available")
	elif seed_type == "carrot":
		print(f"{seed_type.capitalize()} seeds: {quantity} {unit} total")
	elif seed_type == "lettuce":
		print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters")
	else:
		print("Unknown unit type")
