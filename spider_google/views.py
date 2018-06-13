import datetime
from django.shortcuts import render
from spider_google.forms import buscador_googleForm
from spider_google.classes.google_spider import iniciador
from spider_google.models import spider_html, spider_html_incidencia

from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse

# "Context_temp" es un atributo que sirve para intercambiar informacion entre la vista que busca toda la informacion
# del spider con el creador de PDF.
context_temp = {'indice_list': '', 'incidencias_list': ''}

# El metodo "separador_url" nos permite separar la url para que se pueda introducir en una celda de una
# tabla sin problemas en su longitud.
# Sus parametro es:
#     - url: Indica cual es string al que se le desea introducir los separadores.
def separador_url(url):
    # Se crean 4 variables con diferentes funciones:
    #     - url_form: Es la URL con los cambios pertinentes en un formato exacto.
    #     - url_indice: Indica por que indice va el separado de la url.
    #     - continuar: Sirve para indicar al futuro bucle "while" cuando hay que terminar el bucle.
    url_form = ''
    url_indice = 40
    continuar = True

    # El bucle while se compone por la funcionalidad que se le da desde la variable "continuar".
    # Su funcionalidad es la siguiente:
    #     1º. Comprueba que la longitud de la url es mayor que el indice para saber si se tiene que seguir separnado.
    #     Caso "Es mayor":
    #         1.1º. Añade a "url_form" un subtring que comprende desde el indice restado 40 hasta el indice actual.
    #               Este substring es exactamente un trozo de 40 caracteres a la que acto seguido se le añade un espacio
    #               para establecer el separador.
    #         1.2º. Suma a "url_indice" el numero 40 para establecer el siguiente la siguiente iteracion del bucle.
    #
    #     Caso "Es menor":
    #         2.1º. Establece la variable "continuar" como False para que el bucle no siga itinerando.
    #         2.2º. Añade la ultima franja del url deseado que comprende desde el ultimo indice menos 40 hasta
    #               el final de la string.
    #
    # Un ejemplo claro es que si la URL tiene menos de 40 caracteres en su direccion, simplemente cogera desde
    # el inicio hasta el final del string, osease, toda la direccion completa.
    while continuar:
        if url_indice <= len(url):
            url_form += url[url_indice - 40:url_indice] + ' '
            url_indice += 40
        else:
            continuar = False
            url_form += url[url_indice - 40:]
    return url_form

# La funcion "render_to_pdf" nos permite pasar un HTML que cree Django a un archivo PDF descargable y mostrado por web.
# Los parametros son los siguientes:
#     - path: Es la ruta al HTML que se va a usar para la creacion del PDF.
#     - params: Es basicamente los parametros que usara Django en el contexto para crear el PDF.
def render_to_pdf(path, params):
    # Se crean variables para establecer las opciones necesarias para ejecutar el proceso:
    #     - template: Indica cual es el codigo HTML que se va a seguir. Se usa el parametro "path" para indicarselo.
    #     - html: Aqui se renderiza la plantilla mediante la variable "template". El parametro que se le pasa
    #             es el contexto que se usara en la pagina para establecer el contenido.
    #     - response: Se trata del tipo de datos que se incluira en el PDF, es algo obligatorio y propio del modulo usado.
    #     - pdf: Es la conversion del HTML al PDF. Usamos codificacion "UTL-8" para que se puedan mostrar todos
    #            los caracteres españoles a la hora de mostrarlo.
    template = get_template(path)
    html = template.render(params)
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), dest=response)

    # El siguiente condicional simplemente enlaza a diferentes HTML si se produce un error a la hora de crear el PDF.
    # En el caso de que no haya error, te redireccionara a la pagina del PDF.
    # En caso contrario, simplemente mostrara una pagina de error.
    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error Rendering PDF", status=400)

# Create your views here.

# La vista "index_spider_view" nos lleva directamente al formulario donde se va a producir toda la aplicacion.
# Aqui principalmente va a haber un formulario que tendremos que rellenar para obtener resultados.
def index_spider_view(request):
    # Lo primero que hacemos es agarrar el contenido de la variable "context_temp" para establecerla más adelante.
    global context_temp

    # Lo primero que hacemos es saber si ha habido una peticion POST en nuestro formulario.
    if request.method == "POST":
        # Cargamos el formualrio relleno por POST y despues miramos si es o no valido.
        buscador_Form = buscador_googleForm(request.POST)

        if buscador_Form.is_valid():
            # Acto seguido sabemos que el formulario es valido, cargamos todo los datos del formulario en diferentes
            # variables. Estas variables nos serviran para pasar los datos al spider y poder realizar la busqueda
            # personalizada de Google.
            cd_bus = buscador_Form.cleaned_data

            buscador_form = cd_bus['barra_buscador']
            and_form = cd_bus['bus_and']
            or_form = cd_bus['bus_or'].replace('\n', '').replace(',', '+')[:-1]
            exclusion_form = cd_bus['bus_exclusion'].replace('\n', '').replace(',', '+')[:-1]
            dominio_form = cd_bus['bus_dominio']
            dominio_relacionado_form = cd_bus['bus_dominio_relacionado']
            dominio_enlazado_form = cd_bus['bus_dominio_enlazado']
            filtro_avanzado_form = cd_bus['bus_filtro_avanzado'].replace('\n', '').split(',')[:-1]
            extension_archivo_form = cd_bus['bus_extension_archivo']
            fecha_form = cd_bus['bus_fecha']
            idioma_form = cd_bus['bus_idioma']
            pais_form = cd_bus['bus_pais']

            # La mayoria de los campos del formulario en blanco suelen traer informacion que no tiene datos por defecto.
            # Sin embargo, tanto la profundidad de la busqueda, osea la recursividad del spider, como el numero de
            # busquedas que se vayan a ejecutar tienen valores por defecto.
            #
            # Estos valores seran puestos mediante un condicional que busca si estan vacios o no. Al ser un campo
            # del formulario tipo numero, si estan vacios seran "None", que es el "null" de Python.
            if cd_bus['bus_profundidad'] == None:
                profundidad_form = 2
            else:
                profundidad_form = int(cd_bus['bus_profundidad'])

            if cd_bus['bus_num'] == None:
                num_form = 10
            else:
                num_form = int(cd_bus['bus_num'])

            # Creamos una variable que guarde el diccionario que nos vaya a enviar la clase spider_google.
            # Este diccionario tendra principalmente dos elementos:
            #     - lista_subusquedas: Que tiene toda la informacion de las busquedas y subusquedas con las inicencias
            #                          pertinentes.
            #     - lista_busquedas: Que tiene toda la informacion de las busquedas basicas que se generan al buscar
            #                        por Google.
            spider_google_result = iniciador(buscador_form, filtro_avanzado_form, and_form, or_form, exclusion_form,
                                             dominio_form,
                                             dominio_relacionado_form, dominio_enlazado_form, extension_archivo_form,
                                             fecha_form,
                                             idioma_form, pais_form, profundidad_form, num_form)

            # Es importante resaltar que si la lista de subusquedas esta vacia, no mostraria ningun elemento en la pagina
            # de resultados, por eso mismo hemos aplicado un condicional que haga dos funcionalidades diferentes
            # si esta la lista vacia.
            if spider_google_result['lista_subusquedas'] != []:
                # Una vez comprobemos que el elemento "lista_subusquedas" no esta vacio, lo recorremos.
                for ind, info in enumerate(spider_google_result['lista_subusquedas']):
                    # Lo primero que hacemos es introducir los datos dentro de
                    # Las variables son las siguientes:
                    #     - filtro_info: Indica el criterio de busqueda por el cual se ha buscado.
                    #     - titulo_info: Indica el titulo de la pagina web.
                    #     - url_info: Indica la URL de la pagina web que hemos encontrado.
                    #     - url_view: Es la URL que se va a mostar en la tabla. Esta URL tiene una edicion
                    #                 en el string.
                    #     - subtitulo: Indica que tipo de filtro avanzado ha usado para encontrar la pagina web.
                    #     - html_info: Incica el HTML de la pagina que hemos encontrado si hemos elegido
                    #                  la opcion de sacar el HTML de la pagina.
                    filtro_info = info['filtro']
                    titulo_info = info['titulo']
                    url_info = info['url']
                    subtitulo_info = info['subtitulo']
                    html_info = info['html']

                    # Una vez esta todo introducido nos interesa saber si existe ya en la base de datos
                    # la informacion que hemos recolectado. Esto nos sirve para introducirla si no se ha
                    # introducido anteriormente.
                    insercion = spider_html.objects.filter(filtro=filtro_info, subfiltro=subtitulo_info,
                                                            titulo=titulo_info, url=url_info,
                                                            fecha=datetime.datetime.now().strftime(
                                                                '%d-%m-%Y'))
                    existencia = insercion.exists()

                    # En esta parte de la funcionaliad es donde se revisa si existe y si no es asi, se inserta.
                    if not existencia:
                        spider_html(filtro=filtro_info, subfiltro=subtitulo_info, titulo=titulo_info, url=url_info,
                                    html=html_info).save()

                    # Hacemos el mismo proceso anterior con las incidencias:
                    for etiqueta in info['incidencias']:
                        insercion = spider_html.objects.get(filtro=filtro_info, subfiltro=subtitulo_info, titulo=titulo_info,
                                                            url=url_info,
                                                            fecha=datetime.datetime.now().strftime('%d-%m-%Y'))

                        existencia = spider_html_incidencia.objects.filter(spider_html=insercion,
                                                                           incidencia=str(etiqueta)).exists()

                        if not existencia:
                            spider_html_incidencia(spider_html=insercion, incidencia=str(etiqueta)).save()

                    # Como en el anterior creamos las siguientes variables:
                    #     - contexto: Es el diccionario que contiene el contexto de la plantilla que se le va a pasar
                    #                 a la plantilla de resultados.
                    #     - indice_list: Es la lista que contiene todos los indices que saldran en la pagina de resultados.
                    #     - incidencias_lista: Contiene todas las incidencias que se han producido en las paginas en las
                    #                          que hemos buscado. Sin embargo, en esta funcionalidad simplemente sera
                    #                          una lista vacia, por que no puede haber incidencias sin subusquedas.
                    contexto = dict()
                    indice_list = list()
                    incidencias_list = list()
                    for ind, busqueda in enumerate(spider_google_result['lista_subusquedas']):
                        # Inicializamos los siguientes diccionarios:
                        #     - indice_temp: Que guardara los elementos que se vayan a poner en el indice.
                        #     - incidencias_temp: Que guardara los elementos que se vayan a poner en las incidencias.
                        indice_temp = dict()
                        incidencias_temp = dict()

                        # Metemos dentro de la "indice_temp" toda la informacion necesaria para mostrarla en la
                        # plantilla. La informacion es la siguiente:
                        #     - id: Indica el ID del campo que se va a establecer dentro de la plantilla.
                        #     - titulo: Indica el titulo de la pagina web.
                        #     - url: Indica la URL que se va a meter dentro del campo "href" de la tabla.
                        #     - url_view: Es la URL que se va a mostar en la tabla. Esta URL tiene una edicion
                        #                 en el string.
                        #     - subtitulo: Indica que tipo de filtro avanzado ha usado para encontrar la pagina web.
                        indice_temp['id'] = str(ind)
                        indice_temp['titulo'] = busqueda['titulo'].rstrip()
                        indice_temp['url'] = busqueda['url'].rstrip()
                        indice_temp['url_view'] = separador_url(busqueda['url']).rstrip()
                        indice_temp['subtitulo'] = busqueda['subtitulo'].rstrip()

                        # Metemos dentro de la "incidencias_temp" toda la informacion necesaria para mostrarla en la
                        # plantilla. La informacion es la siguiente:
                        #     - id: Indica el ID del campo que se va a establecer dentro de la plantilla.
                        #     - id_ref: Indica el ID de referncia para que el indice pueda llevar a esa etiqueta HTML.
                        #     - titulo: Indica el titulo de la pagina web.
                        #     - id2: Por cuestiones con Django se ha debido de repetir esta parte para crear ciertos elementos
                        #            en la plantilla.
                        #     - indice_list: Indica las incidencias que han encontrado en la pagina web.
                        #     - incidencias: Es una lista con las incidencias que se han encontrado dentro de las paginas web.
                        #                    Funciona mediante los filtros avanzados de busqueda.
                        incidencias_temp['id'] = indice_temp['id'] + "A"
                        incidencias_temp['id_ref'] = indice_temp['id']
                        incidencias_temp['titulo'] = busqueda['titulo'.rstrip()]
                        incidencias_temp['id2'] = incidencias_temp['id']
                        incide_list = list()
                        # Dentro se recorre la lista de incidencias que esta dentro del elemento "list_subusquedas" y
                        # se van insertando en la lista "incide_list".
                        for elemento in busqueda['incidencias']:
                            incide = str(elemento).rstrip()
                            incide_list.append(incide)
                        # Una vez rellenada la lista, esta se introduce dentro del elemento "incidencias".
                        incidencias_temp['incidencias'] = incide_list
                        # Una vez terminado todo el proceso las variables "indice_temp" e "incidencias_temp" se introducen
                        # en las listas "indice_list" e "incidencias_list" respectivamente.
                        indice_list.append(indice_temp)
                        incidencias_list.append(incidencias_temp)

            # En el caso en el que este vacia la "lista_subuquedas" tendremos que revisar el elemento "lista_busquedas".
            else:
                # Como en el anterior creamos las siguientes variables:
                #     - contexto: Es el diccionario que contiene el contexto de la plantilla que se le va a pasar
                #                 a la plantilla de resultados.
                #     - indice_list: Es la lista que contiene todos los indices que saldran en la pagina de resultados.
                #     - incidencias_lista: Contiene todas las incidencias que se han producido en las paginas en las
                #                          que hemos buscado. Sin embargo, en esta funcionalidad simplemente sera
                #                          una lista vacia, por que no puede haber incidencias sin subusquedas.
                contexto = dict()
                indice_list = list()
                incidencias_list = list()

                # Recorremos el interior de el elemento "lista_busquedas".
                # Este diccionario contiene 2 elementos importantes:
                #     - filtro: Indica el criterio de busqueda.
                #     - urls: Diccionario que contiene el titulo de la pagina web y url que se ha encontrado en
                #             la busqueda de Google.
                for info in spider_google_result['lista_busquedas']:
                    for ind, urls in enumerate(info['urls']):
                        # Creamos una variable que se va a recrear vacia en donde se van a poner los elementos
                        # que vayamos extrayendo del diccionario de urls.
                        indice_temp = dict()

                        # Metemos dentro de la "indice_temp" toda la informacion necesaria para mostrarla en la
                        # plantilla. La informacion es la siguiente:
                        #     - id: Indica el ID del campo que se va a establecer dentro de la plantilla.
                        #     - titulo: Indica el titulo de la pagina web.
                        #     - url: Indica la URL que se va a meter dentro del campo "href" de la tabla.
                        #     - url_view: Es la URL que se va a mostar en la tabla. Esta URL tiene una edicion
                        #                 en el string.
                        #     - subtitulo: Indica que tipo de filtro avanzado ha usado para encontrar la pagina web.
                        #                  En este caso siempre es la "base" que esta sacado del motor de busqueda.
                        indice_temp['id'] = str(ind)
                        indice_temp['titulo'] = urls['titulo'].rstrip()
                        indice_temp['url'] = urls['url'].rstrip()
                        indice_temp['url_view'] = separador_url(urls['url']).rstrip()
                        indice_temp['subtitulo'] = 'base'

                        # Una vez terminado toda la introduccion de datos lo añadimos dentro de la variable "indice_list".
                        indice_list.append(indice_temp)

                        # Una vez esta todo introducido nos interesa saber si existe ya en la base de datos
                        # la informacion que hemos recolectado. Esto nos sirve para introducirla si no se ha
                        # introducido anteriormente.
                        existencia = spider_html.objects.filter(filtro=info['filtro'],
                                                                subfiltro=indice_temp['subtitulo'],
                                                                titulo=indice_temp['titulo'],
                                                                url=indice_temp['url'],
                                                                fecha=datetime.datetime.now().strftime(
                                                                    '%d-%m-%Y')).exists()

                        # En esta parte de la funcionaliad es donde se revisa si existe y si no es asi, se inserta.
                        if not existencia:
                            spider_html(filtro=info['filtro'], subfiltro=indice_temp['subtitulo'],
                                        titulo=indice_temp['titulo'], url=indice_temp['url'], html='').save()

            # Una vez terminado todo el proceso de gestion de datos para introducirlos en la plantilla se introducen
            # dentro del diccionario de contexto que servira para añadirle el contexto a la plantilla de resultados
            # del HTML.

            # Tambien se añadira al atributo "context_temp" que nos permitira pasarla a PDF si lo queremos.
            contexto['indice_list'] = indice_list
            contexto['incidencias_list'] = incidencias_list
            context_temp = contexto

            return render(request, 'spider_google/resultados.html', contexto)

    # Si no ha habido ninguna peticion POST lo unico que hace es cargar el formulario vacio.
    else:
        buscador_Form = buscador_googleForm()

    # Cuando se sepa que el formulario es invalido o el formulario esta vacio, entonces se cargara un contexto
    # con el formulario y se renderizara la pagina donde esta la plantilla del formulario.
    contexto = {'buscador_Form': buscador_Form}

    return render(request, 'spider_google/spider.html', contexto)

# Esta vista "pdf_view" lo unico que hace es establecer los parametros que se vayan a usar a la hora de crear el PDF
# y ademas pasarle la ruta donde esta el HTML que va a ser pasado a PDF.
def pdf_view(request):
    params = {
        'indice_list': context_temp['indice_list'],
        'incidencias_list': context_temp['incidencias_list'],
    }
    return render_to_pdf('spider_google/pdf.html', params)
