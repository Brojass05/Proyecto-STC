; Script generado por el asistente de Inno Setup

[Setup]
AppName=SpeechToClip
AppVersion=1.0
DefaultDirName={userdesktop}\SpeechToClip
DefaultGroupName=Speech To Clip
OutputDir=C:\Users\benja\Desktop
OutputBaseFilename=InstallerSTC
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\Users\benja\Desktop\Proyecto_STC\dist\config\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs
Source: "C:\Users\benja\Desktop\Proyecto_STC\dist\escucha_por_debajo\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs


[Icons]
; Accesos directos al ejecutable principal
Name: "{group}\Speech To Clip"; Filename: "{app}\escucha_por_debajo.exe"
Name: "{userdesktop}\Speech To Clip"; Filename: "{app}\escucha_por_debajo.exe"
; Acceso directo para desinstalar
Name: "{group}\Desinstalar Speech To Clip"; Filename: "{uninstallexe}"

[Run]
; Opcionalmente, puedes agregar configuraciones que se ejecuten tras la instalación.
