# Create a menu and allow the user to make a choice 
$menu = Read-Host "Select an option below by entering a number:`n1 - list directories and files in the current directory`n2 - Create a new file in the current directory`n3 - Create a new folder in the current directory.`n"

if ( $menu -eq 1){
    # List all the directories
    ls
}
elseif ($menu -eq 2){
    # Get the name of the file from the user and create the file in the folder
    $file = Read-Host "Enter the name of the file that you want to create"
    
    # An if statement is created inside the body of the if statement (nested if statement)
    # Check if the file exists before creating it 
    if (Test-Path -Path $file){
        Write-Output "The file named $file already exists" 
    }
    else {
        # Create a new file
        New-Item $file
        Write-Output "File with the name $file has been created"
    } 
}
elseif ($menu -eq 3){
    # Get the name of the file from the user and create the file in the folder
    $folder = Read-Host "Enter the name of the folder that you want to create"
    
    # An if statement is created inside the body of the if statement (nested if statement)
    # Check if the folder exists before creating it 
    if (Test-Path -Path $folder){
        Write-Output "The folder named $folder already exists" 
    }
    else {
        # Create a new folder 
        New-Item -Path $folder -ItemType Directory 
        Write-Output "Folder with the name $folder has been created"
    } 
}
else {
    Write-Output "You have made an invalid choice."
}