# Comparación: Regresión lineal en Python vs Rust

## Resultados obtenidos

### Python (Concurrencia)

<img width="338" height="237" alt="Screenshot 2025-11-21 084557" src="https://github.com/user-attachments/assets/e98ad62d-5767-4194-a462-34f94062bcdb" />

### Rust (Secuencial)

<img width="534" height="367" alt="Screenshot 2025-11-21 084619" src="https://github.com/user-attachments/assets/414cdc8b-3b78-465d-9091-b0defa15b267" />

---

## Tabla Comparativa

| Aspecto | Python | Rust | Ganador |
|---------|--------|------|---------|
| **Tiempo de ejecución** | 0.3938 s | 0.0006 s | Rust |
| **Parámetro w** | 1.9994 | 1.9994 | Empate (igual) |
| **Parámetro b** | 0.0042 | 0.0042 | Empate (igual) |
| **Predicción x=11** | 21.9976 | 21.9976 | Empate (igual) |

---

## ¿Qué significa esto?

### Velocidad: Rust es **656 veces más rápido**

Para calcular cuántas veces más rápido es Rust:

```
Speedup = Tiempo Python / Tiempo Rust
Speedup = 0.3938 / 0.0006 = 656x
```

**Si Python tarda 6-7 minutos en algo, Rust lo hace en menos de 1 segundo**

### Precisión: Ambos dan exactamente lo mismo

Aunque Rust es mucho más rápido, los resultados son idénticos:
- Los parámetros `w` y `b` calculados son exactamente iguales
- La predicción para `x=11` da el mismo valor
- Ambos usan el mismo modelo matemático

Esto significa que no sacrificamos exactitud por velocidad. Rust es simplemente más eficiente

---

## Conclusión

**Ambos lenguajes aprenden el mismo modelo pero Rust lo hace 656 veces más rápido** (valores de w y b idénticos)

 **Cuándo usar cada uno:**
- **Python**: Cuando se esta aprendiendo o prototipando rápido
- **Rust**: Cuando la velocidad es esencial o se usan millones de datos

---
