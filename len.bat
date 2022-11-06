$path = 'C:\Users\shariq\Desktop\Projects\readify\audio'

Get-ChildItem $path -Filter *.mp3 -name | Foreach-Object {
    $shell = New-Object -COMObject Shell.Application
    $shellfolder = $shell.Namespace($path)
    $shellfile = $shellfolder.ParseName($_)

    write-host $_ $shellfolder.GetDetailsOf($shellfile, 27);
}