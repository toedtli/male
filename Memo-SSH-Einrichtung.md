Bei SSH, git etc. kann die Eingabe des Passworts bald mühsam werden. Eine sichere Übertragung ohne ständige Passworteingabe ist aber möglich mit public key-Verschlüsselung. So geht's:
- Ausführen:
ssh-keygen
Dies generiert ein Schlüsselpaar (public/private). Den Privaten sicher verwahren (dort, wo er ist).
- Den öffentlichen Schlüssel unter ~/.ssh/id-rsa.pub
auf Github hochladen
- git clone mit ssh
- Angabe von 
git config --global user.email "beat.toedtli@gmail.com"

