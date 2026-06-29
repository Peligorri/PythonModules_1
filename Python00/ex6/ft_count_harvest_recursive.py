# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jangonza <jangonza@student.42urduliz.com>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/29 13:32:45 by jangonza          #+#    #+#              #
#    Updated: 2026/06/29 13:32:47 by jangonza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
def ft_recursive(count, days):
	print(f"Day {count}")
	count += 1
	if(int(count) <= int(days)):
		ft_recursive(count, days)
def ft_count_harvest_recursive():
	count = 1
	days = input("Days until harvest: ")
	ft_recursive(count, days)
	print("Harvest time!")
