<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Access control</title>

</head>
<?php 
$secret = "sne{G1immer_secret}";
?>
<body>
    <header>
        <h1>Hello admin!</h1>
    </header>

    <p></p>
    <p></p>
    <h2>Your secret key: <?php echo $secret; ?> </h2>
</body>
</html>
<?php
header("Location: denied.php");
?>