from pygame import *
class Plitka:
    """Класс, содержащий плитки/кирпичики, которые уничтожаются, когда в них попадает шарик
    Содержит положение плитки(x, y - центр плитки), размер плитки(l - длина, d - ширина), цвет плитки, статус жизни(уничтожена или нет), ряд и столбец плитки"""
    
    x = 0
    
    y = 0
    
    l = 0
    
    d = 0
    
    ryad = 0
    
    stolb = 0
    
    color = ' '
    #FIXME: почему-то подчеркивает красным
    zhizn = true

#Здесь функция, которая задает всем плиткам положение и цвет

vse_plitki = []

def unique_plitka(Plitka):
    for i in range (78):
        pl = Plitka
    for i in range (6):
        for j in range (13):
            Plitka.ryad = i
            Plitka.stolb = j
            vse_plitki.append(Plitka)
    for 
    