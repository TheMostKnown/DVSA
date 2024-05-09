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
$user = "user";
$role = "VIPuser";
if (!isset($_COOKIE['User3'])) {
    $encoded = base64_encode("user:password:VIPuser");
    setcookie("User3", $encoded, time()+7200);
}else{
    $decoded = base64_decode($_COOKIE['User3']);
    list($user, $pass, $role) = explode(":", $decoded);
    if($role == "admin")
    {
        header("Location: ../flag.php?flag=sne{Base64_not_4_encryption}");
    }
}

?>
<body>
    <header>
        <h1>Hello <?php echo "$user, you are $role";?></h1>
    </header>

</body>
</html>