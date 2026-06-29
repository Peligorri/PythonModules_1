# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jangonza <jangonza@student.42urduliz.com>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/29 13:05:28 by jangonza          #+#    #+#              #
#    Updated: 2026/06/29 13:05:31 by jangonza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
def ft_plot_area():
	length = input("Enter length: ")
	width = input("Enter width: ")
	plot = int(length) * int(width)
	print(f"Plot area: {plot}")

