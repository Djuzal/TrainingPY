#Нужно чтобы в заданом списке order было повторяющихся элементов не больше max_e
def delete_nth(order,max_e):
    for item in order:
        if order.count(item) > max_e:#Если количество item в списке order > max_e тогдаЖ
            order.reverse() #разворачиваем список чтобы сохранить порядок, иначе команда .remove удалит первый элемент в списке.
            while order.count(item) > max_e:
                order.remove(item)
            order.reverse()#разворачиваем обратно, в правильное положение.
    return order
print(delete_nth([1,1,3,3,7,2,2,2,2], 3))