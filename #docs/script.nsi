;--------------------------------

; The name of the installer
Name "emotion"

; The file to write
OutFile "task.exe"

; The default installation directory
InstallDir $DESKTOP\emotion

; Registry key to check for directory (so if you install again, it will 
; overwrite the old one automatically)
InstallDirRegKey HKLM "Software\emotion" "Install_Dir"

; Request application privileges for Windows Vista
RequestExecutionLevel admin


;--------------------------------

; Pages

Page components
Page directory
Page instfiles

UninstPage uninstConfirm
UninstPage instfiles

;--------------------------------

; The stuff to install
Section "emotion (required)"

  SectionIn RO
  
  ; Set output path to the installation directory.
  SetOutPath $INSTDIR
  
  ; Put file there
  File "emotion.nsi"
  
  ; Write the installation path into the registry
  WriteRegStr HKLM SOFTWARE\emotion "Install_Dir" "$INSTDIR"
  
  ; Write the uninstall keys for Windows
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\emotion" "DisplayName" "emotion"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\emotion" "UninstallString" '"$INSTDIR\uninstall.exe"'
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\emotion" "NoModify" 1
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\emotion" "NoRepair" 1
  WriteUninstaller "uninstall.exe"
  
SectionEnd

; Optional section (can be disabled by the user)
Section "Start Menu Shortcuts"

  CreateDirectory "$SMPROGRAMS\emotion"
  CreateShortcut "$SMPROGRAMS\emotion\Uninstall.lnk" "$INSTDIR\uninstall.exe" "" "$INSTDIR\uninstall.exe" 0
  CreateShortcut "$SMPROGRAMS\emotion\emotion (MakeNSISW).lnk" "$INSTDIR\emotion.nsi" "" "$INSTDIR\emotion.nsi" 0
  
SectionEnd

;--------------------------------

; Uninstaller

Section "Uninstall"
  
  ; Remove registry keys
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\emotion"
  DeleteRegKey HKLM SOFTWARE\emotion

  ; Remove files and uninstaller
  Delete $INSTDIR\emotion.nsi
  Delete $INSTDIR\uninstall.exe

  ; Remove shortcuts, if any
  Delete "$SMPROGRAMS\emotion\*.*"

  ; Remove directories used
  RMDir "$SMPROGRAMS\emotion"
  RMDir "$INSTDIR"

SectionEnd
