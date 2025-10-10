#php
  
#ejercicio1

<?php
    echo "Hola, Mundo desde PHP!";
?>

#ejercicio2

<?php
    $nombre = "Juan";
    $edad = 30;
    echo "Hola, mi nombre es " . $nombre . " y tengo " . $edad . " años.";
?>


#ejercicio3

<?php
    $num1 = 10;
    $num2 = 5;

    echo "Suma: " . ($num1 + $num2) . "<br>";
    echo "Resta: " . ($num1 - $num2) . "<br>";
    echo "Multiplicación: " . ($num1 * $num2) . "<br>";
    echo "División: " . ($num1 / $num2) . "<br>";
?>


#ejercicio4

<?php
    $nombre = $_GET['nombre'] ?? 'Invitado';
    echo "¡Hola, " . $nombre . "!";
?>


#ejercicio5

<?php
    $paises = ["Chile", "Perú", "Argentina", "Colombia"];

    foreach ($paises as $pais) {
        echo $pais ;
    }
?>


#ejercicio6

<?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $nombre = $_POST['nombre'] ?? '';
        $email = $_POST['email'] ?? '';

        if (!empty($nombre) && !empty($email)) {
            echo "Gracias " . $nombre . ", hemos recibido tu mensaje.";
        } else {
            echo "Error: Debes completar todos los campos.";
        }
    }
?>

#ejercicio7

<?php
    $edad = $_GET['edad'] ?? 0;
    $edad = (int)$edad;

    if ($edad < 18) {
        echo "Menor de edad.";
    } elseif ($edad >= 18 && $edad < 65) {
        echo "Adulto.";
    } else {
        echo "Adulto mayor.";
    }
?>


#ejercicio8

<?php
    $numero = $_GET['num'] ?? 5;
    $numero = (int)$numero;

    echo "<h3>Tabla del " . $numero . "</h3>";
    echo "<table border='1'>";

    for ($i = 1; $i <= 10; $i++) {
        $resultado = $numero * $i;
        echo "<tr><td>" . $numero . " x " . $i . "</td><td>" . $resultado . "</td></tr>";
    }

    echo "</table>";
?>


#ejercicio9

<?php
    function calcularPromedio($numeros) {
        if (empty($numeros)) {
            return 0;
        }
        $suma = array_sum($numeros);
        $conteo = count($numeros);
        return $suma / $conteo;
    }

    $notas = [8, 9, 7, 10];
    $promedio = calcularPromedio($notas);

    echo "El promedio es: " . $promedio;
?>


#ejercicio10

<?php
    require 'header.php';
?>
<main>
    <p>Este es el contenido principal de la página.</p>
</main>
<?php
    require 'footer.php';
?>

#ejercicio11

<?php
    session_start();

    if (!isset($_SESSION['contador'])) {
        $_SESSION['contador'] = 1;
    } else {
        $_SESSION['contador']++;
    }

    echo "Has visitado esta página " . $_SESSION['contador'] . " veces.";
?>


#ejercicio12

<?php
    class Usuario {
        public $nombre;
        public $email;

        public function __construct($nombre, $email) {
            $this->nombre = $nombre;
            $this->email = $email;
        }

        public function saludar() {
            return "Hola, soy " . $this->nombre . " y mi email es " . $this->email . ".";
        }
    }

    $usuario1 = new Usuario("Ana", "ana@gmail.com");
    echo $usuario1->saludar();
?>

#ejercicio13

<?php
    session_start();
    $usuario_valido = 'admin';
    $password_valido = '1234';

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $usuario = $_POST['usuario'] ?? '';
        $password = $_POST['password'] ?? '';

        if ($usuario === $usuario_valido && $password === $password_valido) {
            $_SESSION['logeado'] = true;
            $_SESSION['usuario'] = $usuario;
            header("Location: privada.php");
            exit;
        }
    }
?>



#ejercicio14

<?php
    $archivo = 'datos.txt';

    if (file_exists($archivo)) {
        $contenido = file_get_contents($archivo);
        echo nl2br(htmlspecialchars($contenido));
    } else {
        echo "Error: El archivo no existe.";
    }
?>


#ejercicio15

<?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $nombre = $_POST['nombre'] ?? 'Desconocido';
        $mensaje = $_POST['mensaje'] ?? 'Sin mensaje';
        $timestamp = date("Y-m-d H:i:s");

        $linea_log = "[" . $timestamp . "] Nombre: " . $nombre . ", Mensaje: " . $mensaje . "\n";

        file_put_contents('log.txt', $linea_log, FILE_APPEND | LOCK_EX);
        echo "Datos guardados en log.txt";
    }
?>
