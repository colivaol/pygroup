# Importar el paquete Flask
from flask import Flask
 
# Inicializamos la aplicación
app = Flask(__name__)
 
# Ruta principal
@app.route('/')
def index():
  return 'Hola Mundo'
 
# Configuración básica
if __name__ == '__main__':
  # Activamos debug y configuramos para que sea accesible desde cualquier dispositivo
  app.run(debug=True, host='0.0.0.0')