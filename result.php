<?php
    // Retrieve input values from the form (POST method)
    $x = $_POST['x'];
    $y = $_POST['y'];
    $z = $_POST['z'];

    // Call the Python script with the input values as arguments
    // escapeshellcmd prevents command injection
    $command = escapeshellcmd("python3 /var/www/html/process_input.py $x $y $z");
    $output = shell_exec($command); // Execute the command and capture the output

    // Display results on the webpage
    echo "<h1>Calculation Result</h1>";
    echo $output;
?>
