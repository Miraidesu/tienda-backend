
# Tienda venta componenentes PC
Aplicación web de venta de componentes para PC, hecha con Framework Django<br>
Tercera y cuarta evaluación para la asignatura "Programación Backend"

## Instalación
<details>
  <summary><h3>Cómo contribuir en el proyecto (mini tutorial Pull Request)</h3></summary>
  
  ### Requisitos
  Tener instalado [Git](https://git-scm.com/), [GitHub Desktop](https://desktop.github.com/download/) y [VSCode](https://code.visualstudio.com/) (xd)
  <br><br><hr>
  *Clonar repositorio en GitHub Desktop* 
  <br>en este caso: <b>Miraidesu/tienda-backend</b>
  <br><br>
  ![367130563-98f4655a-d577-4407-af45-656c0245d194](https://github.com/user-attachments/assets/a684dccd-8af5-4919-8511-d4c96d607791)

  ![367130905-48848c1a-b6c8-48a9-8627-85fdca834bae](https://github.com/user-attachments/assets/9a2c2311-48b7-4120-a2ab-18a130b24798)<br><hr>
  *Crear una "branch" del repositorio*<br>
  Esta será una version personal del proyecto para agregar o editar archivos sin modificar el respositorio original (main)
  <br><br>
  ![367132799-f609f6e8-2f8a-4e71-844c-b09ded34703a](https://github.com/user-attachments/assets/0d1b12a3-f589-4797-aeae-8935c1a9c4f3)<br><br>
  Lo ideal sería ponerle un nombre correspondiente al cambio que se va a hacer pero da igual
  <br><br>
  ![367134027-85d0f67f-b050-4fb5-85b5-d92620af9157](https://github.com/user-attachments/assets/be30807a-875e-4f14-8b16-a35736279a0b)

 
 <br><br><hr>
  *Abrir proyecto en VSCode*
  <br><br>
  ![367134799-4df2e80b-296d-4321-bb73-d6b5fe768d55](https://github.com/user-attachments/assets/bcbf9ee8-fcca-4d6d-abb5-78305c438f17)<br><br>
  A partir de aqui hacer todos los cambios que quieras<br>
  Por ejemplo, creé un componente Index para la pagina<br><br>
 ![17dec374-83c8-4e25-aa5e-31f7d4eb8f28](https://github.com/user-attachments/assets/d2c29fb1-ad8e-42fe-898e-44822a5c63ae)

  <br><br><hr>
  Guardar los cambios e ir a este icono (Source Control), este aparece al tener Git instalado

![78346b23-d29c-4a7f-ab9b-25df6f7f771d](https://github.com/user-attachments/assets/3f8a29a5-fa9c-4bfb-9481-99090aaf034f)
 <br><br>
  <br><br>
  Presionar el boton + para ir agregando los cambios

 ![ab18a51e-6c21-4081-b162-b753bc46826d](https://github.com/user-attachments/assets/cde34fcf-2a73-41ca-9f12-6f6dfb6fdf7c)
<br><br>
  <br><br>
  Se pueden agregar varios archivos al grupo de cambios, pero es recomendable hacerlo uno a uno (cada commit)<br>
  Agregar mensaje acorde al cambio que se hizo y presionar "Commit" y "Push origin"
  <br><br>
![304a8bd1-e6ad-4efd-86b4-9580f8d126f5](https://github.com/user-attachments/assets/588f25af-2522-4337-8ead-c2f6a7635468)

  <br><br><hr>
  Una vez hecho esto, volver al Github Desktop y publicar la branch<br><br>
  <br>
![67255e9d-471d-4748-8caf-6f4304a94281](https://github.com/user-attachments/assets/ff5c919c-1236-4964-90c7-9aa9c3b19d4e)

  Al ir a la pagina del repositorio, aparecera esta ventana<br>
  Presionar el boton Compare & pull request<br><br>
 ![31f80393-bc91-42a2-a49f-dad029c94d89](https://github.com/user-attachments/assets/9c0605f4-b02b-4132-b8b9-f45a7cbd8a43)
 <br><br>
  Aqui aparecerá toda la información sobre los cambios, verificar y Create pull request
  <br><br>
  ![b32c2c25-4693-479f-b5db-b6dd5100e285](https://github.com/user-attachments/assets/f4ec57f1-437f-4e25-8143-a4ef8e63ee0c)


  <br><br>
  <hr>
</details>


Libreria de componentes [daisyUI](https://daisyui.com/components/)

En la ruta raíz del proyecto:
```bash
python -m venv .venv            # creación entorno virtual
.venv/Scripts/activate          # activar entorno virtual - linux: 'source .venv/bin/activate'
pip install -r dependencias.txt # instalación paquetes (Django, etc...)
python manage.py runserver      # correr aplicación
```
SIEMPRE correr Django en el entorno virutal, si hay un error al instalar paquetes o al correr el programa usar [Python 3.11.2](https://www.python.org/downloads/release/python-3112/)
