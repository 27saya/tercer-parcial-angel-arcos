import numpy as np
import threading
import time
from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt

# Datos y configuración
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)
y = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], dtype=float)

tasaAprendizaje = 0.01
marcasTiempo = 1000
num_workers = 4

# Clase regresion concurrente
class RegresionConcurrente:
    def __init__(self, tasaAprendizaje, marcasTiempo, num_workers):
        self.w = 0.0
        self.b = 0.0
        self.tasaAprendizaje = tasaAprendizaje
        self.marcasTiempo = marcasTiempo
        self.num_workers = num_workers
        self.lock = threading.Lock()
        self.historial_mse = []
        
    def procesar_chunk(self, inicio, fin, X, y, y_pred):
        """Un trabajador procesa una sección de los datos"""
        error = y_pred[inicio:fin] - y[inicio:fin]
        suma_error_X = np.dot(error, X[inicio:fin])
        suma_error = np.sum(error)
        return suma_error_X, suma_error
    
    def calcular_gradientes_paralelo(self, X, y, y_pred):
        """Calcula gradientes usando múltiples hilos"""
        m = len(X)
        tamaño_chunk = m // self.num_workers
        
        with ThreadPoolExecutor(max_workers=self.num_workers) as executor:
            futures = []
            for i in range(self.num_workers):
                inicio = i * tamaño_chunk
                fin = m if i == self.num_workers - 1 else (i + 1) * tamaño_chunk
                future = executor.submit(self.procesar_chunk, inicio, fin, X, y, y_pred)
                futures.append(future)
            
            suma_total_X = 0
            suma_total_error = 0
            for future in futures:
                sx, se = future.result()
                suma_total_X += sx
                suma_total_error += se
        
        dw = (2 / m) * suma_total_X
        db = (2 / m) * suma_total_error
        return dw, db
    
    def entrenar(self, X, y):
        """Entrena el modelo"""
        inicio_total = time.time()
        
        for marca in range(self.marcasTiempo):
            y_pred = self.w * X + self.b
            
            # Calcular gradientes en paralelo
            dw, db = self.calcular_gradientes_paralelo(X, y, y_pred)
            
            # Actualizar parámetros
            self.w -= self.tasaAprendizaje * dw
            self.b -= self.tasaAprendizaje * db
            
            # Guardar métrica cada 100 marcas
            if (marca + 1) % 100 == 0:
                error = y_pred - y
                mse = np.mean(error ** 2)
                self.historial_mse.append(mse)
                print(f"Marca {marca+1}, MSE: {mse:.6f}, w: {self.w:.4f}, b: {self.b:.4f}")
        
        tiempo_total = time.time() - inicio_total
        return tiempo_total
    
    def predecir(self, x):
        return self.w * x + self.b
    
    
print("=" * 60)
print("Regresión lineal concurrente en python")
print("=" * 60)

modelo_python = RegresionConcurrente(tasaAprendizaje, marcasTiempo, num_workers)
tiempo_python = modelo_python.entrenar(X, y)

print(f"\nTiempo total: {tiempo_python:.4f} segundos")
print(f"w ≈ {modelo_python.w:.4f}, b ≈ {modelo_python.b:.4f}")
print(f"Predicción para x=11: {modelo_python.predecir(11):.4f}")
