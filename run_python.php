<?php
// Path to the Python script
$python_script = '/path/to/your/example.py';

// Execute the Python script and get the output
$output = shell_exec("python3 $python_script");

// Display the output on the HTML page
echo "<h1>Output from Python:</h1>";
echo "<pre>$output</pre>";
?>
