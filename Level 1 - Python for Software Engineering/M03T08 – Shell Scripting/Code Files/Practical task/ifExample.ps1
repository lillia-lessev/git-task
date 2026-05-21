# Lillia Lessev
# Shell Scripting

$new_folder = "new_folder"
$if_folder = "if_folder"

# Check if new_folder exists
if (Test-Path -Path $new_folder -PathType Container){
    # new_folder already exists
    cd $new_folder
    
    if (Test-Path -Path $if_folder -PathType Container){
        # if_folder already exists
        cd $if_folder
        $my_newer_folder = "hyperionDev"
        New-Item -Path $my_newer_folder -ItemType Directory -Force | Out-Null
        write-Output "`nThe folder called $my_newer_folder was created inside the folder called $if_folder`n"
    }
    
    else{
        # if_folder doesn't exist
        #cd $new_folder
        Write-Output "`nThe folder called $new_folder exists."
        New-Item -Path $if_folder -ItemType Directory -Force | Out-Null
        Write-Output "The folder called $if_folder was created inside the folder called $new_folder`n"

    }
    
    }
else {
    Write-Output "`nThe folder called $new_folder does not exist.`nCould not create $if_folder inside $new_folder`n"

}