from bs4 import BeautifulSoup
import threading
import requests
import codecs
import urllib
import sys
import re


# En los atributos de la clase usamos dos atributos por instancia. Uno hace referencia al atributo y otro
# a un control de asceso para que no haya problemas al haber varios hilos intentando asceder al atributo.

# Lista_busqueda es un atributo que sirve para recoger los resultados de las busquedas.
lista_busquedas = list()
lock_lista_busquedas = threading.Lock()

# Lista_subusqueda es un atributo que sirve para recoger los resultados de las busquedas avanzadas dentro de las
# paginas web.
lista_subusquedas = list()
lock_lista_subusquedas = threading.Lock()


# La clase spider_web sirve para extraer informacion de las URL que le pasemos como parametro al constructor.
# Dentro de la clase encontraremos diferentes funciones para tratar la informacion.
class spider_web(threading.Thread):
    # Este es el constructor de la clase.
    # Le pasamos los siguientes parametro que nos sirve para crear los siguientes atributos:
    #    - URL: Nos sirve para establecer de que pagina web vamos a extraer la informacion.
    #    - Filtro: Indica cual es el filtro por el cual hemos encontrado la pagina. Sirve para organizar la informacion.
    #    - Lista_filstros: Indica una lista de filtros avanzados para hacer subusquedas.

    #    - E: Indica el nivel actual de subusqueda. Por defecto es 0.
    #    - E_max: Indica el nivel maximo de niveles de subusquedas. Por defecto es 2.
    #    - Subtitulo: Indica si la busqueda es derivada de otra, aqui se guarda ese titulo. Por defecto esta vacio.
    #
    # Tambien tenemos los siguientes atributos que no hemos mencionado.
    #    - Titulo: Indica el titulo de la pagina web de la que hemos sacado la informacion. Sirve para ordenar.
    #    - Source: Aqui se guarda todo el HTML de la pagina web en la que estamos recolectando informacion.
    def __init__(self, url, filtro, lista_filtros, e=0, e_max=2, subtitulo='base', html_crear=False):
        super().__init__()

        self.url = url
        self.base_url = self.extractor_base_url(url)
        self.filtro = filtro
        self.lista_filtros = lista_filtros
        self.e_max = e_max
        self.e = e
        self.subtitulo = subtitulo
        self.html_crear = html_crear
        self.source = self.creador_source()

        try:
            self.titulo = self.source.find("title").text
        except:
            self.titulo = self.url

    # Esta funcion nos sirve para sacar la informacion HTML de la pagina objetivo.
    # La URL se pasa mediante el atributo self.url, creada desde el constructor.
    def creador_source(self):
        # La variable "dict_error" simplemente es una variable que se usa cuando la busqueda da algun tipo de error.
        # Su contenido es igual que un diccionario normal que se añadiria a "lsita_subusquedas"
        # pero añadiendo otro titulo.
        dict_error = {"filtro": self.filtro, "url": self.url, "incidencias": list(), "subtitulo": self.subtitulo,
                      "html": ""}

        # Este control de exepciones controla que no haya errores de esquema, ni de SSL ni otro tipo de errores en la
        # pagina. Los errores pueden ser los siguientes:
        #     - Esquema: BeatifulSoup no puede recuperar el esquema de la pagina debido a un error en la URL.
        #     - SSL: Se trata de un error de verificacion en la pagina web a la que se intenta acceder y debido a esto
        #            no lo consigue.
        #     - Otros: Pueden haber errores por otros temas, debido a que no se desea romper la experiencia
        #              de usuario con errores, por lo tanto simplemente se agrega el nombre del error pero
        #              no se quita la URL por si desea vistarla a mano.
        try:
            source = requests.get(self.url).text
            return BeautifulSoup(source, 'lxml')

        except requests.exceptions.MissingSchema:
            dict_error["titulo"] = "Error de esquema."
            lista_subusquedas.append(dict_error)
            return 0

        except requests.exceptions.SSLError:
            dict_error["titulo"] = "Error de SSL."
            lista_subusquedas.append(dict_error)
            return 0

        except:
            dict_error["titulo"] = "Error de " + str(sys.exc_info()[0]) + "."
            lista_subusquedas.append(dict_error)
            return 0


    # Esta funcion nos permite sacar la URL basica de una pagina web. Esto nos puede servir, por ejemplo, para añdirlo
    # al principio de una URL relativa y seguir navegando por las paginas web derivadas.
    def extractor_base_url(self, url):
        # El metodo para extraer la URL basica es encontrar el primer caracter "/" despues del dominio.
        # Por ejemplo, si deseamos sacar la URL basica de esta URL: "https://www.tiendaonline/Articulos":
        #     - 1º. Nos posicionamos en el dominio desde el primer punto, que es "tiendaonline.com/Articulos".
        #     - 2º. Nos posicionamos en el caracter "/", que seria "Articulos".
        #     - 3º. Retornamos un substring con el contenido desde el inicio hasta la barra, restandole 1 para quitar la
        #           barra. El valor retornado seria: "https://www.tiendaonline" que equivale al dominio de la web.
        index_punto = url.find('.')
        index_barra = url.find('/', index_punto - 1)
        return url[:index_barra]

    # Esta funcion sirve para poner la informacion en un archivo de texto, dentro de una carpeta con el nombre del
    # filtro del que fue sacada la URL.
    def coger_html(self, dict_subusquedas):
        # Lo primero que tenemos que hacer es saber si el archivo que vamos a almacenar existe.
        # Para eso llamamos al metodo "existe_archivo" y lo almacenamos en la variable "existe".
        #
        # Despues lo pasamos por un condicional para saber si existe o no.
        # Si existe, guardamos el archivo.
        # Si no existe, termina el metodo.
        global lista_subusquedas
        global lock_lista_subusquedas

        html = ''

        if self.html_crear:
            # Para guardar el archivo lo primero que vamos a hacer es usar el metodo "pettryfy" de BS4 para
            #  almacenar el HTML de la pagina web de una forma facil de leer.
            #
            # Despues de eso, creamos la ruta donde vamos a crear el archivo y lo abrimos con una codificacion
            # UTF-8 para poder leer caracteres especiales y la capacidad de sobrescribir el archivo.
            # Al finalizar lo cerramos correctamente para evitar errores.
            search_source = self.source.prettify()
            html = codecs.open('', 'w', 'utf-8')
            html.write(search_source)
            html.close()

        dict_subusquedas['html'] = html

        lock_lista_subusquedas.acquire()
        lista_subusquedas.append(dict_subusquedas)
        lock_lista_subusquedas.release()

    # Este metodo nos permite buscar, mediante una lista de filtros, informacion especifica y enlaces de interes de
    # cada una de las paginas web que hemos logrado encontrar.
    def busqueda_avanzada(self):
        # Lo primero que hacemos es establecer las variables globales referentes a las subusquedas.
        # Tambien establecemos las siguientes variables para poder almacenar y gestionar la informacion:
        #     - Lista_etiquetas_busqueda: Sirve para establecer por las etiquetas HTML por donde vamos a buscar
        #                                 las subusquedas.
        #     - Lista_incidencias: Sirve para almacenar cuando se encuentre una etiqueta con el dato que buscamos.
        #     - Lista_diccionario_enlaces: Sirve para almacenar una lista de diccionarios con las siguientes etiquetas:
        #                                  - Filtro: Nos sirve para establecer mediante que filtro se ha conseguido
        #                                            la informacion.
        #                                  - Enlace: Lista con los enlaces que han conseguido recopilar.
        global lista_subusquedas
        global lock_lista_busquedas

        lista_etiquetas_busqueda = ['p', 'a', 'span', re.compile('^h\d')]
        lista_incidencias = list()
        lista_diccionario_enlaces = list()
        dict_subusquedas = dict()
        # Ahora debemos buscar por cada filtro coincidencias en la pagina. Para ello usamos el siguiente codigo.
        # Una vez extraemos un filtro de la lista, debemos crear las siguientes variables.
        #     - Diccionario_enlaces: Sirve para guardar la lista de enlaces referentes al filtro correspondiente.
        #                             Dentro de él se guarda el nombre del filtro y la url.
        #     - Lista_enlaces: Lista que almacena los enlaces que vayamos recopilando de HTML.
        # Una vez creados lo primero que hacemos es inicializarlo guardando el filtro al que se hace referencia
        # y una lista vacia que posteriormente se rellenara con la variable "lista enlaces".
        #
        # Mediante un condicional revisamos si encuentra o no alguna coincidencai en la pagina.
        # Si no encuentra ninguno, acaba la revision y prosigue con el siguiente filtro.
        #
        # Cuando encuentre una coincidencia lo guarda en una variable llamada "incidencias" que almacena
        # las coincidencias que encuentre en la pagina web. Despues de eso inicia un recorrido por cada
        # coincidencia que recoja.
        #
        # Una vez dentro, guarda cada incidencia en una variable llamda "lsita_incidencias" y revisa
        # si esa etiqueta tiene o es una etiqueta "a", que es la que suele tener enlaces a otras paginas.
        # Si encuentra una etiqueta "a" saca el atributo "href" que es donde esta la URL.
        #
        # Una vez extraido el atributo "href" analizamos si su primer caracter es un caracter "/".
        # Si es un caracter "/" debemos ponerle la URL base de la pagina web mediante el atributo "base_url"
        # que esta anteriormente explicado en el constructor. Despues la almacenamos en la variable "lista_enlaces".
        # Si no lo encuentra, simplemente almacenamos la URL resultante en la variable "lista_enlaces".
        #
        # Una vez almacenados los enlaces, debemos almacenar la variable "lista_enlaces" en la variable
        # "diccionario_enlaces" en la clave "enclaces".
        #
        # Cuando terminemos la ejecucion del primer condicional almecanamos la variable "diccionario_enlaces" en
        # la variable "lista_diccionario_enlaces". Sin importar que este vacio o no.
        for filtro in self.lista_filtros:
            diccionario_enlaces = dict()
            lista_enlaces = list()
            diccionario_enlaces["filtro"] = filtro
            diccionario_enlaces["enlaces"] = list()
            if self.source.find(lista_etiquetas_busqueda, text=re.compile(filtro)) or \
                    self.source.find(lista_etiquetas_busqueda, text=re.compile(filtro.lower())) or \
                    self.source.find(lista_etiquetas_busqueda, text=re.compile(filtro.upper())) or \
                    self.source.find(lista_etiquetas_busqueda, text=re.compile(filtro.capitalize())):
                if self.source.find(lista_etiquetas_busqueda, text=re.compile(filtro.lower())):
                    incidencias = self.source.find_all(lista_etiquetas_busqueda, text=re.compile(filtro.lower()))
                elif self.source.find(lista_etiquetas_busqueda, text=re.compile(filtro.upper())):
                    incidencias = self.source.find_all(lista_etiquetas_busqueda, text=re.compile(filtro.upper()))
                elif self.source.find(lista_etiquetas_busqueda, text=re.compile(filtro.capitalize())):
                    incidencias = self.source.find_all(lista_etiquetas_busqueda, text=re.compile(filtro.capitalize()))
                else:
                    incidencias = self.source.find_all(lista_etiquetas_busqueda, text=re.compile(filtro))
                for incide in incidencias:
                    lista_incidencias.append(incide)
                    if incide.get('href'):
                        enlace = incide.get('href')
                        if enlace[0:1].find('/'):
                            lista_enlaces.append(enlace)
                        else:
                            lista_enlaces.append(self.base_url + enlace)
                diccionario_enlaces["enlaces"] = lista_enlaces
            lista_diccionario_enlaces.append(diccionario_enlaces)

        # Incrementamos el valor de la recursividad en 1.
        self.e = self.e + 1
        # Almacenamos en un diccionario la subusqueda actual los atributos titulo, url, incidencias y subtitulo.
        # Si queremos asceder a la informacion de extraigamos de forma general, este es el mejor metodo.
        #
        # Despues la almacenamos en la variable global "lista_subusquedas" y como es una variable global
        # le ponemos un control de acceso mediante su propio candado.
        dict_subusquedas["filtro"] = self.filtro
        dict_subusquedas["titulo"] = self.titulo
        dict_subusquedas["url"] = self.url
        dict_subusquedas["incidencias"] = lista_incidencias
        dict_subusquedas["subtitulo"] = self.subtitulo

        # Ahora, una vez que hemos extraido las URL, debemos crear más hilos del objeto "spider_web" para
        # analizar las url que hemos extraido. El procedimiento es el mismo que en las otras creaciones de hilos.
        # Solo cambia los atributos que se le pasan al objeto.
        hilos_enlaces = list()

        for diccionario in lista_diccionario_enlaces:
            for i, enlace in enumerate(diccionario["enlaces"]):
                # El objeto "spider_web" tenemos que pasarle los siguientes parametros:
                #     - Filtro: Misma funcion que su homologo.
                #     - Lista_filtros: Misma funcion que su homologo.
                #     - E: Indica el nivel de recursividad en el que nos encontramos.
                #     - E_max: Indica el nivel maximo de recursividad al que queremos llegar. Lo enviamos por si
                #             si se ha personalizado cuando se ha iniciado la primera ejecucion del objeto.
                #     - Subtitulo: Indica cual es el filtro avanzado por el cual hemos conseguido la pagina.
                hilo = spider_web(enlace, self.filtro, self.lista_filtros, e=self.e, e_max=self.e_max,
                                  subtitulo=diccionario["filtro"], html_crear=self.html_crear)
                hilos_enlaces.append(hilo)
                hilos_enlaces[i].start()

        for hilo in hilos_enlaces:
            while hilo.is_alive():
                pass

        # Una vez terminanos toda la ejecucion, guardamos el HTML.
        self.coger_html(dict_subusquedas)

    # La funcion "run" es un metodo basico de los hilos que nos permite iniciar la ejecucion de la clase.
    def run(self):
        # Como hemos creador un hilo recursivo tenemos que establecer cual es el limite de veces que se tiene que repetir.
        # Establecemos esto mediante una comprobacion, el cual si ya ha llegado a su limite, simplemente termina la
        # ejecucion del hilo.
        if self.e_max > self.e and type(self.source) != int:
            self.busqueda_avanzada()


# La clase google_spider_search nos permite extraer los titulos y las URL de una busqueda de google de numero
# de resultados que queramos. Esto nos sirve a posteriori para analizar los enlaces y sacar informacion de los HTML.
class google_spider_search(threading.Thread):
    # Este es el constructor de la clase.
    # Le pasamos los siguinetes parametros al constructor:
    #   - Filtro: Indica cual es el filtro por el cual iniciar la busqueda en el motor de busqueda Google.
    #   - num_busquedas: Indica el numero de resultados que vamos a cojer. Tiene un valor por defecto de 10. (1º Pagina)
    #   - epg: Indica parametros de busqueda extra mediante and.
    #   - op: Indica parametros de busqueda extra mediante or.
    #   - exclusion: Indica que palabras queremos excluir de la busqueda.
    #   - lengua: Indica en que idioma queremos que esten las paginas web que estamos buscando.
    #   - pais: Indica en que pais queremos que esten localizadas las busquedas.
    #   - dominio: Indica sobre que demonios queremos buscar.
    #   - dominio_relacionado: Indica sobre que dominio quieres que Google busque pensando sobre dominios relacionados
    #                          con el que se indica.
    #   - dominio_enlazado: Indica sobre que dominio quieres que Google busque en sitio que enlazan con ese dominio.
    #   - extension: Indica en que extension buscar archivos en Google.
    #   - fecha: Indica un limite de fecha en la cual se pretende buscar.
    #
    # Casi todos los parametros son por defecto cadenas vacias por que buscamos crear una url personalizada
    # posteriormente y gracias a esto podemos crearla sin problemas.
    def __init__(self, filtro, num_busquedas='10', epq='', op='', exclusion='', lengua='', pais='', dominio='',
                 dominio_rel='', dominio_enl='', extension='', fecha=''):
        # Las variables del constructor son las siguientes:
        #     - filtro: Sirve para indicar el filtro de busqueda y ademas el nombre de algunos archivos.
        #     - extension_google: Es un diccionario que sirve para poner los parametros de busqueda extra por
        #                         los que queramos buscar.
        #     - url: Nos sirve para almacenar la url por la cual vamos a buscar en Google. Esta se construye en base
        #            a los parametros del constructor mediante la funcion "creador_url"
        #
        # El diccionario tiene los mismos nombres que los parametros que pasamos al constructor, para más informacion
        # consulte el constructor.
        super().__init__()
        self.filtro = filtro
        self.extension_google = {
            'base_url': 'http://www.google.com/',
            'google_search': 'search?q=',
            'google_and': '&as_epq=',
            'google_or': '&as_oq=',
            'google_exclusion': '&as_eq=',
            'google_lengua': '&lr=lang_',
            'google_pais': '&cr=county',
            'google_dominio': '&as_sitesearch=',
            'google_dominio_relacionado': '&as_rq=',
            'google_dominio_enlazados': '&as_lq=',
            'google_extension': '&as_filetype=',
            'google_fecha': '&as_qdr=',
            'google_num': '&num='
        }

        self.url = self.creador_url(filtro, num_busquedas, epq, op, exclusion, lengua, pais, dominio,
                                    dominio_rel, dominio_enl, extension, fecha)

        # Iniciamos la recoleccion del HTML y buscamos todos las etiquetas "h3".
        # Estas etiquetas contienen el titulo y la url de la busqueda.
        self.search_source = self.creador_source().find_all('h3')

    # Esta funcion nos sirve para sacar la informacion HTML de la pagina objetivo.
    # La URL se pasa mediante el atributo self.url, creada desde el constructor.
    def creador_source(self):
        source = requests.get(self.url).text
        return BeautifulSoup(source, 'lxml')

    # Esta funcion nos sirve para crear la url por la que vamos a buscar en google.
    # Esta url es completamente personalizada y depende de los datos que le pasamos al constructor debido a que sirven
    # esencialmente para esta funcion.
    def creador_url(self, filtro, num_busquedas, epq, op, exclusion, lengua, pais, dominio,
                    dominio_rel, dominio_enl, extension, fecha):
        # Creamos una variable url que va añadiendo las incrementaciones segun los parametros de busqueda.
        # Aumenticamente añadimos la base del bsucador, el filtro y el numero de busquedas que queremos buscar.
        url = self.extension_google['base_url']
        url += self.extension_google['google_search'] + filtro
        url += self.extension_google['google_num'] + str(num_busquedas)

        # El siguiente condicional lo unico que hace es revisar que cadenas estan vacias para poder introducir
        # los criterios de busqueda en la url. Si las cadenas no estan vacias, lo añade a la url.
        if epq != '':
            url += self.extension_google['google_and'] + epq
        if op != '':
            url += self.extension_google['google_exclusion'] + exclusion
        if lengua != '':
            url += self.extension_google['google_lengua'] + lengua
        if pais != '':
            url += self.extension_google['google_pais'] + pais
        if dominio != '':
            url += self.extension_google['google_dominio'] + dominio
        if dominio_rel != '':
            url += self.extension_google['google_dominio_relacionado'] + dominio_rel
        if dominio_enl != '':
            url += self.extension_google['google_dominio_enlazados'] + dominio_enl
        if extension != '':
            url += self.extension_google['google_extension'] + extension
        if fecha != '':
            url += self.extension_google['google_fecha'] + fecha

        return url

    # El metodo "run" es un metodo basico de los hilos que nos permite iniciar la ejecucion de la clase.
    def run(self):
        # Establecemos el atributo global "lista_busqueda" y su controlador de acceso para ir añadiendo las URL
        # que vayamos encontrando.
        global lista_busquedas
        global lock_lista_busquedas

        # Inicializamos el diccionario con las claves de filtro y urls.
        #     - Filtro: Nos servira para situar el filtro de busqueda.
        #     - Urls: Nos sirve para poner una lista de diccionarios que contienen los titulos y
        #             las urls de la busqueda.
        #
        # Tambien inciiamos una lista de diccionarios que nos permitira hacer la recoleccion de los diccionarios
        # anteriormente creados.
        diccionario_spider = {'filtro': self.filtro, 'urls': list()}
        lista_diccionario_busqueda = list()

        # Recorremos el resultado de la recopilacion de etiquetas y empezamos a tratar la informacion.
        for element in self.search_source:
            # Creamos las variables vacias para recopilar y ordenar la informacion.
            #     - diaccionario_busqueda: Sirve para colocar el titulo y la url que necesitamos extraer.
            #     - titulo: Es la variable vacia para colocar el titulo y saber si devuelve nulo o no.
            #     - url: Es la variable vacia para colocar la url y saber si devuelve nulo o no.
            diccionario_busqueda = dict()
            titulo = ''
            url = ''

            # Usamos un metodo de exepciones para evitar errores imprevistos, como por ejemplo que no se pueda
            # extraer un titulo o una url de los campos que hemos seleccionado.
            try:
                # Extraemos el texto de la etiqueta, este texto equivale al titulo.
                titulo = str(element.a.text)

                # Extraemos el url de la etiqueta "a" y del parametro "href". Tambien descodificamos la url para
                # evitar problemas con ciertas partes de los urls.
                # Por ejemplo los "=" o "?" se suelen codificar, asi los descodificamos y podemos analizarlas con
                # mayor facilidad
                url = urllib.parse.unquote(element.a["href"])

                # Aqui tratamos la url para que sea lo más clara posible para el programa.
                # Es importante hacer esto debido a que las url sacadas de la etiqueta "a" tienen ruido y no queremos
                # que eso interfiera en el analisis.
                #
                # La primera parte del tratamiento es descubrir si en realidad es una sentencia de busqueda como de por
                # ejemplo google Imagenes, Noticias, etc. En ese caso lo que tenemos que hacer es añadir la url base
                # de google a la url. El añadido de coger a partir de la 1º letra, es para evitar que el caracter "/"
                # este varias veces por url. Esto puede crear problemas
                #
                # En el caso de que no sea una sentencia de busqueda, lo que necesitamos es quitar el ruido de la url.
                # Necesitamos coger toda la url base, que es aquella que este precedida por el apartado "/url?q=" y
                # antecedido por "&sa".
                #
                # Para ello, remplazamos el apartado de "/url?q=" por una cadena vacia y separamos el contenido de la
                # url en una lista separada por la cadena "&sa". Acto seguido cogemos la 1º posicion que es la url base.
                if url.find('/search?q') != -1:
                    url = self.extension_google['base_url'] + url[1:]
                else:
                    url = url.replace('/url?q=', '').split('&sa')[0]

            except AttributeError:
                pass

            # Cuando terminamos de limpiar la URL y analizar la etiqueta "h3". Procedemos a ver si los campos
            # no son nulos. Si estos no son nulos, los almacenamos en un diccionario para ordenarlo.
            if (titulo != '') and (url != ''):
                diccionario_busqueda['titulo'] = titulo
                diccionario_busqueda['url'] = url
                lista_diccionario_busqueda.append(diccionario_busqueda)

        # Cuando terminamos de ordenar todas las url con sus titulos. Introducimos la lista de diccionarios en la clave
        # de "urls" y lo introducimos en el atributo lista_busqueda para su posterior procesamiento.
        # Este atributo, al ser global, nos interesa que haya un control de asceso.
        # Para este control usamos el metodo acquire, que sirve para bloquear el asceso, y release, que sirve
        # para liberar el asceso.
        diccionario_spider['urls'] = lista_diccionario_busqueda
        lock_lista_busquedas.acquire()
        lista_busquedas.append(diccionario_spider)
        lock_lista_busquedas.release()


# Esta funcion solamente inicia el proceso de recoleccion y tratamiento de los datos.
def iniciador(filtro, lista_filtros_avanzados=list(), bus_and='', bus_or='', bus_exclusiones='',
              bus_dominio='', bus_dominio_rel='', bus_dominio_enl='', bus_extension='', bus_fecha='', bus_idioma='',
              bus_pais='', bus_profundidad=2, bus_busquedas='', html_crear=False):
    global lista_busquedas
    global lista_subusquedas

    lista_busquedas = list()
    lista_subusquedas = list()

    busqueda_principal = google_spider_search(filtro, epq=bus_and, op=bus_or, exclusion=bus_exclusiones,
                                              dominio=bus_dominio, dominio_rel=bus_dominio_rel,
                                              dominio_enl=bus_dominio_enl, extension=bus_extension, fecha=bus_fecha,
                                              lengua=bus_idioma, pais=bus_pais, num_busquedas=bus_busquedas)
    busqueda_principal.start()

    # Es importante añadir que no continue la ejecucion de la siguiente parte del codigo hasta que todos los hilos
    # anteriores terminen su ejecucion, por ello usamos el metodo de "is_alive" que devuelve el valor True si el hilo
    # esta en ejecucion. Eso permite que si lo aislamos en un bucle while paremos la ejcucion del programa base hasta
    # que terminen de ejecutarse los hilos.
    while busqueda_principal.is_alive():
        pass

    # Esta lista vacia sirve para almacenar los hilos que vayamos creando.
    hilos_busqueda = list()

    # Lo que hacemos en este bucle es crear hilos, almacenarlos en la lista que almacena los hilos y ejecutarlos.
    # Este bucle recoge la informacion de la lista "busqueda".
    if lista_filtros_avanzados:
        for i, busq in enumerate(lista_busquedas):
            hilos_busqueda = list()
            filtro = busq['filtro']

            for i, url in enumerate(busq['urls']):
                hilo = spider_web(url['url'], filtro, lista_filtros_avanzados, e_max=bus_profundidad,
                                  html_crear=html_crear)
                hilos_busqueda.append(hilo)
                hilos_busqueda[i].start()

    # El proposito de esta ejecucion es la misma que la anterior.
    for hilo in hilos_busqueda:
        while hilo.is_alive():
            pass

    return {'lista_busquedas': lista_busquedas, 'lista_subusquedas': lista_subusquedas}
