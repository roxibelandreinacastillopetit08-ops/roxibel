// javascrips


//ejercicio1 
const nombre = "roxibel";
console.log("Hola, soy " + nombre);

//ejercicio2
const num1 = 10;
const num2 = 5;

const suma = num1 + num2;
console.log("Suma: " + suma);

const resta = num1 - num2;
console.log("Resta: " + resta);

const multiplicacion = num1 * num2;
console.log("Multiplicación: " + multiplicacion);

const division = num1 / num2;
console.log("División: " + division);


//ejercicio3
const colores = ["Rojo", "Verde", "Azul", "Amarillo", "Púrpura"];
console.log(colores);
console.log("Longitud: " + colores.length);

//ejercicio4 

const usuario = {
    nombre: "roxibel castillo",
    edad: 17,
    email: "roxibelcastillo@gmail.com"
};

console.log(usuario);
console.log(usuario.email);

//ejercicio5

const numeroIngresado = prompt("Escribe un número, por favor:");

const miNumero = Number(numeroIngresado);

const resultado = miNumero > 50;

alert(resultado);

//ejercicio6

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

//ejercicio7
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

//ejercicio8


function calcularIVA(precio) {
    return precio * 0.21;
}

const precioProducto = 100;

const ivaCalculado = calcularIVA(precioProducto);

console.log(ivaCalculado);

//ejercicio9#ejercicio9
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

//ejercicio10

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


//ejercicio13
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




