# Lillia Lessev
# Shell Scripting


# Create three new folders

$folder1 = Read-Host "Enter name of first folder: "
New-Item -Path $folder1 -ItemType Directory
Write-Output "Folder with the name $folder1 is created"

$folder2 = Read-Host "Enter name of second folder: "
New-Item -Path $folder2 -ItemType Directory
Write-Output "Folder with the name $folder2 is created"

$folder3 = Read-Host "Enter name of third folder: "
New-Item -Path $folder3 -ItemType Directory
Write-Output "Folder with the name $folder3 is created"

# Navigate inside one of the folders
$option = Read-Host "`nWhich folder would you like to navigate into?`nType the number ONLY.`n1 - $folder1`n2 - $folder2`n3 - $folder3`n`nOption: "
if ($option -eq 1){
    # Folder 1
    cd $folder1
    Write-Output "Creating 3 new folders inside $folder1"
    $file1A = "Folder 1A"
    $file1B = "Folder 1B"
    $file1C = "Folder 1C"

    New-Item $file1A
    New-Item $file1B
    New-Item $file1C

    # Deleting Other Two Folders
    $del_option = Read-Host "Would you like to delete $folder2 and $folder3 ?'`Enter only 'y' or 'n'.`nResponse (y/n): "
    if ($del_option -eq 'y'){
        cd ..
        Remove-Item $folder2 -Recurse -Force
        Remove-Item $folder3 -Recurse -Force
        Write-Output "$folder2 and $folder3 deleted."
    }
    elseif ($del_option -eq 'n'){
        Write-Output "Nothing deleted."
    }
    else {
        Write-Output "Not a valid option."
    }
    

} 
elseif ($option -eq 2){
    # Folder 2
    cd $folder2
    Write-Output "Creating 3 new folders inside $folder2"
    $file2A = "Folder 2A"
    $file2B = "Folder 2B"
    $file2C = "Folder 2C"

    New-Item $file2A
    New-Item $file2B
    New-Item $file2C

    # Deleting Other Two Folders
    $del_option = Read-Host "Would you like to delete $folder1 and $folder3 ?'`Enter only 'y' or 'n'.`nResponse (y/n): "
    if ($del_option -eq 'y'){
        cd ..
        Remove-Item $folder1 -Recurse -Force
        Remove-Item $folder3 -Recurse -Force
        Write-Output "$folder1 and $folder3 deleted."
    }
    elseif ($del_option -eq 'n'){
        Write-Output "Nothing deleted."
    }
    else {
        Write-Output "Not a valid option."
    }

}
elseif ($option -eq 3){
    # Folder 3
    cd $folder3
    Write-Output "Creating 3 new folders inside $folder3"
    $file3A = "Folder 3A"
    $file3B = "Folder 3B"
    $file3C = "Folder 3C"

    New-Item $file3A
    New-Item $file3B
    New-Item $file3C

    # Deleting Other Two Folders
    $del_option = Read-Host "Would you like to delete $folder1 and $folder2 ?'`Enter only 'y' or 'n'.`nResponse (y/n): "
    if ($del_option -eq 'y'){
        cd ..
        Remove-Item $folder1 -Recurse -Force
        Remove-Item $folder2 -Recurse -Force
        Write-Output "$folder1 and $folder2 deleted."
    }
    elseif ($del_option -eq 'n'){
        Write-Output "Nothing deleted."
    }
    else {
        Write-Output "Not a valid option."
    }
}
else {
    Write-Output "Not a valid option."
}

