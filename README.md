<p class="has-line-data" data-line-start="0" data-line-end="1">Este proyecto contiene pruebas automatizadas para validar la funcionalidad de la API de [Nombre del Proyecto]. Las pruebas están diseñadas para verificar la creación de kits y usuarios, asegurando que el sistema maneje correctamente los casos de éxito y los errores.</p>
<h2 class="code-line" data-line-start=2 data-line-end=3 ><a id="Archivos_2"></a>Archivos</h2>
<ul>
<li class="has-line-data" data-line-start="4" data-line-end="5"><code>configuration.py</code>: Contiene las URL del sevidor y los enpoints trabajar con las API.</li>
<li class="has-line-data" data-line-start="5" data-line-end="6"><code>data.py</code>: Almacena los encabezados y datos en formato JSON que se utilizarán para la creción de kits…</li>
<li class="has-line-data" data-line-start="6" data-line-end="7"><code>sender_stand_request.py</code>: Es la funcion para enviar la solicitud de creación de nuevo kit.</li>
<li class="has-line-data" data-line-start="7" data-line-end="9"><code>create_kit_name_kit_test.py</code>: Contiene las pruebas tanto postivas como negativas para pobrar la creación de usuarios.</li>
</ul>
<h2 class="code-line" data-line-start=9 data-line-end=10 ><a id="Requisitos_9"></a>Requisitos</h2>
<ol>
<li class="has-line-data" data-line-start="10" data-line-end="11">Tener instalado Python 3.12.4</li>
<li class="has-line-data" data-line-start="11" data-line-end="16">Instalar la paqueteria:<pre><code class="has-line-data" data-line-start="13" data-line-end="16" class="language-bash">pip <span class="hljs-number">24.2</span>
requests <span class="hljs-number">2.32</span>.<span class="hljs-number">3</span>
pytest <span class="hljs-number">8.3</span>.<span class="hljs-number">2</span>
</code></pre>
</li>
</ol>
<h2 class="code-line" data-line-start=16 data-line-end=17 ><a id="Pruebas_16"></a>Pruebas</h2>
<p class="has-line-data" data-line-start="17" data-line-end="19"><strong>1. API-1  test_create_kit_1_letter_in_name_get_success_response</strong><br>
<strong>Descripción:</strong>  se creará un usuario llenando el apartado “name” con solo una letra, en este caso la letra “a”.</p>
<p class="has-line-data" data-line-start="20" data-line-end="21"><strong>Precondición:</strong></p>
<ol>
<li class="has-line-data" data-line-start="21" data-line-end="22">Realizar una función de para crear kit en el archivo <code>sender_stand_request.py</code> y realizar la importación de la función en <code>create_kit_name_kit_test.py</code></li>
<li class="has-line-data" data-line-start="22" data-line-end="23">Tener en el archivo <code>data.py</code> los encabezados con el “authToken” y los datos a llenar en formato JSON.</li>
<li class="has-line-data" data-line-start="23" data-line-end="24">Realizar una función de para crear kit en el archivo <code>sender_stand_request.py</code> y realizar la importación de la función en <code>create_kit_name_kit_test.py</code></li>
<li class="has-line-data" data-line-start="24" data-line-end="26">Crear en el archvo <code>create_kit_name_kit_test.py</code> la función: <em>def get_kit_body(name)</em> para cambiar el contenido del cuerpo de solicitud</li>
</ol>
<p class="has-line-data" data-line-start="26" data-line-end="27"><strong>Pasos a seguir:</strong></p>
<ol>
<li class="has-line-data" data-line-start="27" data-line-end="28">Crear la función <em>positive_assert</em> tomando la función <em>def get_kit_body(name)</em> y verificando el estado del código en <strong>201</strong>.</li>
<li class="has-line-data" data-line-start="28" data-line-end="29">Crear la prueba def test_create_kit_1_letter_in_name_get_success_response en el archivo <code>create_kit_name_kit_test.py</code> y agregar que los caracteres que se agreguen a name sea “a”</li>
<li class="has-line-data" data-line-start="29" data-line-end="31">Verificar que el estado del código sea <strong>201</strong></li>
</ol>
<p class="has-line-data" data-line-start="31" data-line-end="36"><strong>Resultado esperado:</strong><br>
Código de respuesta: 201<br>
<strong>Resultado actual:</strong><br>
Código de respuesta: 201<br>
create_kit_name_kit_test.py::test_create_kit_1_letter_in_name_get_success_response PASSED [100%]</p>
<p class="has-line-data" data-line-start="37" data-line-end="39"><strong>2. API-2  test_create_user_511_letters_in_name_get_success_response</strong><br>
<strong>Descripción:</strong>  se creará un usuario llenando el apartado “name” con 511 letras, en este caso la letra “AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC”.</p>
<p class="has-line-data" data-line-start="40" data-line-end="41"><strong>Precondición:</strong></p>
<ol>
<li class="has-line-data" data-line-start="41" data-line-end="42">Realizar una función de para crear kit en el archivo <code>sender_stand_request.py</code> y realizar la importación de la función en <code>create_kit_name_kit_test.py</code></li>
<li class="has-line-data" data-line-start="42" data-line-end="43">Tener en el archivo <code>data.py</code> los encabezados con el “authToken” y los datos a llenar en formato JSON.</li>
<li class="has-line-data" data-line-start="43" data-line-end="44">Realizar una función de para crear kit en el archivo <code>sender_stand_request.py</code> y realizar la importación de la función en <code>create_kit_name_kit_test.py</code></li>
<li class="has-line-data" data-line-start="44" data-line-end="46">Crear en el archvo <code>create_kit_name_kit_test.py</code> la función: <em>def get_kit_body(name)</em> para cambiar el contenido del cuerpo de solicitud</li>
</ol>
<p class="has-line-data" data-line-start="46" data-line-end="47"><strong>Pasos a seguir:</strong></p>
<ol>
<li class="has-line-data" data-line-start="47" data-line-end="48">Crear la función <em>positive_assert</em> tomando la función <em>def get_kit_body(name)</em> y verificando el estado del código en <strong>201</strong>.</li>
<li class="has-line-data" data-line-start="48" data-line-end="49">Crear la prueba def test_create_kit_1_letter_in_name_get_success_response en el archivo <code>create_kit_name_kit_test.py</code> y agregar que los caracteres que se agreguen a name sea “AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC”</li>
<li class="has-line-data" data-line-start="49" data-line-end="51">Verificar que el estado del código sea <strong>201</strong></li>
</ol>
<p class="has-line-data" data-line-start="51" data-line-end="56"><strong>Resultado esperado:</strong><br>
Código de respuesta: 201<br>
<strong>Resultado actual:</strong><br>
Código de respuesta: 201<br>
create_kit_name_kit_test.py::test_create_kit_1_letter_in_name_get_success_response PASSED [100%]</p>
<p class="has-line-data" data-line-start="57" data-line-end="59"><strong>3. API-3  test_create_kit_1_letter_in_name_get_success_response</strong><br>
<strong>Descripción:</strong>  se creará un usuario teniendo 0 caracteres en el “name”</p>
<p class="has-line-data" data-line-start="60" data-line-end="61"><strong>Precondición:</strong></p>
<ol>
<li class="has-line-data" data-line-start="61" data-line-end="62">Realizar una función de para crear kit en el archivo <code>sender_stand_request.py</code> y realizar la importación de la función en <code>create_kit_name_kit_test.py</code></li>
<li class="has-line-data" data-line-start="62" data-line-end="63">Tener en el archivo <code>data.py</code> los encabezados con el “authToken” y los datos a llenar en formato JSON.</li>
<li class="has-line-data" data-line-start="63" data-line-end="64">Realizar una función de para crear kit en el archivo <code>sender_stand_request.py</code> y realizar la importación de la función en <code>create_kit_name_kit_test.py</code></li>
<li class="has-line-data" data-line-start="64" data-line-end="66">Crear en el archvo <code>create_kit_name_kit_test.py</code> la función: <em>def get_kit_body(name)</em> para cambiar el contenido del cuerpo de solicitud</li>
</ol>
<p class="has-line-data" data-line-start="66" data-line-end="67"><strong>Pasos a seguir:</strong></p>
<ol>
<li class="has-line-data" data-line-start="67" data-line-end="68">Crear la función <em>positive_assert</em> tomando la función <em>def get_kit_body(name)</em> y verificando el estado del código en <strong>201</strong>.</li>
<li class="has-line-data" data-line-start="68" data-line-end="69">Crear la prueba def test_create_kit_1_letter_in_name_get_success_response en el archivo <code>create_kit_name_kit_test.py</code> y agregar que los caracteres que se agreguen a name sea “”</li>
<li class="has-line-data" data-line-start="69" data-line-end="71">Verificar que el estado del código sea <strong>201</strong></li>
</ol>
<p class="has-line-data" data-line-start="71" data-line-end="78"><strong>Resultado esperado:</strong><br>
Código de respuesta: 400<br>
<strong>Resultado actual:</strong><br>
Código de respuesta: 201<br>
create_kit_name_kit_test.py::test_create_user_empty_name_get_error_response FAILED [100%]<br>
create_kit_name_kit_test.py:78 (test_create_user_empty_name_get_error_response)<br>
201 != 400</p>