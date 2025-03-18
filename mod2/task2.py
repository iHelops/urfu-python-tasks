square_side_length = float(input(""))

perimeter = round(4*square_side_length, 2)
area = round(square_side_length**2, 2)
diagonal = round(((square_side_length**2) * 2) ** 0.5, 2);


print(f'{perimeter}, {area}, {diagonal}') 