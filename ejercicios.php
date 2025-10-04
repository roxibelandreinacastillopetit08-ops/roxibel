<?php
//contador de pares y impares

$pares = 0;
$impares = 0;

for ($i = 8; $i <= 58; $i++) {
    if ($i % 2 == 0) {
        $pares++;
    } else {
        $impares++;
    }
}

echo "Pares: " . $pares . "\n";
echo "Impares: " . $impares . "\n";


?>

<?php
tabla de multiplicar del 8
$num = 8;

for ($i = 1; $i <= 10; $i++) {
    $resultado = $num * $i;
    echo "$num x $i = $resultado \n"; 
}
?>


<?php
//adivina el numero

$secreto = 12; 
$intento = 0;
$contador = 0;

echo "Iniciando juego...\n";

while ($intento != $secreto) {
    $intento++;
    $contador++;
    echo "Intento $contador: $intento\n";
}

echo "¡Adivinado! El número era $secreto. Se hicieron $contador intentos.";

?>


<?php
//Suma de Impares del 1 al 100

$suma = 0;

for ($i = 1; $i <= 100; $i++) {
    // Si el residuo es diferente de 0, es impar
    if ($i % 2 != 0) {
        $suma += $i;
    }
}

echo "La suma de los impares del 1 al 100 es: " . $suma; 

?>

<?php
 //Verificación para Licencia de Conducir
$edad = 35; 


if (($edad >= 18) && ($edad <= 65)) {
    echo "Cumple los requisitos para la licencia. ✅";
} else {
    echo "No cumple los requisitos para la licencia. ❌";
}

?>


<?php
//Dibujo de un Cuadrado con 

for ($i = 0; $i < 5; $i++) {
    $linea = "";
    
   
    for ($j = 0; $j < 5; $j++) {
        $linea .= "#";
    }
    
    echo $linea . "\n"; 
}

?>

<?php
//Clasificación de un Número
$num = -5; 

if ($num > 0) {
    echo "El número es positivo.";
} elseif ($num < 0) {
    echo "El número es negativo.";
} else {
    echo "El número es cero.";
}

?>

<?php
//Impresión Condicional: Mar y Tierra

for ($i = 1; $i <= 30; $i++) {
    
    if (($i % 3 == 0) && ($i % 5 == 0)) {
        echo "MarTierra ";
    } elseif ($i % 3 == 0) {
        echo "Mar ";
    } elseif ($i % 5 == 0) {
        echo "Tierra ";
    } else {
        echo $i . " ";
    }
}

?>

<?php
//Clasificación de Temperatura
$temp = 28; 
if ($temp < 10) {
    echo "Fría ❄️";
} elseif ($temp <= 25) {
    echo "Templada 🌤️";
} else {
    echo "Calurosa 🔥";
}

?>


<?php
 //Cuenta Regresiva de Año Nuevo
for ($i = 10; $i >= 1; $i--) {
    echo $i . "\n"; 
}

echo "¡Feliz Año Nuevo! ";

?>