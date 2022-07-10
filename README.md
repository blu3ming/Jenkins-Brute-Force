# Jenkins - Brute Force Atack

Script que nos permite efectuar un ataque de fuerza bruta sobre un panel de logueo de Jenkins. Se realiza lanzando una serie de peticiones POST sobre el endpoint: */j_acegi_security_check* con credenciales de diccionario en busca de una combinación válida.

El script requiere de tres parámetros básicos:
- URL destino (con el endpoint anterior)
- Diccionario de contraseñas
- Un usuario a probar (solo uno)

		python2 jenkins-brute-force.py http://10.10.20.30/j_acegi_security_check /usr/share/wordlists/rockyou.txt admin

![37](https://user-images.githubusercontent.com/25083316/178154558-91cb3289-cf99-4c57-bf4e-e5acac6334c7.png)

Cuando realizamos un logueo no exitoso, el sistema nos devuelve un mensaje diciendo *Invalid username or password*; por lo tanto, analizamos la respuesta de cada petición en busca de aquella que no contenga dicha cadena, entonces podríamos asegurar estar frente a una credencial válida.

Nota: Se intentó una implementación por medio de hilos para agilizar la búsqueda, por desgracia, esta daba error en cada ejecución al mostrar una desconexión con el servidor remoto. Queda a futuro arreglar esto para hacer la búsqueda más eficiente.
