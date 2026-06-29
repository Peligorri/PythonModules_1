# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jangonza <jangonza@student.42urduliz.com>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/29 13:32:27 by jangonza          #+#    #+#              #
#    Updated: 2026/06/29 13:32:29 by jangonza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
	count = 1
	days = input("Days until harvest: ")
	while int(count) <= int(days):
		print(f"Day {count}")
		count += 1
	print("Harvest time!")
