<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, inital-scale=1.0">
    <title> File uploaders team</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link rel=”stylesheet” href=”https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css” />
    <link rel="stylesheet" href="../static/style.css">
</head>
<?php 

$directory = "upload";
$images = glob($directory . "/*.jpg");
$images = $images + glob($directory . "/*.png");

?>
<body>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    <div class="container nav_bar">
        <div class="row">
            <div class="col-2 nav_logo"> <a href="/"></a> </div>
            <div class="col-10">
                <div class="nav_text">File uploaders team</div>
            </div>
        </div>
    </div>
    <header>
        <h1>There are your images!</h1>
    </header>
    <div class="grid-container">

        <?php

        foreach($images as $image)
        {
            echo "<div class='border-item image-item'>";
            echo "<img src='$image' alt='$image' width='400' height='400'>";
            echo "</div>";
        }
        ?>        
    </div>

    <script type="text/javascript" src="js/button.js"></script>
</body>
</html>