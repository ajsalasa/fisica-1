import math

print("=== Suma de vectores 2D ===")

# pedir cuántos vectores
n = int(input("¿Cuántos vectores vas a sumar? "))

sx = 0  # suma en x
sy = 0  # suma en y

for i in range(n):
    print(f"\nVector {i + 1}")
    modo = input("1) magnitud y ángulo (°)\n2) componentes x,y\nElige 1 o 2: ")

    if modo == "1":
        mag = float(input("  magnitud: "))
        ang_deg = float(input("  ángulo en grados: "))
        rad = math.radians(ang_deg)
        x = mag * math.cos(rad)
        y = mag * math.sin(rad)
    else:  # si escribe otra cosa, asumimos x,y directos
        x = float(input("  x: "))
        y = float(input("  y: "))

    sx += x
    sy += y

print("\n--- Resultado ---")
print("Componente x:", round(sx, 4))
print("Componente y:", round(sy, 4))

mag_r = math.hypot(sx, sy)
ang_deg_r = math.degrees(math.atan2(sy, sx))

print("\nForma polar:")
print("Magnitud:", round(mag_r, 4))
print("Ángulo:", round(ang_deg_r, 2), "°")
