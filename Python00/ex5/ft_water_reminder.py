# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jangonza <jangonza@student.42urduliz.com>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/29 13:21:11 by jangonza          #+#    #+#              #
#    Updated: 2026/06/29 13:21:13 by jangonza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
	days = input("Days since last watering: ")
	if 2 < int(days):
		print("Water the plants!")
	else:
		print("Plants are fine")
