# Prueba Tecnica 1

Crea un script de extracción, para el menú de despensa del sitio. Incluir Dockerfile
https://www.soriana.com/

## Instalación

Instalar librerias que estan dentro del archivo requirements.txt

## Uso

Una ve instalados los requerimientos, entrar al directorio en donde
se encuentra nuestro WebScraper ws_soriana.py 
(extraccion/extraccion/spiders/ws_soriana.pyextraccion/extraccion/spiders/ws_soriana.py)

Una vez que nos ubicamos dentro de la carpeta, ejecutar el comando:

```cmd
scrapy crawl ws_soriana
```

Realizado esto, podremos observar el funcionamiento completo del Scrapers

## Notas importantes / Observaciones

#### Rotacion de Agentes de Usuario

Se optó por usar la libreria 

```cmd
random_user_agent
```

debido a que podemos usar diferentes tipos de
agentes de usuario que se pueden utilizar para evitar
una deteccion temprana del bot, con esta libreria
podemos seleccionar el tipo de navegador, sistema operativo
y el numero total de agentes de usuario que queremos obtener, de los cuales
solo uno de forma aleatoria se va a elegir cada que inicie un nuevo flujo.

Como nota extra, para evitar una deteccion temprana del bot o baneo,
se puede realizar una rotacion de proxys.

# Librerias utilizadas

- Scrapy
- random-user-agent