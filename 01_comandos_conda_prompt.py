""" 
COMANDOS DESDE EL PROMPT DE CONDA
Los entornos de conda se crean para crear proyectos que contengan versiones específicas de las librerias que requiera el proyecto. De esta manera se tiene aisladas las herramientas y versiones parea el proyecto en el entorno que se administre.
Puede trabajar en varios ambientes en el mismo equipo. Solo debe tener en cuenta activar el entorno en el cual vaya a trabajar. 
Para estos comandos, se requiere haber instalado anaconda, posteriormente abrir el prompt de conda, el cual debe figurar en la lista de programas instalados como Conda Prompt  
Puede crear un entorno y configurarlo en power bi en las herramientas de opciones, solo debe especificar la ruta del entorno.  Así power bi trabajará con las utilerías del entorno configurado.

* Ver el entorno (ambiente actual) actual: 
    conda info --envs

* Cuando ejecutas el comando para ver los entornos instalados, el entorno activo es aquel que contiene un asterisco * 
   
* Crear nuevo entorno(ambiente) de Conda:

    conda create --name <mi_entorno> python=version
    Ejemplo: create --name entorno1 python=3.8

* activar el entorno:
    conda activate <mi_entorno>

* Desactivar el entorno:
    conda deactivate <mi_entorno>

* Ver las librerías o módulos instalados en un entorno:
   pip install <nombre modulo>
   ejemplo: pip install pandas
   
   opcion2: conda install <nombre modulo>
            ejemplo: conda install pandas
            
            
* Actualizar conda y todos los paquetes:
    conda update conda
    conda update all

* Eliminar un entorno: Debe estar en el entorno base o fuera del entorno que desea eliminar
    conda env remove --name <mi-entorno>
    posteriormente listar los entornos para verificar.
    
"""