<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Access control</title>
    <link rel="stylesheet" href="../static/style.css">
</head>
<?php
if (isset($_COOKIE['User1']) && $_COOKIE['User1']<>"admin" && isset($_COOKIE['isAdmin1']) && $_COOKIE['isAdmin1'] == "true") {
    header("Location: ../flag.php?flag=sne{T00_e@sy_acce55_c0ntro1}");
}
?>
<body>
    <div class="container nav_bar">
        <div class="row">
            <div class="col-2 nav_logo"> <a href="/"></a> </div>
            <div class="col-10">
                <div class="nav_text"><a href="/">Access control</a></div>
            </div>
        </div>
    </div>
    <header>
        <h1><?php if (!isset($_COOKIE['User1'])) {echo "Login to get access to our site";}else{echo "Welcome";}; ?></h1>
    </header>
    <div class="container">
    <?php if (!isset($_COOKIE['User1'])) 
    {echo '
        <div class="row">
            <div class="col-12">
                <form method="POST" class="login-page" action="simple.php">
                <p class="text-left">Login</p>
                <div class="row form__reg"><input class="form" type="text" name="login" placeholder="Login"></div>
                <p class="text-left">Password</p>
                <div class="row form__reg"><input class="form" type="password" name="password" placeholder="password"></div>
                <button type="submit" class="btn__reg" name="thebutton">Submit</button>
            </div>
        </div>';}else{
        echo '
        <div class="row"><div class="col-12">
            <h1> HELloo, just a user! </h1>
        </div></div>';}
    ?>
    </div>

</body>
</html>

<?php
if(isset($_POST["thebutton"]))
{
    if($_POST["login"] == "user" && $_POST["password"] == "user")
    {
        setcookie("User1", "user", time()+7200);
        setcookie("isAdmin1", "false", time()+7200);
    }

}
?>