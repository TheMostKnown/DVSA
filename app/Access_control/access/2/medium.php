<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Access control</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link rel=”stylesheet” href=”https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css” />
    <link rel="stylesheet" href="../static/style.css">
</head>
<?php 

if ($_GET["user"]<>"admin" && $_GET["user"]<>"user"){
    header("Location: ../index.html");
}
if ($_GET["user"]=="admin"){
    header("Location: admin.php");
}
$secret = rand(10000, 99999);
?>
<body>
    <header>
        <h1>Hello user!</h1>
    </header>

    <p></p>
    <p></p>
    <h2>Your secret key: <?php echo $secret; ?> </h2>
</body>
</html>
