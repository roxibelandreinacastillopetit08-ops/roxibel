#javaScript

#ejercicio1
const nombre = "Alejandro";
console.log("Hola, mi nombre es " + nombre);


#ejercicio2

const num1 = 20;
const num2 = 5;

console.log(num1 + num2);
console.log(num1 - num2);
console.log(num1 * num2);
console.log(num1 / num2);

#ejercicio3

const colores = ["Rojo", "Verde", "Azul", "Amarillo"];

console.log(colores);
console.log(colores.length);


#ejercicio4
const perfilUsuario = {
    nombre: "Ana perez",
    edad: 30,
    email: "ana.perez@gmail.com"
};

console.log(perfilUsuario);

console.log(perfilUsuario.email);

#ejercicio5

const numeroIngresado = prompt("Escribe un número, por favor:");

const miNumero = Number(numeroIngresado);

const resultado = miNumero > 50;

alert(resultado);


#ejercicio6

<!DOCTYPE html>
<html>
<head>
    <title>Interacción DOM</title>
</head>
<body>
    <p id="textoOriginal">Este texto cambiará al hacer clic.</p>
    <button id="cambiarBtn">Cambiar</button>

    <script src="script.js"></script>
</body>
</html>


const parrafo = document.getElementById("textoOriginal");
const boton = document.getElementById("cambiarBtn");

boton.addEventListener("click", function() {
    parrafo.textContent = "¡El texto ha sido modificado!";
});



#ejercicio7

<!DOCTYPE html>
<html>
<head>
    <title>Generador de Lista</title>
</head>
<body>
    <ul id="listaVacia">
    </ul>

    <script>
        const datos = ["Elemento A", "Elemento B", "Elemento C", "Elemento D"];
        const lista = document.getElementById("listaVacia");

        for (let i = 0; i < datos.length; i++) {
            const nuevoLi = document.createElement("li");
            nuevoLi.textContent = datos[i];
            lista.appendChild(nuevoLi);
        }
    </script>
</body>
</html>


#ejercicio8

function calcularIVA(precio) {
    return precio * 0.21;
}

const precioProducto = 100;

const ivaCalculado = calcularIVA(precioProducto);

console.log(ivaCalculado);

#ejercicio9
<!DOCTYPE html>
<html>
<head>
    <title>Cambio de Estilo</title>
    <style>
        #textoCambiante {
            font-size: 16px; /* Tamaño inicial */
            border: 1px solid #ccc;
            padding: 10px;
            margin: 10px 0;
            display: inline-block;
        }
    </style>
</head>
<body>
    <button id="aumentar">Aumentar Tamaño (+)</button>
    <button id="disminuir">Disminuir Tamaño (-)</button>
    
    <div id="textoCambiante">
        Este es el texto que cambiará de tamaño.
    </div>

    <script>
        const texto = document.getElementById("textoCambiante");
        const btnAumentar = document.getElementById("aumentar");
        const btnDisminuir = document.getElementById("disminuir");

        btnAumentar.addEventListener("click", function() {
            let tamañoActual = parseInt(window.getComputedStyle(texto).fontSize);
            texto.style.fontSize = (tamañoActual + 2) + "px";
        });

        btnDisminuir.addEventListener("click", function() {
            let tamañoActual = parseInt(window.getComputedStyle(texto).fontSize);
            if (tamañoActual > 8) { // Establece un límite mínimo para que no desaparezca
                texto.style.fontSize = (tamañoActual - 2) + "px";
            }
        });
    </script>
</body>
</html>


#ejercicio10
let limite = parseInt(prompt("Ingresa un número entero positivo para el límite del conteo:"));
if (isNaN(limite) || limite <= 0) {
    console.log("Entrada no válida.");
} else {
    let contador = 0;
    while (contador < limite) {
        contador++;
        if (contador === 5) {
            console.log("El número 5 se ha saltado.");
            continue;
        }
        console.log(contador);
    }
}
#ejercicio11
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Registro DOM</title>
</head>
<body>

    <form id="formularioRegistro">
        <h2>Formulario de Registro Básico</h2>
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" name="nombre" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="password">Contraseña:</label>
        <input type="password" id="password" name="password" required><br><br>

        <button type="submit">Registrar Datos</button>
    </form>

    <script>
        // Código JavaScript Básico
        const formulario = document.getElementById('formularioRegistro');

        formulario.addEventListener('submit', (evento) => {
            // 1. Previene el envío del formulario (el comportamiento por defecto)
            evento.preventDefault();

            // 2. Obtiene los valores de los inputs
            const nombre = document.getElementById('nombre').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            // 3. Crea un objeto con los datos
            const datosRegistro = {
                nombreUsuario: nombre,
                emailUsuario: email,
                contrasena: password
            };

            // 4. Muestra el objeto en la consola
            console.log("Datos capturados:", datosRegistro);
            
            // Opcional: Podrías limpiar el formulario si quisieras
            // formulario.reset();
        });
    </script>
</body>
</html>


#ejercicio12

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Lista Minimalista</title>
</head>
<body>

    <input id="i" placeholder="Nueva tarea">
    <button id="a">Añadir</button>

    <ul id="l"></ul>

    <script>
        const input = document.getElementById('i');
        const lista = document.getElementById('l');
        const botonAgregar = document.getElementById('a');

        botonAgregar.addEventListener('click', () => {
            if (input.value.trim() === "") return;

            const li = document.createElement('li');
            li.innerHTML = `${input.value} <button class="eliminar">x</button>`;
            
            lista.appendChild(li);
            input.value = '';
        });

        // Delegación de eventos para eliminar
        lista.addEventListener('click', (e) => {
            if (e.target.classList.contains('eliminar')) {
                e.target.parentElement.remove();
            }
        });
    </script>

</body>
</html>



#ejercicio13

class Rectangulo {
    constructor(ancho, alto) {
        this.ancho = ancho;
        this.alto = alto;
    }

    calcularArea() {
        return this.ancho * this.alto;
    }
}

const miRectangulo = new Rectangulo(10, 5);
console.log(miRectangulo.calcularArea());



#ejercicio14

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reloj Digital</title>
</head>
<body>

    <h1 id="reloj">Cargando...</h1>

    <script>
        const reloj = document.getElementById('reloj');

        function actualizarHora() {
            const ahora = new Date();
            const horas = ahora.getHours().toString().padStart(2, '0');
            const minutos = ahora.getMinutes().toString().padStart(2, '0');
            const segundos = ahora.getSeconds().toString().padStart(2, '0');
            
            reloj.textContent = `${horas}:${minutos}:${segundos}`;
        }

        actualizarHora();
        setInterval(actualizarHora, 1000);
    </script>

</body>
</html>




#ejercicio15


<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Galería Minimal</title>
    <style>
        .m { width: 50px; cursor: pointer; }
        #p { width: 300px; }
    </style>
</head>
<body>

    <img id="p" src="https://picsum.photos/300/200?random=1" alt="Principal">

    <div id="c">
        <img class="m" src="https://picsum.photos/50/50?random=1" data-f="https://picsum.photos/300/200?random=1" alt="Mini 1">
        <img class="m" src="https://picsum.photos/50/50?random=2" data-f="https://picsum.photos/300/200?random=2" alt="Mini 2">
        <img class="m" src="https://picsum.photos/50/50?random=3" data-f="https://picsum.photos/300/200?random=3" alt="Mini 3">
    </div>

    <script>
        const principal = document.getElementById('p');
        const contenedor = document.getElementById('c');

        contenedor.addEventListener('click', (e) => {
            // Si el elemento clickeado tiene la clase 'm' (miniatura)
            if (e.target.classList.contains('m')) {
                // Actualiza el 'src' de la imagen principal con el valor de 'data-f'
                principal.src = e.target.getAttribute('data-f');
            }
        });
    </script>

</body>
</html>
