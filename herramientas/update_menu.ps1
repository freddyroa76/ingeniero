$target = '<a href="01_pipe_thickness.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-[#0f172a]">Espesores de Tubería</a>'
$replacement = '<a href="01_pipe_thickness.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-[#0f172a]">Espesores de Tubería</a>' + "`r`n" + '                <a href="02_hoop_stress.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-[#0f172a]">Esfuerzo Circunferencial</a>'
$files = Get-ChildItem "c:\Users\Freddy Roa\OneDrive - AB PROYECTOS SA\Documentos\ingeniero\herramientas\*.html" -Exclude "02_hoop_stress.html"

foreach ($file in $files) {
    if ($file.Name -eq "generate_final_js.py") { continue }
    $content = Get-Content $file.FullName -Raw
    # Check if link exists in desktop dropdown (checking for py-2 which is specific to desktop)
    if ($content -notmatch 'href="02_hoop_stress.html".*?py-2') {
        $newContent = $content.Replace($target, $replacement)
        if ($newContent -ne $content) {
            Set-Content -Path $file.FullName -Value $newContent -NoNewline
            Write-Host "Updated $($file.Name)"
        } else {
            Write-Host "Target not found in $($file.Name)"
        }
    } else {
        Write-Host "Already has link: $($file.Name)"
    }
}
