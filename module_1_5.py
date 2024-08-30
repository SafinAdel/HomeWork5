immutable_var=('Камень', 'Ножницы', 'Бумага', 'Ящерица', 'Спок', 1, 2, 3)
# immutable_var [0]=Вода выдаст ошибку. Для изм. дан. в кортеже, необ. прописать новый кортеж,(стр. 4) или исп. сложение (стр. 7)
print(immutable_var)
immutable_var=('7', 'Ножницы', 'Бумага', 'Ящерица', 'Спок', 1, 2, 3)
print(immutable_var)
immutable_var_new='Вода'
immutable_var=(immutable_var_new,) + immutable_var[1:]
print(immutable_var)

mutable_list=["Table", "Chair", "Sofa"]
mutable_list [0] = "Стол"
mutable_list [1] = 1000
mutable_list [2] = "Диван"
print(mutable_list)