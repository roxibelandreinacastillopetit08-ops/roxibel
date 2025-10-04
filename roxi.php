<?php
$nombre = "roxibel";
$apellido = "castillo";
$nombreCompleto = $nombre . " " . $apellido;
echo "Concatenación (.): " . $nombreCompleto . "\n";

$año_nacimiento = 2008;
$edad_actual = 2025;
echo "Resta: " . ($año_nacimiento - $edad_actual) . "\n"; 


?>


<?php
//ejercico1 saludo personalizado
$nombre = "roxibel";
$apellido = "castillo";
$nombreCompleto = $nombre . " " . $apellido;

echo "hola $nombreCompleto bienvenido a php (.): " . "\n"; 

?>

<?php
//ejercicio2 calculadora basica
$numero1 = 10;
$numero2 = 3;

echo "Suma: " . ($numero1 + $numero2) . "\n";          
echo "Resta: " . ($numero1 - $numero2) . "\n";         
echo "Multiplicación: " . ($numero1 * $numero2) . "\n"; 
echo "División: " . ($numero1 / $numero2) . "\n";  
?>

<?php
//ejercicio4 mayor de edad
$edad = 15;

if ($edad >= 18) {
    echo "Eres mayor de edad. Puedes ingresar.\n";
} else {
    echo "No eres mayor de edad. Acceso denegado.\n";
}
echo "\n";
?>


<?php
//ejercicio5 par o impar
$entrada = readline("Ingresa un número entero: ");
$numero_entero = intval($entrada);

if ($numero_entero % 2 == 0) {
    echo "PAR\n";
} else {
    echo "IMPAR\n";
}
?>

<?php

$edad = (int) $edad;
if ($edad >= 0 && $edad <= 12) {
      echo $clasificacion = "niño/a";
} elseif ($edad >= 13 && $edad <= 17) {
      echo  $clasificacion = "adolescente";
} elseif ($edad >= 18 && $edad <= 64) {
      echo $clasificacion = "adulto";
    } else 
        $clasificacion = "adulto mayor";

?>