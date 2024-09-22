import py5

def setup():
    # Definir el tamaño de la ventana
    py5.size(800, 600)
    
    # Declarar las variables globales
    global logo, x, y, x_speed, y_speed
    
    # Cargar la imagen del logo
    logo = py5.load_image('logo.png')  # Asegúrate de tener el archivo 'logo.png' en el mismo directorio
    
    # Inicializar las coordenadas del logo en el centro de la pantalla
    x = py5.width / 2
    y = py5.height / 2
    
    # Velocidades iniciales del logo en ambos ejes
    x_speed = 2
    y_speed = 2

def draw():
    # Declarar las variables globales
    global x, y, x_speed, y_speed
    
    # Definir el color de fondo (negro en este caso)
    py5.background(0)
    
    # Dibujar el logo en las coordenadas actuales
    py5.image(logo, x, y)
    
    # Mover el logo sumando las velocidades a las coordenadas x e y
    x += x_speed
    y += y_speed
    
    # Detectar si el logo choca con los bordes horizontales (izquierda o derecha)
    if x <= 0 or x + logo.width >= py5.width:
        x_speed *= -1  # Invertir la dirección en el eje x
    
    # Detectar si el logo choca con los bordes verticales (arriba o abajo)
    if y <= 0 or y + logo.height >= py5.height:
        y_speed *= -1  # Invertir la dirección en el eje y

# Opcional: Función para cambiar la velocidad del logo con las teclas
def key_pressed():
    global x_speed, y_speed
    if py5.key == 'UP':  # Aumentar la velocidad
        x_speed += 1
        y_speed += 1
    elif py5.key == 'DOWN':  # Disminuir la velocidad
        x_speed -= 1
        y_speed -= 1

# Correr el sketch usando py5.run_sketch()
py5.run_sketch()
