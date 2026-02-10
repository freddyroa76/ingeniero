
# Script para verificar la consistencia entre el objeto de datos y el select HTML en 01_pipe_thickness.html
import re

def extract_select_options(html_content):
    options = []
    # Buscar el select id="pipeSize"
    select_match = re.search(r'<select id="pipeSize"[^>]*>(.*?)</select>', html_content, re.DOTALL)
    if select_match:
        options_html = select_match.group(1)
        # Extraer valores de las opciones
        matches = re.findall(r'<option value="([^"]+)">', options_html)
        for val in matches:
            if val: # Ignorar valor vacío (placeholder)
                options.append(float(val))
    return sorted(options)

def extract_js_keys(html_content):
    keys = []
    # Buscar el objeto pipeDimensions
    # Asumimos que empieza con const pipeDimensions = { y termina con };
    start_marker = 'const pipeDimensions = {'
    start_idx = html_content.find(start_marker)
    
    if start_idx != -1:
        # Extraer el bloque (simplificado, buscando claves numéricas)
        content_after = html_content[start_idx:]
        # Buscar claves como "0.125": o 1: 
        # Regex para claves: (?:^|\s)([\d\.]+): \{
        matches = re.findall(r'(?:^|\s)([\d\.]+): \{', content_after)
        for val in matches:
            keys.append(float(val))
    return sorted(keys, key=float)

file_path = '01_pipe_thickness.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

select_options = extract_select_options(html_content)
data_keys = extract_js_keys(html_content)

print(f"Opciones en SELECT ({len(select_options)}): {select_options}")
print(f"Claves en DATOS ({len(data_keys)}): {data_keys}")

missing_in_select = set(data_keys) - set(select_options)
missing_in_data = set(select_options) - set(data_keys)

if not missing_in_select and not missing_in_data:
    print("\n✅ TODO CORRECTO: El menú desplegable coincide exactamente con la base de datos.")
else:
    if missing_in_select:
        print(f"\n❌ FALTAN EN EL SELECT: {sorted(list(missing_in_select))}")
    if missing_in_data:
        print(f"\n❌ SOBRAN EN EL SELECT (no hay datos): {sorted(list(missing_in_data))}")
