# Punto 1 y 2 - Regresiones lineales

## 1. Diseño con concurrencia y calculo pi

```mermaid
classDiagram
    class DatosRegresion {
        -X: Array
        -y: Array
        -m: int
        +cargar_datos()
        +obtener_tamaño()
    }
    
    class CalculadorGradientes {
        -numero_trabajadores: int
        +calcular_gradiente_w_paralelo()
        +calcular_gradiente_b_paralelo()
        -dividir_trabajo()
    }
    
    class hiloTrabajador {
        -inicio: int
        -fin: int
        -X: Array
        -y: Array
        -y_pred: Array
        +procesar_chunk()
        +retornar_suma_parcial()
    }
    
    class RegresionConcurrente {
        -w: float
        -b: float
        -tasaAprendizaje: float
        -marcaTiempo: int
        -calculador: CalculadorGradientes
        -datos: DatosRegresion
        +entrenar()
        +actualizar_parametros()
        +predecir()
    }
    
    class CalculadorPI {
        -num_puntos: int
        +estimar_pi_monte_carlo()
        -generar_puntos_aleatorios()
    }
    
    class MonitorProgreso {
        -marca_actual: int
        +mostrar_mse()
        +mostrar_pi_actual()
        +sincronizar_hilos()
    }
    
    DatosRegresion --> RegresionConcurrente
    RegresionConcurrente --> CalculadorGradientes
    CalculadorGradientes --> hiloTrabajador
    RegresionConcurrente --> CalculadorPI
    RegresionConcurrente --> MonitorProgreso
```

### Explicacion del diseño:

**Componentes principales**:
- **DatosRegresion**: Almacena X, y de forma segura para acceso concurrente
- **CalculadorGradientes**: Coordina múltiples workers para calcular gradientes en paralelo
- **hiloTrabajador**: Cada trabajador procesa un pedazo de los datos
- **RegresionConcurrente**: Organiza todo el flujo
- **CalculadorPI**: Estima pi en segundo plano (métrica de concurrencia)
- **MonitorProgreso**: Sincroniza outputs y muestra métricas

**Ventajas**: Los gradientes se calculan más rápido dividiendo el trabajo entre diferentes nue del procesador.
**Nota**: El numero pi se calculó utilizando el metodo de monte carlo, el cual consiste en que por medio de la estadística y la probabilidad, determinar valores o soluciones de ecuaciones que calculados con exactitud son muy complejas, pero que mediante este método resulta sencillo calcular una aproximación al resultado que buscamos.

---
## 2. Diseño con paradigma de aspectos

```mermaid
classDiagram
    class RegresionLineal {
        -w: float
        -b: float
        -tasaAprendizaje: float
        -marcaTiempo: int
        +entrenar()
        +predecir()
    }
    
    class AspectoValidacion {
        +validar_antes_entrenar()
        +validar_datos()
        +validar_hiperparametros()
    }
    
    class AspectoLogging {
        +registrar_inicio()
        +registrar_fin()
        +registrar_cada_marca()
        +guardar_logs()
    }
    
    class AspectoPersistencia {
        +guardar_modelo()
        +cargar_modelo()
        +backup_parametros()
    }
    
    class AspectoTiempo {
        +medir_tiempo_entrenamiento()
        +medir_tiempo_prediccion()
        +registrar_duracion()
    }
    
    class AspectoManejo {
        +capturar_excepciones()
        +registrar_errores()
        +recuperar_estado()
    }
    
    class AspectoOptimizacion {
        +detener_anticipadamente()
        +convergencia()
        +ajustar_tasaAprendizaje()
    }
    
    RegresionLineal --> AspectoValidacion
    RegresionLineal --> AspectoLogging
    RegresionLineal --> AspectoPersistencia
    RegresionLineal --> AspectoTiempo
    RegresionLineal --> AspectoManejo
    RegresionLineal --> AspectoOptimizacion
```

### Explicacion del diseño con Aspectos:

**Idea general**: La clase principal de regresión solo se enfoca en lo esencial (entrenar y predecir). Todo lo "extra" se maneja como aspectos que se aplican automáticamente.

**Aspectos (responsabilidades)**:
- **AspectoValidacion**: Revisa que datos y parámetros sean válidos antes de hacer nada
- **AspectoLogging**: Registra qué está pasando en cada paso
- **AspectoPersistencia**: Guarda y carga el modelo
- **AspectoTiempo**: Mide cuánto tarda todo
- **AspectoManejo**: Si algo falla, lo captura y recupera
- **AspectoOptimizacion**: Decide si parar antes de terminar todos las marcas de tiempo

**Ventaja**: Si se necesita agregar una nueva responsabilidad, solo hace fakta crear un nuevo aspecto sin tocar la clase principal.

