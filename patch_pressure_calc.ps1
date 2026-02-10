$path = "herramientas\03_max_design_pressure.html"
$content = Get-Content $path -Encoding UTF8

if ($content.Count -gt 1032) {
    # Replace lines 1033-1037 with new content
    # The original lines look like:
    # 1033:         document.getElementById("formulaDetails").innerHTML = `
    # 1034:                 <strong>Calculation Walkthrough:</strong><br>
    # 1035:                 P = (2  ${t.toFixed(4)}  ${S}  ${F}  ${E}  ${T}) / ${D.toFixed(3)}<br>
    # 1036:                 P = ${(2 * t * S * F * E * T).toFixed(2)} / ${D.toFixed(3)}<br>
    # 1037:                 <strong>P = ${Math.round(P_max).toLocaleString()} psi</strong>
    # 1038:             `;

    $newBlock = @(
        '        document.getElementById("formulaDetails").innerHTML = `',
        '                <div class="overflow-x-auto">',
        '                  <table class="w-full text-sm text-left text-gray-500">',
        '                    <thead class="text-xs text-gray-700 uppercase bg-gray-50">',
        '                        <tr>',
        '                            <th scope="col" class="px-6 py-3">Parameter</th>',
        '                            <th scope="col" class="px-6 py-3">Value</th>',
        '                            <th scope="col" class="px-6 py-3">Description</th>',
        '                        </tr>',
        '                    </thead>',
        '                    <tbody>',
        '                        <tr class="bg-white border-b">',
        '                            <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">D (Diameter)</td>',
        '                            <td class="px-6 py-4">${D.toFixed(3)}"</td>',
        '                            <td class="px-6 py-4">Outside Diameter</td>',
        '                        </tr>',
        '                        <tr class="bg-white border-b">',
        '                            <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">t (Thickness)</td>',
        '                            <td class="px-6 py-4">${t.toFixed(4)}"</td>',
        '                            <td class="px-6 py-4">Wall Thickness</td>',
        '                        </tr>',
        '                        <tr class="bg-white border-b">',
        '                            <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">S (SMYS)</td>',
        '                            <td class="px-6 py-4">${S.toLocaleString()} psi</td>',
        '                            <td class="px-6 py-4">Specified Minimum Yield Strength</td>',
        '                        </tr>',
        '                         <tr class="bg-white border-b">',
        '                            <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">F (Design)</td>',
        '                            <td class="px-6 py-4">${F.toFixed(2)}</td>',
        '                            <td class="px-6 py-4">Design Factor</td>',
        '                        </tr>',
        '                         <tr class="bg-white border-b">',
        '                            <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">E (Joint)</td>',
        '                            <td class="px-6 py-4">${E.toFixed(2)}</td>',
        '                            <td class="px-6 py-4">Longitudinal Joint Factor</td>',
        '                        </tr>',
        '                         <tr class="bg-white border-b">',
        '                            <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">T (Temp)</td>',
        '                            <td class="px-6 py-4">${T.toFixed(3)}</td>',
        '                            <td class="px-6 py-4">Temperature Derating Factor</td>',
        '                        </tr>',
        '                    </tbody>',
        '                  </table>',
        '                </div>',
        '',
        '                <div class="mt-6 p-4 bg-gray-50 rounded-lg border border-gray-200">',
        '                    <h4 class="text-sm font-bold text-gray-900 uppercase mb-2">Calculation Step-by-Step</h4>',
        '                    <p class="font-mono text-sm text-gray-700 mb-2">',
        '                        P = (2 &times; S &times; t &times; F &times; E &times; T) / D',
        '                    </p>',
        '                    <p class="font-mono text-sm text-gray-700 mb-2">',
        '                        P = (2 &times; ${S} &times; ${t.toFixed(4)} &times; ${F} &times; ${E} &times; ${T}) / ${D.toFixed(3)}',
        '                    </p>',
        '                    <p class="font-mono text-sm text-gray-700 mb-4">',
        '                         P = ${(2 * t * S * F * E * T).toFixed(2)} / ${D.toFixed(3)}',
        '                    </p>',
        '                    <div class="flex items-center gap-3 pt-4 border-t border-gray-200">',
        '                        <span class="text-xs font-bold text-gray-500 uppercase">Calculated Result:</span>',
        '                        <span class="text-xl font-bold text-[#008F4C]">${Math.round(P_max).toLocaleString()} psi</span>',
        '                    </div>',
        '                </div>',
        '            `;'
    )
    
    # Simple direct overwrite of lines by index since we know exactly where they are
    # Lines are 0-indexed in array but 1-indexed in viewer
    # Viewer said 1033 starts the block. So index 1032.
    
    # We will slice before and after
    $before = $content[0..1032]
    $after = $content[1038..($content.Count - 1)]
    
    $finalContent = $before + $newBlock + $after
    $finalContent | Set-Content $path -Encoding UTF8
    Write-Host "File patched successfully."
}
else {
    Write-Error "File too short or structure changed."
}
