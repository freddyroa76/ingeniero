$files = Get-ChildItem "c:\Users\Freddy Roa\OneDrive - AB PROYECTOS SA\Documentos\ingeniero\herramientas\*.html" -Exclude "02_hoop_stress.html"

foreach ($file in $files) {
    if ($file.Name -eq "generate_final_js.py") { continue }
    $content = Get-Content $file.FullName -Raw
    
    # Check if link exists in desktop dropdown (py-2)
    if ($content -notmatch 'href="02_hoop_stress.html".*?py-2') {
        # Regex to match the pipe thickness line. 
        # Escape brackets: \[ and \]
        $regex = '(\s*)<a href="01_pipe_thickness\.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-\[#0f172a\]">Espesores de Tubería</a>'
        
        $newLine = '<a href="02_hoop_stress.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-[#0f172a]">Esfuerzo Circunferencial</a>'
        
        # Perform replacement. $0 is match, $1 is captured indentation group.
        # Use single quotes for replacement string to avoid variable expansion except for specific ones? 
        # Actually in PS string, $0 and $1 are literal unless in regex substitution context.
        # But -replace operator handles the substitution logic.
        # We need to ensure newlines are correct.
        
        $newContent = $content -replace $regex, ('$0' + "`r`n" + '$1' + $newLine)
        
        if ($newContent -ne $content) {
            Set-Content -Path $file.FullName -Value $newContent -NoNewline
            Write-Host "Updated $($file.Name)"
        }
        else {
            Write-Host "Target not found (regex) in $($file.Name)"
        }
    }
    else {
        Write-Host "Already has link: $($file.Name)"
    }
}
