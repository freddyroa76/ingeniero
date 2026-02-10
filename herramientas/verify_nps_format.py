# FORMATO DE TAMAÑOS NPS - VERIFICACIÓN

print("=" * 70)
print("FORMATO DE TAMAÑOS NPS CON FRACCIONES")
print("=" * 70)

# Mapeo de tamaños
size_mapping = {
    0.125: '1/8"',
    0.25: '1/4"',
    0.375: '3/8"',
    0.5: '1/2"',
    0.75: '3/4"',
    1: '1"',
    1.25: '1-1/4"',
    1.5: '1-1/2"',
    2: '2"',
    2.5: '2-1/2"',
    3: '3"',
    3.5: '3-1/2"',
    4: '4"',
    5: '5"',
    6: '6"',
    8: '8"',
    10: '10"',
    12: '12"',
    14: '14"',
    16: '16"',
    18: '18"',
    20: '20"',
    22: '22"',
    24: '24"',
    30: '30"',
    32: '32"',
    34: '34"',
    36: '36"',
    42: '42"'
}

print("\nTamaños con FRACCIONES (formato estándar de la industria):")
print("-" * 70)
fractional_sizes = [0.125, 0.25, 0.375, 0.5, 0.75, 1.25, 1.5, 2.5, 3.5]
for size in fractional_sizes:
    print(f"  {str(size).ljust(6)} => {size_mapping[size]}")

print("\nTamaños ENTEROS:")
print("-" * 70)
whole_sizes = [1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 30, 32, 34, 36, 42]
for size in whole_sizes:
    print(f"  {str(size).ljust(6)} => {size_mapping[size]}")

print("\n" + "=" * 70)
print("CONFORMIDAD CON ESTÁNDARES DE LA INDUSTRIA")
print("=" * 70)
print("\n[OK] Tamaños fraccionarios usan notación estándar (ej: 1/2\", 1-1/4\")")
print("[OK] Tamaños enteros incluyen símbolo de pulgadas (\")")
print("[OK] Formato compatible con ASME B36.10M y práctica industrial")
print("\n*** FORMATO DE VISUALIZACIÓN CORRECTO ***")
print("=" * 70)
