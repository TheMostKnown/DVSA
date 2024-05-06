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
        <h1>Upload Your Favorite Image!</h1>
    </header>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h2> Only jpeg or png files!</h2>
            </div>
            <div class="col-12">
            <form method="POST" class="login-page" action="medium.php" enctype="multipart/form-data" name="upload">
                <input type="file" name="file" /><br>
                <p></p>
                <button type="submit" class="button_index" name="thebutton">Upload!</button>
            </div>
        </div>
    </div>
    <div class="margin-top-40">
        <button onclick="location.href='/2/images.php'" type="button" class="button_index">First task</button>
    </div>
    <script type="text/javascript" src="js/button.js"></script>
</body>
</html>
<?php
echo "ok1";
if (isset($_POST['thebutton'])) {
    $allowedtypes = ['image/gif', 'image/jpeg', 'image/jpg', 'image/pjpeg', 'image/x-png', 'image/png'];
    echo "ok2";
    if(!empty($_FILES["file"]))
    {
        echo "ok3";
        if (((@$_FILES["file"]["type"] == "image/gif") || (@$_FILES["file"]["type"] == "image/jpeg")
        || (@$_FILES["file"]["type"] == "image/jpg") || (@$_FILES["file"]["type"] == "image/pjpeg")
        || (@$_FILES["file"]["type"] == "image/x-png") || (@$_FILES["file"]["type"] == "image/png"))
        && (@$_FILES["file"]["size"] < 102400))
        {
            echo "ok4";
            $fileType = finfo_file(finfo_open(FILEINFO_MIME_TYPE), $_FILES['file']['tmp_name']);
            if (!in_array($fileType, $allowedTypes)) {
                header("Location: flag.php?flag=sne{This_one_was_ok}");
            }else{
                $tempPath = $_FILES['file']['tmp_name'];
                $destinationPath = 'upload/' . uniqid() . '_' . basename($_FILES['file']['name']);
                echo "ok5";
                if (move_uploaded_file($tempPath, $destinationPath)){
                    echo "Load in:  " . "upload/" . $destinationPath;
                } else{
                    echo "Error!!!";
                }
                echo "ok6";
            }
        }
        else
        {
            echo "upload failed!";
        }
    }
}
?>