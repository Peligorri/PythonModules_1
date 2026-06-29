# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jangonza <jangonza@student.42urduliz.com>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/29 13:10:35 by jangonza          #+#    #+#              #
#    Updated: 2026/06/29 13:10:38 by jangonza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
def ft_harvest_total():
	day1 = input("Day 1 harvest: ")
	day2 = input("Day 2 harvest: ")
	day3 = input("Day 3 harvest: ")
	total_plot = int(day1) + int(day2) + int(day3)
	print(f"Total harvest: {total_plot}")

