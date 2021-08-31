# EPN

## Examen primer bimestre de Analisis de Datos

**Carlos Diaz**

Implementar los scripts necesarios de acuerdo a la arquitectura propuesta.

Crear un repositorio de github donde se implemente mediante scripts de python cada numeral de la arquitectura de ingesta de datos. Los scripts deben llamarse “n.py” donde “n” es el # de script correspondiente. El readme del repositorio debe ser explicativo, es decir en sus palabras deben indicar cada script o proceso de forma general.

Subir el link de github al aula virtual. NO puede hacer cambios en el repositorio posterior a la hora límite.

Cualquier similitud en los comentarios del código serán considerados copia.

![img.png](img.png)
1. Implementamos tweepy para obtener informacion sobre ciudades de Japon donde se desarrollan los juegos olimpicos, esto se almacena en CouchDB

![img_1.png](img_1.png)
2. Implementamos tweepy para obtener informacion sobre las palabras 'juegos olimpicos', 'Tokio 2020' para obtener informacion acerca de los juegos olimpicos, esto se almacena en CouchDB

![img_2.png](img_2.png)
3. Implementamos un web scraper que permite obtener informacion en la pagina del comercion acerca de los juegos olimpicos, se lamacena en MongoDB de forma local

![img_3.png](img_3.png)
4. Implementamos facebook scraper para tomar informacion de la pagina olympics de la cual nos retorno informacion sobre las ultimas publicaciones esto se guardo en MongoDB de manera local

 Para tiktok-scraper es necesario ejecutar los comandos:
  
   - Iniciará el scraper mediante npm
   
   **npm i -g tiktok-scraper**
  
  - Hecho esto basta ejecutar el comando con los parametros siguientes para que nos genere un CSV:

  Usuario 1: **tiktok-scraper user stamkkk -t csv**
  
   ![image](https://user-images.githubusercontent.com/58191417/127723791-fa78aeb3-1623-4f02-a9df-1d7ad53d14b8.png)

  Usuario 2: **tiktok-scraper user dannapaola -t csv**
  
  ![image](https://user-images.githubusercontent.com/58191417/127723799-bed0bef6-23c3-4d78-9bde-e6cb5fdfb65c.png)
  
  Para importar el CSV a MySQL verificamos los pasos:
  
  ![image](https://user-images.githubusercontent.com/58191417/127723817-c9370ae0-b59f-46c4-a84b-14c1ec0d7b40.png)

  ![image](https://user-images.githubusercontent.com/58191417/127723822-67755cdf-44e6-4ec4-9563-9b238c4d49d1.png) 
  
  ![image](https://user-images.githubusercontent.com/58191417/127723828-3877d95e-6dd4-44da-8489-9c66c18b9a54.png)

  Comprobamos que la BD se haya insertar de manera correcta (por la extensión de la misma, solo se adjuntan capturas que comprueben el hecho)
  
  ![image](https://user-images.githubusercontent.com/58191417/127723855-b0076644-5b7b-498a-9cc9-09e419f06941.png)

  ![image](https://user-images.githubusercontent.com/58191417/127723859-bfe04f9f-8cb8-4462-baf6-60ee16ad3534.png)

  ![image](https://user-images.githubusercontent.com/58191417/127723863-d5f270fc-1040-45d8-8a86-52a69f89ae2d.png)

  ###### Mismo proceso para el otro usuario:
  
  ![image](https://user-images.githubusercontent.com/58191417/127723874-9c72810a-5026-4941-a83d-7fe2691922dd.png)

  ![image](https://user-images.githubusercontent.com/58191417/127723877-8c22e9eb-1b54-4c7c-8093-06ecd0dd6119.png)

  ![image](https://user-images.githubusercontent.com/58191417/127723881-8ab70164-2585-4e90-9e90-a266808dbed5.png)

  Comprobamos:
  
  ![image](https://user-images.githubusercontent.com/58191417/127723892-a2f71e6d-f919-4f84-b48a-08c3e4077864.png)

  ![image](https://user-images.githubusercontent.com/58191417/127723897-869d0652-5cdc-493e-a939-bed49523b494.png)

  ![image](https://user-images.githubusercontent.com/58191417/127723905-0a854b54-f6a1-4c41-b58a-48383d509835.png)

## 6) MySQL => MongoDB

  Para migrar de MySQL a MongoDB es ncesario exportar las BD de MySQL
  
  ![image](https://user-images.githubusercontent.com/58191417/127724379-d4966180-5ce1-437a-904d-dda19e704cb8.png)

  - Al hacer esto se generará un JSON
  
  ![image](https://user-images.githubusercontent.com/58191417/127724395-53f053c6-db85-4860-807f-9ab9a4f8a060.png)

  - En MongoDB Compass creamos la BD tiktok y la colección para la primera BD (dannapaola)
  
  ![image](https://user-images.githubusercontent.com/58191417/127724447-7b41c8c3-683f-4312-bf9f-0adca0355206.png)

  - Importamos el archivo JSON generados anteriormente:
  
  ![image](https://user-images.githubusercontent.com/58191417/127724476-c6c35c0b-e8a6-4345-8e10-b879cdffaf00.png)

  ![image](https://user-images.githubusercontent.com/58191417/127724479-75760779-a50c-4c79-b216-dbe59e17872e.png)

  - Comprobamos que la importación se realizó con exito:
  
  ![image](https://user-images.githubusercontent.com/58191417/127724501-9183a388-4528-42bc-9a77-946460cacd4e.png)

  ![image](https://user-images.githubusercontent.com/58191417/127724505-5eefb428-8937-4d2e-a503-74cb53f4fde7.png)

  **Repetimos los mismos pasos para la otra BD (stamkkk):**
  
  ![image](https://user-images.githubusercontent.com/58191417/127724559-40b38405-cc5c-4385-af96-ccaef9e4805b.png)

  ![image](https://user-images.githubusercontent.com/58191417/127724565-4f5d5125-a502-4c7e-81f6-571b943db681.png)

  ![image](https://user-images.githubusercontent.com/58191417/127724528-0c9d8136-6a52-46e2-8f9c-87040bfd6136.png)

  ![image](https://user-images.githubusercontent.com/58191417/127724535-e7adc039-0f7c-47b8-be0d-76f6dea6507c.png)

  ![image](https://user-images.githubusercontent.com/58191417/127724552-c72763ab-942e-43d0-ac34-905d6c191e81.png)

  ![image](https://user-images.githubusercontent.com/58191417/127724537-549679ac-33a2-46d8-9a8f-9367f557ff18.png)

## 3) Web Scrapping
   
  Se importan las librerías necesarias, en este caso Pymongo:
  
  ![image](https://user-images.githubusercontent.com/58191417/127725140-8ce5a1e3-997a-4917-8837-d722d09c8338.png)
   
   Se definen las funciones que serviran para la busqueda:
   
   ![image](https://user-images.githubusercontent.com/58191417/127725163-3f3e9609-4102-40b0-98a0-7fb00c0b7d29.png)

  Con la ayuda de BeatifulSoup se filtra y además se crean los contenedores:
  
  ![image](https://user-images.githubusercontent.com/58191417/127725191-772b058c-1858-4113-b0ec-9710894fba95.png)
  
  Finalmente se limpia el código HTML por ultima vez y se conecta con el cliente de MongoDB para guardar los datos:
  
  ![image](https://user-images.githubusercontent.com/58191417/127725216-284558fc-c9b0-4fcc-b046-3e7268d2b5c8.png)

  Se crea la BD en MongoDB Compass correctamente:
  
  ![image](https://user-images.githubusercontent.com/58191417/127725076-c842b885-0e4f-4373-9cef-424ad5cb2d52.png)

  - Se ha creado la colección:
  
  ![image](https://user-images.githubusercontent.com/58191417/127725102-e4bddc68-7d1d-47cb-8fc5-c43393231bd4.png)

  - Se presenta cada objeto nuevo de la colección:

  ![image](https://user-images.githubusercontent.com/58191417/127725116-0f347ea4-9799-4859-969f-64b85e6e5fb4.png)

