def promedio_estudiante(calificaciones):
    if len(calificaciones) == 0:
        return 0.0  # evita ZeroDivisionError
    
    promedio = sum(calificaciones) / len(calificaciones)
    return float(promedio)