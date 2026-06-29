# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jangonza <jangonza@student.42urduliz.com>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/29 13:16:15 by jangonza          #+#    #+#              #
#    Updated: 2026/06/29 13:16:17 by jangonza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
	days = input("Enter plant age in days: ")
	if 60 < int(days):
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow.")
		
