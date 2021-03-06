"""Snake, classic arcade game.
Exercises
1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.
"""

'''
Herramientas Computacionales: El Arte de la Programación
Grupo: 201   TC1001S
Modified by:
        Léa Rodríguez Jouault A01659896   
        Mauricio Juárez Sánchez A01660336'''

#Importamos librería turtle para dibujar la serpiente, dibujar la comida y entre otras funciones
#Importamos random para las funciones aleatorias

from turtle import *
import random
from freegames import square, vector

saltos=[10,0,-10] #Grupo de valores que nos permiten mover la comida en el tablero

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors=['green','magenta','purple', 'orange','blue'] #Lista con los colores posibles de la comida y serpiente
colorSnake=random.choice(colors) #Elección aleatoria de colores para la serpiente
colorFood=random.choice(colors) #Elección de colores aleatoria para la comida
while(colorSnake==colorFood): #Sentencia para que la serpiente y comida difieran en color
    colorFood=random.choice(colors)
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190
tiempo = 0
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = random.randrange(-15, 15) * 10
        food.y = random.randrange(-15, 15) * 10
        square(food.x, food.y, 9, colorFood)
    else:
        snake.pop(0)

    clear()
    global tiempo  #Variable global
    tiempo += 1  #Nos permite controlar el tiempo para que la comida no se mueva tan rápido
    for body in snake:
        square(body.x, body.y, 9, colorSnake)
    if (tiempo == 7): #Tiempo ajustado para un funcionamiento apropiado de la serpiente
        if ((food.x <= 180 and food.x >= -180) and (food.y <= 180 and food.y >= -180)):
            food.x = food.x + random.choice(saltos) #Ocupamos esto para saltos aleatorios en X
            food.y = food.y + random.choice(saltos) #Ocupamos esto para saltos aleatorios en Y
        elif (food.x <= -180 and food.y >= 180): #Esquina Arriba Izquierda
            food.x = food.x + saltos[0]
            food.y= food.y - saltos[0]

        elif (food.x >= 180 and food.y >= 180): #Esquina Arriba Derecha
            food.x = food.x - saltos[0]
            food.y = food.y - saltos[0]

        elif (food.x <= -180 and food.y <= -180): #Esquina Abajo Izquierda
            food.x = food.x + saltos[0]
            food.y = food.y + saltos[0]

        elif (food.x >= 180 and food.y <= -180): #Esquina Abajo Derecha
            food.x = food.x - saltos[0]
            food.y = food.y + saltos[0]

        #Las siguientes sentencias permiten que la comida se mueva por todo el tablero
        elif (food.x >= 180 and (food.y <=180 and food.y>=-180)):
            food.x = food.x - saltos[0]
        elif (food.x <= -180 and (food.y <=180 and food.y>=-180)):
            food.x = food.x + saltos[0]
        elif (food.y >= 180 and (food.x <=180 and food.x>=-180)):
            food.x = food.x - saltos[0]
        elif (food.y <= -180 and (food.x <180 and food.x>=-180)):
            food.x = food.x + saltos[0]
        tiempo = 0
    square(food.x, food.y, 9, colorFood)
    update()
    ontimer(move, 80) #Velocidad a la que progresan los eventos en el juego
#
setup(420, 420, 360, 0) #Tamaño y posición del tablero
hideturtle()
tracer(False)
listen()

#Se recibe como input las entradas por teclado y se realiza una acción posterior, en este caso mover unidades.
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done() #Fin del programa