res =[
	{'id': 62, 'first_name': 'Test', 'last_name': 'Test', 'email': 'test@gmail.com', 'dog_id': 246, 'name': 'rrg', 'sex': 'f', 'age_months': 95, 'birth_month': 12, 'birth_day': 6, 'feeding_amount_kcal': 1741.4, 'feeding_amount_cups': 3.0},
	{'id': 62, 'first_name': 'Test', 'last_name': 'Test', 'email': 'test@gmail.com', 'dog_id': 248, 'name': 'iu', 'sex': 'm', 'age_months': 80, 'birth_month': 10, 'birth_day': 7, 'feeding_amount_kcal': 1834.2, 'feeding_amount_cups': 3.0},
	{'id': 62, 'first_name': 'Test', 'last_name': 'Test', 'email': 'test@gmail.com', 'dog_id': 249, 'name': 'b fgbg', 'sex': 'm', 'age_months': 82, 'birth_month': 12, 'birth_day': 5, 'feeding_amount_kcal': 1628.1, 'feeding_amount_cups': 3.0},
	{'id': 62, 'first_name': 'Test', 'last_name': 'Test', 'email': 'test@gmail.com', 'dog_id': 261, 'name': 'njfrnf', 'sex': 'm', 'age_months': 200, 'birth_month': 4, 'birth_day': 13, 'feeding_amount_kcal': 1467.3, 'feeding_amount_cups': 3.0},
	{'id': 63, 'first_name': 'Dave', 'last_name': 'Knoepfle', 'email': 'dave.knoepfle@coastandrange.com', 'dog_id': 250, 'name': 'Dharma', 'sex': 'f', 'age_months': 125, 'birth_month': 5, 'birth_day': 31, 'feeding_amount_kcal': 1101.2, 'feeding_amount_cups': 2.0},
	{'id': 63, 'first_name': 'Dave', 'last_name': 'Knoepfle', 'email': 'dave.knoepfle@coastandrange.com', 'dog_id': 251, 'name': 'Hana', 'sex': 'f', 'age_months': 116, 'birth_month': 2, 'birth_day': 14, 'feeding_amount_kcal': 1560.3, 'feeding_amount_cups': 3.0},
	{'id': 63, 'first_name': 'Dave', 'last_name': 'Knoepfle', 'email': 'dave.knoepfle@coastandrange.com', 'dog_id': 252, 'name': 'Hana', 'sex': 'f', 'age_months': 116, 'birth_month': 2, 'birth_day': 14, 'feeding_amount_kcal': 845.2, 'feeding_amount_cups': 1.0},
	{'id': 63, 'first_name': 'Dave', 'last_name': 'Knoepfle', 'email': 'dave.knoepfle@coastandrange.com', 'dog_id': 254, 'name': 'Dharma', 'sex': 'f', 'age_months': 53, 'birth_month': 4, 'birth_day': 4, 'feeding_amount_kcal': 1483.6, 'feeding_amount_cups': 3.0},
	{'id': 64, 'first_name': 'Leith', 'last_name': 'Henry', 'email': 'konaskitchen@gmail.com', 'dog_id': 253, 'name': 'Hana', 'sex': 'f', 'age_months': 117, 'birth_month': 2, 'birth_day': 14, 'feeding_amount_kcal': 845.2, 'feeding_amount_cups': 1.0},
	{'id': 65, 'first_name': 'Becky', 'last_name': 'Knoepfle', 'email': 'rebeccaknoepfle@hotmail.com', 'dog_id': 255, 'name': 'Dharma', 'sex': 'f', 'age_months': 124, 'birth_month': 5, 'birth_day': 31, 'feeding_amount_kcal': 1175.5, 'feeding_amount_cups': 2.0},
	{'id': 66, 'first_name': 'Tenicka', 'last_name': 'Kingsley', 'email': 'tenicka_kingsley@yahoo.com', 'dog_id': 256, 'name': 'Nala', 'sex': 'f', 'age_months': 51, 'birth_month': 8, 'birth_day': 1, 'feeding_amount_kcal': 510.2, 'feeding_amount_cups': 1.0},
	{'id': 66, 'first_name': 'Tenicka', 'last_name': 'Kingsley', 'email': 'tenicka_kingsley@yahoo.com', 'dog_id': 257, 'name': 'Nala', 'sex': 'f', 'age_months': 51, 'birth_month': 8, 'birth_day': 1, 'feeding_amount_kcal': 510.2, 'feeding_amount_cups': 1.0},
	{'id': 66, 'first_name': 'Tenicka', 'last_name': 'Kingsley', 'email': 'tenicka_kingsley@yahoo.com', 'dog_id': 258, 'name': 'Nala', 'sex': 'f', 'age_months': 51, 'birth_month': 8, 'birth_day': 1, 'feeding_amount_kcal': 510.2, 'feeding_amount_cups': 1.0},
	{'id': 67, 'first_name': 'Priyanka', 'last_name': 'Superstar', 'email': 'priyanka.impinge@gmail.com', 'dog_id': 259, 'name': 'Doug', 'sex': 'f', 'age_months': 68, 'birth_month': 4, 'birth_day': 8, 'feeding_amount_kcal': 980.8, 'feeding_amount_cups': 2.0},
	{'id': 68, 'first_name': 'Gggfg', 'last_name': 'Ggju', 'email': 'tesrgg@ftj.hhj', 'dog_id': 260, 'name': 'Thhj', 'sex': 'm', 'age_months': 28, 'birth_month': 5, 'birth_day': 4, 'feeding_amount_kcal': 879.1, 'feeding_amount_cups': 1.0}
]


c=0
for j in res:	
	dogs=[]
	g=j['id']
	if c!=g:
		for i in res:
			c=g
			if i['id']==g:
				x={'name':i['name']}
				y={i['dog_id']:x}
				dogs.append(y)
				dog={'email':i['email'],'dogs':dogs}
				id={i['id']:dog}				
		print(id)
	


		

		
			
